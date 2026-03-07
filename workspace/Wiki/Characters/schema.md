# Character Profile Schema

## Overview

This schema defines the comprehensive structure for character profiles in the DesertedTales lore wiki. It serves as a general-purpose history wiki designed to support multiple media formats (games, books, films, documentaries) across the historical period of Morocco and the broader Maghreb from approximately 700-2000 CE.

---

## File Naming Convention

**Format:** `Full_Name.md`  
**Rules:**
- Use full name with capitalization (e.g., `Salih_ibn_Tarif.md`, not `salih.md`)
- Replace spaces with underscores
- Include patronymic/laqab when known (e.g., `Abu_Bakr_ibn_Umar.md`)
- Avoid abbreviations unless universally recognized

---

## 1. Front Matter (YAML Header)

```yaml
---
name: "[Full Name]"
alternate_names:
  - "[Name in Arabic script]"
  - "[Common nickname]"
  - "[Laqab/Honorific]"
title: "[Primary Title/Role]"
dynasty: "[Dynasty Name or None]"
faction: "[Primary Faction/Allegiance]"
type: "[Historical Figure / Legendary Character / Composite / Fictional]"
era: "[e.g., Early Islamic Morocco, Almoravid Period, Colonial Era]"
region: "[Primary Geographic Region]"
status: "[Canon / Draft / Under Review]"
last_updated: "YYYY-MM-DD"
historical_sources: 
  - "[Primary source 1]"
  - "[Primary source 2]"
academic_consensus: "[Brief summary of scholarly agreement]"
---
```

**Field Definitions:**
| Field | Description | Required |
|-------|-------------|----------|
| `name` | Full name as commonly known | Yes |
| `alternate_names` | Variants (Arabic, nicknames, titles) | Yes |
| `title` | Primary honorific or functional role | Yes |
| `dynasty` | Ruling family affiliation | If applicable |
| `faction` | Political/religious/tribal allegiance | Yes |
| `type` | Categorization for media distinction | Yes |
| `era` | Historical time period | Yes |
| `region` | Primary geographic area | Yes |
| `status` | Wiki workflow state | Yes |
| `last_updated` | ISO 8601 date | Yes |
| `historical_sources` | Primary/medieval sources | Recommended |
| `academic_consensus` | Summary of scholarly agreement | Recommended |

---

## 2. Overview

**Purpose:** Quick identification and narrative summary  
**Length:** 4-6 sentences  
**Must Include:**
- Who they are
- What they did (primary significance)
- Temporal context (when they lived)
- Geographic context (where they operated)
- Why they matter to the broader narrative

**Format:**
```
[Full Name] was a [role/occupation] who [primary achievement/action] during the [period]. 
[Additional context: significance, legacy, or controversy]. [Brief mention of their lasting impact or cultural memory].
```

---

## 3. Etymology & Name Analysis

### Full Name Breakdown

**Name Structure:** `[Given Name] ibn [Father's Name] [Laqab/Title]`

| Component | Arabic | Meaning | Notes |
|-----------|--------|---------|-------|
| [Given Name] | [Arabic] | [Etymology] | Origin and significance |
| ibn | ابن | "son of" | Patronymic marker |
| [Father's Name] | [Arabic] | [Etymology] | Family/lineage |
| [Laqab] | [Arabic] | [Meaning] | Honorific or epithet |

### Honorifics & Titles

| Title | Origin | Significance |
|-------|--------|--------------|
| [Title 1] | [Arabic/Other] | Context and usage |

### Name Variations

- **In Arabic Sources:** [Variants from medieval sources]
- **In Modern Scholarship:** [Common transliterations]
- **In Local Tradition:** [Regional/vernacular names]

---

## 4. Dates & Vital Statistics

**Format:** Table

| Event | Date | CE/AH | Notes |
|-------|------|-------|-------|
| **Born** | [Date] | [AH if known] | [Location if known] |
| **Died** | [Date] | [AH if known] | [Circumstance if noteworthy] |
| **Age at Death** | [Years] | — | [Calculation method] |
| **Primary Active Period** | [Start]–[End] | — | [Context] |

**Date Precision Guidelines:**
| Marker | Meaning | Example |
|--------|---------|---------|
| *(exact)* | Historically attested | 744 CE |
| *(c.)* | Approximate | c. 750 CE |
| *(q.)* | Quarter-century | q. 8th century |
| *(?)* | Unknown | 750? CE |
| *(trad.)* | Traditional date | (trad. 791 CE) |

---

## 5. Origins & Lineage

### Birth & Early Life

**Place of Birth:** [Location, with historical/modern names]

**Family Background:**
- **Social Class:** [Aristocratic/Common/Military/Religious]
- **Tribal Affiliation:** [Primary tribe and subtribe]
- **Economic Basis:** [Pastoral/Agricultural/Urban/Trade]

**Formative Experiences:**
- [Key events that shaped them]
- [Influences on worldview/ideology]

### Ethnicity & Identity

| Attribute | Details |
|-----------|---------|
| **Primary Ethnicity** | [e.g., Masmuda Berber] |
| **Language(s)** | [Native and secondary languages] |
| **Cultural Affiliation** | [Regional/cultural identity] |
| **Religious Affiliation** | [At birth, later if changed] |

### Family Relations

| Relation | Name | Status | Notes |
|----------|------|--------|-------|
| **Father** | [Name] | [Living/Deceased by time of subject's prominence] | [Brief note on identity/role] |
| **Mother** | [Name] | — | [Tribe, notable if any] |
| **Paternal Grandfather** | [Name] | — | [If notable] |
| **Spouse(s)** | [Names] | — | [Number, political/affective] |
| **Sons** | [Names] | — | [If notable for succession] |
| **Daughters** | [Names] | — | [If notable] |
| **Brothers** | [Names] | — | [If politically relevant] |
| **Sisters** | [Names] | — | [If notable] |
| **Notable Descendants** | [Names] | — | [If relevant to legacy] |

---

## 6. Chronological Timeline

**Purpose:** Quick-reference table of major life events

| Year | CE | AH (if relevant) | Event | Significance |
|------|-----|-------------------|-------|---------------|
| [Year] | [CE] | [AH] | [Event description] | [Why it matters] |
| [Year] | [CE] | [AH] | [Event description] | [Why it matters] |

---

## 7. Historical Context

### Era Overview

**Time Period:** [Era name and dates]

**Major Contemporary Events:**
| Event | Date | Relationship |
|-------|------|--------------|
| [Event 1] | [Date] | [How it relates to subject] |
| [Event 2] | [Date] | [How it relates to subject] |

### Contemporary Figures

| Figure | Relationship | Nature | Notes |
|--------|-------------|--------|-------|
| [Name] | [Ally/Rival/Family/Mentor/Enemy] | [Brief descriptor] | [Context of relationship] |
| [Name] | [Ally/Rival/Family/Mentor/Enemy] | [Brief descriptor] | [Context of relationship] |

### Geographic Context

**Primary Regions:**
| Region | Role | Period |
|--------|------|--------|
| [Region 1] | [Base of operations] | [When] |
| [Region 2] | [Military/political activity] | [When] |

**Territorial Control:** [If applicable - extent of domains]

**Key Locations:**
- **[Location]:** [Significance]
- **[Location]:** [Significance]

---

## 8. Biography

### [Early Life / Rise]

[Chronological narrative of formative years, background, and rise to prominence]

### [Primary Career / Reign]

[Major period of activity - detailed narrative]

### [Major Phase / Specific Achievements]

[Thematic breakdown if needed - military campaigns, religious activities, etc.]

### [Crisis / Conflict / Controversy]

[Major challenges, internal/external conflicts]

### [Death & Succession]

[Final years, death circumstances, successor, legacy transmission]

---

## 9. Political & Religious Role

### Primary Position(s)

| Position | Faction | Period | Notes |
|----------|---------|--------|-------|
| [Role 1] | [Faction] | [Dates] | [Brief note] |
| [Role 2] | [Faction] | [Dates] | [Brief note] |

### Ideology & Beliefs

**Religious Affiliation:** [Denomination/school]
**Political Philosophy:** [Governance style, ideology]
**Key Policies:** [Major decisions that defined their rule]

### Controversies & Disputes

| Controversy | Nature | Historical View | Modern View |
|-------------|--------|-----------------|-------------|
| [Issue 1] | [Religious/Political/Personal] | [How contemporaries viewed] | [How modern scholars view] |

---

## 10. Primary Sources & Quotations

### Contemporary Accounts

| Source | Author | Date | Description | Reliability |
|--------|--------|------|-------------|-------------|
| [Source 1] | [Author] | [Date] | [Brief description] | [Assessment] |

### Attributed Quotations

> "[Quotation]"
> — [Attribution], [Source], [Date if known]

> "[Quotation]"
> — [Attribution], [Source], [Date if known]

### Epigraphic & Archaeological Evidence

- [Inscriptions, coins, buildings attributed]
- [Archaeological findings relevant to their existence/activities]

### Source Limitations

[Discussion of gaps, biases, or problems with available sources]

---

## 11. Historiography

### Medieval Arab Sources

| Source | Author | Century | Treatment of Subject |
|--------|--------|---------|---------------------|
| [Source 1] | [Author] | [Century] | [How they portray subject] |
| [Source 2] | [Author] | [Century] | [How they portray subject] |

### Modern Scholarship

**Key Scholars & Interpretations:**
| Scholar | Work | Position |
|---------|------|----------|
| [Name] | [Title] | [View on subject] |

### Conflicting Interpretations

| View | Proponents | Evidence | Counter-evidence |
|------|------------|----------|------------------|
| [Interpretation 1] | [Scholars] | [Key evidence] | [Problems with this view] |
| [Interpretation 2] | [Scholars] | [Key evidence] | [Problems with this view] |

### Current Academic Consensus

[Summary of where mainstream scholarship stands]

---

## 12. Associated Artefacts

### Buildings & Architecture

| Structure | Location | Type | Period | Status |
|-----------|----------|------|--------|--------|
| [Name] | [Location] | [Mosque/Palace/Fortress] | [Date] | [Extant/Ruined/Destroyed] |

### Texts & Manuscripts

| Work | Type | Language | Period | Notes |
|------|------|----------|--------|-------|
| [Title] | [Religious/Administrative/Literary] | [Language] | [Date] | [Attribution status] |

### Coins & Inscriptions

- [Numismatic evidence]
- [Epigraphic evidence]

### Archaeological Sites

- [Sites associated with them]

---

## 13. Symbolism & Iconography

### Religious/Military Symbols

- [Symbols associated with their movement/faction]
- [Iconographic elements]

### Heraldic Elements

- [Coat of arms/emblem if any]
- [Colors and their significance]
- [Animals/devices used]

### Artistic Representations

| Period | Type | Description | Location |
|--------|------|-------------|----------|
| [Century] | [Painting/Manuscript/Sculpture] | [Description] | [Collection/Museum] |

### Modern Iconography

- [How they're depicted in modern Morocco]
- [National/regional significance]

---

## 14. Legacy & Significance

### Historical Impact

**Immediate:**
- [Short-term effects of their actions]

**Long-term:**
- [Lasting effects on Morocco/region]
- [Institutional/political/religious legacy]

### Modern Assessment

**Historiographical:**
- [How historians view them today]
- [Changes in scholarly perception over time]

**Cultural:**
- [How they're remembered in Moroccan culture]
- [Regional/local memory]

### Popular Memory

- [In Moroccan folklore]
- [In contemporary discourse]
- [In education]

---

## 15. Pop Culture & Modern Reception

### Media Appearances

| Medium | Title | Date | Portrayal |
|--------|-------|------|-----------|
| [Film/Documentary/Game] | [Name] | [Year] | [Brief note on portrayal] |

### Academic Treatment

- [Major scholarly works about them]
- [Controversies in modern scholarship]

### Cultural References

- [In literature, art, music]
- [Political instrumentalization]

---

## 16. Related Entries

### Internal Links

**Characters:**
- [[Wiki/Characters/Name]] — [Relationship]
- [[Wiki/Characters/Name]] — [Relationship]

**Events:**
- [[Wiki/Events/Name]] — [Involved in/as context]
- [[Wiki/Events/Name]] — [Involved in/as context]

**Locations:**
- [[Wiki/Locations/Name]] — [Associated region]
- [[Wiki/Locations/Name]] — [Associated region]

**Factions:**
- [[Wiki/Factions/Name]] — [Member/Leader]
- [[Wiki/Factions/Name]] — [Ally/Enemy]

**Concepts:**
- [[Wiki/Concepts/Name]] — [Related]
- [[Wiki/Concepts/Name]] — [Related]

---

## 17. Media Adaptations

*(formerly "Game-Specific Information")*

### Role in Narrative

[Character's function in the broader DesertedTales narrative]

### Media Potential

| Medium | Suitability | Notes |
|--------|-------------|-------|
| **Video Game** | [High/Medium/Low] | [Why and how] |
| **Film/Television** | [High/Medium/Low] | [Why and how] |
| **Novel/Book** | [High/Medium/Low] | [Why and how] |
| **Documentary** | [High/Medium/Low] | [Why and how] |

### Archetype

[Suggested character archetype for adaptation]

### Key Story Hooks

- [Compelling narrative elements]
- [Thematic conflicts]
- [Relationship dynamics]

---

## 18. Further Reading

### Primary Historical Sources

- [Source 1]: [Brief note]
- [Source 2]: [Brief note]

### Secondary Sources

- [Scholar, Year]: [Title]
- [Scholar, Year]: [Title]

### Academic References

- [Full bibliography entry]
- [Full bibliography entry]

### Lore Source

`Lore/Characters/[Name].md` — [Notes on contradictions resolved]

---

## Formatting Rules

### Markdown Standards

| Element | Syntax | Example |
|---------|--------|---------|
| Title | `#` | `# Name` |
| Section | `##` | `## Overview` |
| Subsection | `###` | `### Early Life` |
| Bold | `**text**` | **important** |
| Italic | `*text*` | *foreign term* |
| Internal Link | `[[Wiki/Path|Text]]` | [[Wiki/Characters/Salih_ibn_Tarif|Salih ibn Tarif]] |
| Table | `\| \|` | See examples above |

### Language Usage

| Language | Treatment |
|----------|-----------|
| **Arabic** | Italicize, use macrons (ā, ī, ū) |
| **Tamazight** | Italicize, note variant |
| **Place Names** | Modern name (historical variants) |

### Citation Style

- **In-text:** `(Author, Year)` or `(Source, Century)`
- **Footnotes:** Use markdown footnote syntax `[^1]`
- **Sources section:** Full bibliography

---

## Canon vs. Speculation

### Uncertainty Markers

| Marker | Meaning | Use For |
|--------|---------|---------|
| *(exact)* | Historically attested | Confirmed facts |
| *(c.)* | Approximate | Inferred or scholarly consensus |
| *(trad.)* | From oral/narrative sources | Folklore, legendary |
| *(unconfirmed)* | Suspected but unproven | Reasonable speculation |
| *(lore)* | Game-only addition | Fictional expansion |

### Prohibited Phrases

Never use:
- ❌ "Possibly..." or "maybe..." without marking
- ❌ Contradictory views in main text (resolve in Lore)
- ❌ "[Player decides]" or "[up to writer]"
- ❌ Unsupported speculation presented as fact

---

## Workflow: Vault → Lore → Wiki

### Phase 1: Research (Vault)
- Collect raw notes in `Vault/UnstructuredData/`
- Document all sources
- Note contradictions and gaps

### Phase 2: Draft (Lore)
- Organize in `Lore/Characters/`
- Present multiple interpretations
- Mark options for decision

### Phase 3: Review
- Review options
- Resolve contradictions
- Fill gaps with agreed assumptions

### Phase 4: Canonization (Wiki)
- Write final profile following this schema
- Remove speculation markers
- Record decisions made
- Link to Lore source file

### Phase 5: Validation
- All required sections present
- Front matter complete
- No "Options" remain
- Internal links functional

---

## Schema Version

**Version:** 2.0  
**Effective Date:** 2026-03-07  
**Maintainer:** OmniversifyBot  
**Review Cycle:** As needed for new character types and media requirements

---

## Appendix: Section Checklist

| Section | Required | Word Count (Major Character) |
|---------|----------|------------------------------|
| Front Matter | Yes | — |
| Overview | Yes | 100-150 words |
| Etymology | Recommended | 200-400 words |
| Dates & Vital Stats | Yes | Table |
| Origins & Lineage | Yes | 300-600 words |
| Chronological Timeline | Recommended | Table |
| Historical Context | Recommended | 200-400 words |
| Biography | Yes | 800-2000 words |
| Political/Religious Role | Yes | 300-500 words |
| Primary Sources | Recommended | 200-400 words |
| Historiography | Recommended | 200-400 words |
| Associated Artefacts | If applicable | 150-300 words |
| Symbolism | Recommended | 150-300 words |
| Legacy | Yes | 300-500 words |
| Pop Culture | If applicable | 100-200 words |
| Related Entries | Yes | Lists |
| Media Adaptations | If applicable | 150-300 words |
| Further Reading | Yes | Lists |

---

*This schema ensures comprehensive, citation-ready character profiles suitable for historical reference, academic use, and multi-media adaptation.*
