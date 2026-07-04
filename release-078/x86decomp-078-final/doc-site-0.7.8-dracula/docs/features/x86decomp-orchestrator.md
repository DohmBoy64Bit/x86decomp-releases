---
title: x86decomp.orchestrator
description: Source module reference for x86decomp.orchestrator.
---

# `x86decomp.orchestrator`

**Source path:** `src/x86decomp/orchestrator.py`  
**SHA-256:** `752a6e6b5d4f931007e93ee7898f6a0d2500b044266c7153a27be7e7eb49477e`

| Symbol | Kind | Line | Body lines |
| --- | --- | ---: | --- |
| `PipelineStage.from_dict` | method | 100 | 101, 103, 104, 106, 107, 109, 114, 115, 116, 120, 121, 123… |
| `PipelineManifest.load` | method | 159 | 160, 161, 163, 164, 166, 167, 169, 170, 172, 173, 174, 176… |
| `Orchestrator.__init__` | method | 188 | 189, 190, 191, 192, 193, 194, 195, 196, 197, 214 |
| `Orchestrator.close` | method | 218 | 219 |
| `Orchestrator.__enter__` | method | 221 | 222 |
| `Orchestrator.__exit__` | method | 224 | 225 |
| `Orchestrator._transaction` | method | 227 | 228 |
| `Orchestrator.register` | method | 230 | 231, 232, 234, 235, 236, 237, 269 |
| `Orchestrator._idempotency_key` | method | 271 | 272, 273, 280, 293 |
| `Orchestrator._event` | method | 295 | 296 |
| `Orchestrator._completed_result_is_intact` | method | 301 | 303, 305, 309, 310, 312, 324 |
| `Orchestrator._materialize_outputs` | method | 326 | 329, 330, 331, 332, 333, 358 |
| `Orchestrator._dependency_states` | method | 360 | 361, 362, 368 |
| `Orchestrator.run` | method | 370 | 371, 372, 373, 399, 400 |
| `Orchestrator._set_state` | method | 402 | 403, 404, 405, 406 |
| `Orchestrator._run_stage` | method | 417 | 418, 419, 420, 421, 443, 457, 458, 459, 462, 463, 464, 475… |
| `Orchestrator.recover_stale_jobs` | method | 526 | 528, 530, 531, 541, 542, 550, 551, 562, 564 |
| `Orchestrator.cancel` | method | 571 | 572, 573, 588 |
| `Orchestrator.retry` | method | 590 | 591, 595, 597, 598, 613 |
| `Orchestrator._update_pipeline_status` | method | 615 | 616, 617, 629 |
| `Orchestrator.status` | method | 631 | 632, 633, 635, 636, 653 |
| `create_default_pipeline` | function | 662 | 669, 670, 671, 672, 674, 711, 732, 733, 735, 742, 743 |
