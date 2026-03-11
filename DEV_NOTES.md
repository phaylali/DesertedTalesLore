# DEV_NOTES.md — Technical Documentation

This document covers the technical architecture, tooling, and workflows that power DesertedTalesLore.

## Project Overview

**DesertedTalesLore** is an AI-assisted worldbuilding repository focused on Moroccan history (8th–11th centuries CE), currently specializing in the Barghawata dynasty. The project maintains a structured **Vault → Lore → Wiki** pipeline for transforming raw historical research into polished, consistent character profiles and realm documentation.

## Repository Structure

```
DesertedTalesLore/
├── workspace/                    # Main working directory
│   ├── AGENTS.md               # AI agent instructions & workflow
│   ├── SOUL.md                 # AI identity & personality
│   ├── IDENTITY.md             # Project identity & current task
│   ├── USER.md                 # User context & preferences
│   ├── BOOTSTRAP.md            # Initial setup instructions
│   ├── TOOLS.md                # Local tooling notes
│   ├── HEARTBEAT.md            # Periodic task checklist
│   ├── memory/                 # Session memory & daily logs
│   │   └── YYYY-MM-DD.md       # Daily work logs
│   ├── Vault/                  # Raw source material (unstructured)
│   │   ├── UnstructuredData/  # Notes, research, fragments
│   │   └── characters/         # Raw character notes
│   ├── Lore/                   # Draft material (semi-organized)
│   │   └── Characters/        # Working drafts
│   ├── Wiki/                   # Canonized content (final)
│   │   ├── Characters/         # Character profiles
│   │   ├── Realms/             # Location/kingdom docs
│   │   ├── Events/             # Historical events
│   │   ├── Factions/            # Organizations & groups
│   │   ├── Concepts/           # Themes & ideas
│   │   └── Locations/          # Geographic entries
│   ├── .smtcmp_vector_db/      # Semantic search index
│   ├── .smtcmp_json_db/        # Structured data storage
│   └── tree.canvas             # Visual knowledge graph
├── .git/                        # Git repository
├── .gitignore
└── README.md
```

## Tech Stack & Tools

### AI Infrastructure
- **ClawX** — Desktop AI assistant (based on OpenClaw)
- **Vector Database** — Semantic search for finding related content
- **JSON Database** — Structured data persistence
- **Memory System** — Daily logs + long-term memory (MEMORY.md)

### Research Tools
- **Web Search** — DuckDuckGo integration for historical research
- **Web Fetch** — Content retrieval from URLs
- **File System** — Full read/write access to workspace

### Obsidian Integration
The workspace uses Obsidian vault structure:
- Markdown-based notes
- Internal wiki-style linking `[[Wiki/Path]]`
- Canvas files for visual organization
- Community plugins for enhanced functionality

## Data Pipeline

### Phase 1: Vault (Research)
Raw source material lives in `Vault/UnstructuredData/`:
- Research notes and fragments
- Web search results
- Historical source excerpts
- Contradictions and gaps marked

### Phase 2: Lore (Drafting)
Semi-organized content in `Lore/Characters/`:
- Multiple interpretations preserved
- Options marked for decision
- Source citations included

### Phase 3: Wiki (Canonization)
Final polished content in `Wiki/`:
- Schema-compliant profiles
- All contradictions resolved
- Links to Lore source file
- Ready for publication

## Character Schema (Version 2.0)

Comprehensive profile structure defined in `Wiki/Characters/schema.md`:

| Section | Purpose |
|---------|---------|
| Front Matter (YAML) | Metadata, alternate names, sources |
| Overview | 4-6 sentence summary |
| Etymology | Name breakdown with Arabic/Tamazight |
| Dates & Vital Statistics | Table format with precision markers |
| Origins & Lineage | Family, tribe, ethnicity |
| Chronological Timeline | Major events table |
| Historical Context | Contemporary figures, geography |
| Biography | Detailed narrative (800-2000 words) |
| Political & Religious Role | Positions, ideology |
| Primary Sources | Contemporary accounts |
| Historiography | Modern scholarship |
| Associated Artefacts | Buildings, texts, coins |
| Symbolism | Religious/military symbols |
| Legacy | Historical & cultural impact |
| Pop Culture | Modern reception |
| Related Entries | Cross-references |
| Media Adaptations | Story potential & hooks |
| Further Reading | Bibliography |

### Precision Markers

| Marker | Meaning |
|--------|---------|
| *(exact)* | Historically attested |
| *(c.)* | Approximate |
| *(q.)* | Quarter-century |
| *(?)* | Unknown |
| *(trad.)* | Traditional date |
| *(unconfirmed)* | Suspected but unproven |
| *(lore)* | Fictional expansion |

## Workflow: AI Session

### Startup Sequence
1. Read `SOUL.md` — AI identity
2. Read `USER.md` — User context
3. Read `memory/YYYY-MM-DD.md` — Recent sessions
4. If main session: Read `MEMORY.md` — Long-term memory

### Character Processing Workflow
1. Find source in `Vault/UnstructuredData/characters/`
2. Search web for additional context
3. Create Wiki entry following `Wiki/Characters/schema.md`
4. Resolve contradictions, document decisions
5. Present summary, ask for next action

### Memory & Continuity
- **Daily logs:** `memory/YYYY-MM-DD.md` — Session notes
- **Long-term:** `MEMORY.md` — Curated memories (main session only)
- All significant work committed to files

## Semantic Search

The project for semantic search:
- `.smtcmp_vector_db/` — Compressed vector database
- Enables uses vector embeddings finding related content across the wiki
- Used by AI for contextual recall

## Git Workflow

Standard git operations for version control:
- Untracked: New research, drafts
- Staged: Ready for commit
- Committed: Incremental progress

## Key Historical Sources

### Medieval Arab Sources
- Ibn Khaldun — *Muqaddimah* & *History of the Berbers*
- al-Bakri — *Geographic Compendium*
- al-Ya'qubi — *Kitab al-Buldan*
- Ibn Hazm — *al-Fasl fi al-Milal wa al-Ahwa*

### Modern Scholarship
- John Iskander — Barghawata research
- Dr. Mohamed Chtatou — Moroccan Berber studies
- Various academic papers on North African history

## Content Status Levels

| Status | Meaning |
|--------|---------|
| **Draft** | Initial creation, incomplete |
| **Under Review** | Complete but awaiting review |
| **Canon** | Finalized, official content |

## Extending the Project

### Adding New Characters
1. Create source file in `Vault/UnstructuredData/characters/[Name].md`
2. Run character creation workflow
3. Output to `Wiki/Characters/[Name].md`
4. Link from relevant entries

### Adding New Realms
1. Create source research in `Vault/UnstructuredData/`
2. Create Realm entry following Realm schema
3. Add to appropriate Wiki category

### Adding New Historical Periods
1. Update `IDENTITY.md` with new focus
2. Create new Vault structure
3. Develop appropriate schema extensions

## Environment Variables & Configuration

- **Project root:** `/home/phaylali/Documents/Apps/DesertedTalesLore`
- **Workspace:** `workspace/`
- **AI context files:** AGENTS.md, SOUL.md, IDENTITY.md

## Current Focus

As of 2026-03-11:
- Complete Barghawata dynasty Wiki profiles (7 rulers)
- Barghawata Confederacy realm document
- Building interconnected wiki with cross-references

## Notes for Contributors

1. **Always use precision markers** for uncertain dates/facts
2. **Document contradictions** — never hide them
3. **Cite sources** — both primary and secondary
4. **Link generously** — internal connections strengthen the wiki
5. **Follow schema** — consistency enables tooling

---

*This is a living technical document. Update as project evolves.*
 the