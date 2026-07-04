---
title: x86decomp.project_state
description: Source module reference for x86decomp.project_state.
---

# `x86decomp.project_state`

**Source path:** `src/x86decomp/project_state.py`  
**SHA-256:** `703c7418398cb445f9d235035fa8b3d6760fa3297064df3efc2032be2ce907a5`

| Symbol | Kind | Line | Body lines |
| --- | --- | ---: | --- |
| `ProjectCheck.to_dict` | method | 77 | 78 |
| `ProjectStateDatabase.__init__` | method | 88 | 89, 90, 91, 92, 93, 94, 95, 96, 97 |
| `ProjectStateDatabase.close` | method | 105 | 106 |
| `ProjectStateDatabase.__enter__` | method | 108 | 109 |
| `ProjectStateDatabase.__exit__` | method | 111 | 112 |
| `ProjectStateDatabase.transaction` | method | 115 | 116, 117 |
| `ProjectStateDatabase.integrity_check` | method | 125 | 126, 127 |
| `ProjectStateDatabase.record_migration` | method | 129 | 139 |
| `ProjectStateDatabase.snapshot` | method | 149 | 150, 151, 152, 153, 155, 161, 162, 163, 168 |
| `ProjectStateDatabase.upsert_artifact_reference` | method | 170 | 171 |
| `ProjectStateDatabase.artifact_digests` | method | 178 | 179 |
| `state_database_path` | function | 182 | 183 |
| `create_project_backup` | function | 186 | 188, 189, 191, 192, 194, 195, 196, 201, 202, 203, 218 |
| `_migration_2_to_3` | function | 221 | 222, 235, 237, 238, 239, 249 |
| `migrate_project` | function | 252 | 258, 259, 260, 261, 263, 264, 266, 268, 269, 270, 283, 284… |
| `check_project_state` | function | 314 | 315, 316, 317, 318, 319, 320, 350 |
| `repair_project_state` | function | 353 | 355, 356, 357, 358, 359, 364, 365, 370, 380 |
| `project_gc` | function | 383 | 384, 385, 386 |
| `restore_project_backup` | function | 389 | 391, 392, 393, 395, 397, 398, 433, 434 |
