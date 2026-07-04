const { chromium } = require("playwright");

const baseUrl = process.env.MKDOCS_BASE_URL || "http://127.0.0.1:8001";
const viewports = [
  { name: "mobile-390", width: 390, height: 844 },
  { name: "tablet-768", width: 768, height: 1024 },
  { name: "desktop-1280", width: 1280, height: 900 },
];

async function pageUrls() {
  const res = await fetch(`${baseUrl}/sitemap.xml?audit=${Date.now()}`);
  if (!res.ok) {
    throw new Error(`Unable to fetch sitemap: ${res.status} ${res.statusText}`);
  }
  const xml = await res.text();
  return [...xml.matchAll(/<loc>([^<]+)<\/loc>/g)]
    .map((match) => match[1])
    .filter((url) => !url.endsWith("/404/"));
}

function px(value) {
  if (!value) return 0;
  return Number(String(value).replace("px", ""));
}

async function auditPage(page, url, viewportName) {
  await page.goto(`${url}${url.includes("?") ? "&" : "?"}audit=${viewportName}-${Date.now()}`, {
    waitUntil: "domcontentloaded",
    timeout: 30000,
  });

  return page.evaluate((vp) => {
    const doc = document.documentElement;
    const bodyText = document.body ? document.body.innerText : "";
    const h1 = document.querySelector("h1");
    const h2 = document.querySelector("h2");
    const h3 = document.querySelector("h3");
    const css = (el) => (el ? getComputedStyle(el) : null);
    const font = (el) => (el ? Number(getComputedStyle(el).fontSize.replace("px", "")) : 0);
    const cards = [...document.querySelectorAll("a.doc-card")].map((card) => {
      const href = card.getAttribute("href") || "";
      return {
        href,
        path: href ? new URL(href, location.href).pathname : "",
        text: (card.textContent || "").trim().replace(/\s+/g, " ").slice(0, 90),
      };
    });
    const badCards = cards.filter((card) =>
      /\/project-examples\/project-examples\//.test(card.path) ||
      /\/reference\/(commands|schemas|integrations|features|functions|tests)\//.test(card.path) ||
      /\/release-evidence\/(verification|source-coverage|changelog|about)\//.test(card.path)
    );
    const preOverflow = [...document.querySelectorAll("pre")].filter(
      (pre) => pre.scrollWidth > pre.clientWidth + 1 && getComputedStyle(pre).overflowX === "visible"
    ).length;
    const preVerticalBars = [...document.querySelectorAll("pre")].filter((pre) => {
      const style = getComputedStyle(pre);
      return style.overflowY !== "hidden";
    }).length;
    const flatBlackCodeBlocks = [...document.querySelectorAll("pre")].filter((pre) => {
      const style = getComputedStyle(pre);
      return style.backgroundImage === "none" && /rgb\(33,\s*34,\s*44\)/.test(style.backgroundColor);
    }).length;
    const opaquePreCodeBackgrounds = [...document.querySelectorAll("pre code")].filter((code) => {
      const style = getComputedStyle(code);
      return style.backgroundColor !== "rgba(0, 0, 0, 0)";
    }).length;
    const tinyStepNumbers = [...document.querySelectorAll(".doc-step-number")].filter((number) => {
      const style = getComputedStyle(number);
      return Number(style.fontSize.replace("px", "")) < 14 || number.getBoundingClientRect().width < 26;
    }).length;
    const tableParentOverflow = [...document.querySelectorAll("table")].filter((table) => {
      const parent = table.parentElement;
      return parent && parent.scrollWidth > parent.clientWidth + 1 && getComputedStyle(parent).overflowX === "visible";
    }).length;
    const linksWithPilcrowText = [...document.querySelectorAll("a")].filter((link) =>
      (link.textContent || "").includes("¶")
    ).length;
    return {
      viewport: vp,
      url: location.pathname,
      title: document.title,
      bodyChars: bodyText.length,
      bodyFont: css(document.body).fontSize,
      h1Font: font(h1),
      h2Font: font(h2),
      h3Font: font(h3),
      hasH1: Boolean(h1),
      headerlinks: document.querySelectorAll("a.headerlink").length,
      linksWithPilcrowText,
      visiblePilcrow: bodyText.includes("¶"),
      horizontalOverflow: doc.scrollWidth > doc.clientWidth + 1,
      overflowPx: doc.scrollWidth - doc.clientWidth,
      preOverflow,
      preVerticalBars,
      flatBlackCodeBlocks,
      opaquePreCodeBackgrounds,
      tinyStepNumbers,
      tableParentOverflow,
      badCards,
    };
  }, viewportName);
}

function problemsFor(result) {
  const problems = [];
  if (!result.hasH1) problems.push("missing-h1");
  if (result.bodyChars < 160) problems.push("very-short-body");
  if (result.headerlinks) problems.push("headerlink-anchor-present");
  if (result.linksWithPilcrowText || result.visiblePilcrow) problems.push("visible-pilcrow");
  if (result.horizontalOverflow) problems.push(`document-overflow-${result.overflowPx}`);
  if (result.badCards.length) problems.push("bad-card-path");
  if (result.preOverflow) problems.push("uncontained-pre-overflow");
  if (result.preVerticalBars) problems.push("code-block-vertical-scrollbar");
  if (result.flatBlackCodeBlocks) problems.push("flat-black-code-block");
  if (result.opaquePreCodeBackgrounds) problems.push("opaque-nested-code-background");
  if (result.tinyStepNumbers) problems.push("tiny-step-number");
  if (result.tableParentOverflow) problems.push("uncontained-table-overflow");
  if (result.viewport === "mobile-390" && result.h2Font && result.h1Font <= result.h2Font) {
    problems.push("collapsed-mobile-heading-hierarchy");
  }
  if (result.viewport === "tablet-768" && result.h2Font && result.h1Font <= result.h2Font) {
    problems.push("collapsed-tablet-heading-hierarchy");
  }
  if (result.viewport === "desktop-1280" && result.h1Font < 30) {
    problems.push("desktop-h1-too-small");
  }
  return problems;
}

(async () => {
  const urls = await pageUrls();
  const browser = await chromium.launch({ headless: true });
  const failures = [];
  const samples = [];
  let checked = 0;

  try {
    for (const viewport of viewports) {
      let page = await browser.newPage({ viewport });
      for (const url of urls) {
        let result;
        let lastError;
        try {
          for (let attempt = 1; attempt <= 3; attempt += 1) {
            try {
              result = await auditPage(page, url, viewport.name);
              lastError = undefined;
              break;
            } catch (error) {
              lastError = error;
              await page.close().catch(() => {});
              await new Promise((resolve) => setTimeout(resolve, 200 * attempt));
              page = await browser.newPage({ viewport });
            }
          }
        } catch (error) {
          lastError = error;
        }
        if (!result) {
          failures.push({
            viewport: viewport.name,
            url,
            problems: ["navigation-or-evaluation-error"],
            message: String(lastError).slice(0, 300),
          });
          continue;
        }
        checked += 1;
        if (
          samples.length < 12 &&
          ["/", "/getting-started/", "/commands/claim-attach/", "/project-examples/", "/reference/", "/source-coverage/"].includes(result.url)
        ) {
          samples.push(result);
        }
        const problems = problemsFor(result);
        if (problems.length) {
          failures.push({
            viewport: viewport.name,
            url: result.url,
            title: result.title,
            problems,
            overflowPx: result.overflowPx,
            h1Font: result.h1Font,
            h2Font: result.h2Font,
            badCards: result.badCards.slice(0, 3),
          });
        }
      }
      await page.close().catch(() => {});
    }
  } finally {
    await browser.close();
  }

  const summary = {
    baseUrl,
    pages: urls.length,
    viewports,
    checked,
    failureCount: failures.length,
    failures: failures.slice(0, 50),
    samples,
  };
  console.log(JSON.stringify(summary, null, 2));
  if (failures.length) {
    process.exitCode = 1;
  }
})();
