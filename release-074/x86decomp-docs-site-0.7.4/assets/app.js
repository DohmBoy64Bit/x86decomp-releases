(() => {
  const root = window.X86DOCS_ROOT || '';
  const html = document.documentElement;
  const saved = localStorage.getItem('x86docs-theme');
  if (saved) html.dataset.theme = saved;
  document.querySelector('[data-theme-toggle]')?.addEventListener('click', () => {
    const next = html.dataset.theme === 'dark' ? 'light' : 'dark';
    html.dataset.theme = next; localStorage.setItem('x86docs-theme', next);
  });
  const sidebar = document.querySelector('[data-sidebar]');
  document.querySelector('[data-menu-toggle]')?.addEventListener('click', () => sidebar?.classList.toggle('open'));
  document.querySelectorAll('pre').forEach(pre => {
    const button = document.createElement('button'); button.className = 'copy-button'; button.textContent = 'Copy';
    button.addEventListener('click', async () => {
      await navigator.clipboard.writeText(pre.innerText.replace(/^Copy\s*/, ''));
      button.textContent = 'Copied'; setTimeout(() => button.textContent = 'Copy', 1100);
    }); pre.appendChild(button);
  });
  const dialog = document.querySelector('[data-search-dialog]');
  const input = document.querySelector('[data-search-input]');
  const results = document.querySelector('[data-search-results]');
  const openSearch = () => { if (!dialog) return; dialog.hidden = false; setTimeout(() => input?.focus(), 0); };
  const closeSearch = () => { if (!dialog) return; dialog.hidden = true; if (input) input.value = ''; if (results) results.innerHTML = ''; };
  document.querySelector('[data-search-trigger]')?.addEventListener('click', openSearch);
  document.querySelector('[data-search-close]')?.addEventListener('click', closeSearch);
  dialog?.addEventListener('click', e => { if (e.target === dialog) closeSearch(); });
  document.addEventListener('keydown', e => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); openSearch(); }
    if (e.key === 'Escape') closeSearch();
  });
  const normalize = s => (s || '').toLowerCase();
  const search = query => {
    const q = normalize(query).trim();
    if (!results) return;
    if (q.length < 2) { results.innerHTML = '<div class="search-empty">Enter at least two characters.</div>'; return; }
    const tokens = q.split(/\s+/);
    const items = (window.X86DOCS_SEARCH_INDEX || []).map(item => {
      const title = normalize(item.title), text = normalize(item.text), tags = normalize(item.tags);
      let score = 0;
      for (const token of tokens) {
        if (title === token) score += 80;
        if (title.startsWith(token)) score += 45;
        if (title.includes(token)) score += 24;
        if (tags.includes(token)) score += 12;
        if (text.includes(token)) score += 4;
      }
      return {item, score};
    }).filter(x => x.score > 0).sort((a,b) => b.score - a.score || a.item.title.localeCompare(b.item.title)).slice(0, 60);
    if (!items.length) { results.innerHTML = '<div class="search-empty">No matching documentation found.</div>'; return; }
    results.innerHTML = items.map(({item}) => `<a class="search-result" href="${root}${item.url}"><strong>${escapeHtml(item.title)}</strong><span>${escapeHtml(item.type)} · ${escapeHtml(item.text.slice(0, 170))}</span></a>`).join('');
  };
  const escapeHtml = s => String(s).replace(/[&<>'"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]));
  input?.addEventListener('input', e => search(e.target.value));
  document.querySelectorAll('[data-filter-input]').forEach(inputEl => {
    const target = document.querySelector(inputEl.dataset.filterTarget);
    inputEl.addEventListener('input', () => {
      const q = normalize(inputEl.value).trim();
      target?.querySelectorAll('[data-filter-item]').forEach(item => {
        item.hidden = q && !normalize(item.textContent).includes(q);
      });
    });
  });
})();
