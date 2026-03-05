# Character Profile Schema

## File Naming Convention

**Format:** `Full_Name.md`  
**Rules:**
- Use full name with capitalization (e.g., `Salih_ibn_Tarif.md`, not `salih.md`)
- Replace spaces with underscores
- Include patronymic/laqab when known (e.g., `Abu_Bakr_ibn_Umar.md`)
- Avoid abbreviations unless universally recognized

---

## Required Sections

All character profiles MUST include these sections in this order:

---

### 1. Front Matter (YAML Header)

```yaml
---
name: "[Full Name]"
alternate_names:
  - "[Name in Arabic]"
  - "[Nickname]"
  - "[Laqab/Honorific]"
title: "[Primary Title/Role]"
dynasty: "[Dynasty Name or None]"
faction: "[Primary Faction/Allegiance]"
type: "[Historical Figure / Legendary Character / Composite / Fictional]"
status: "[Canon / Draft / Under Review]"
last_updated: "YYYY-MM-DD"
---
```

**Field Definitions:**
- **name:** Full name as commonly known
- **alternate_names:** Array of variants (Arabic script, nicknames, titles)
- **title:** Primary honorific or functional role
- **dynasty:** Ruling family affiliation, if any
- **faction:** Political/religious/tribal allegiance
- **type:** Categorization for game/lore distinction
- **status:** Wiki workflow state
- **last_updated:** ISO 8601 date

---

### 2. Overview

**Purpose:** Quick identification and role summary  
**Length:** 2-4 sentences  
**Must Include:**
- Who they are
- What they did (primary significance)
- Temporal context (when they lived)
- Geographic context (where they operated)

**Format:**
```
[Full Name] was a [role/occupation] who [primary achievement/action] during the [period]. 
[Additional context: significance, legacy, or controversy].
```

---

### 3. Dates & Vital Statistics

**Format:** Table or structured list

| Field | Value | Notes |
|-------|-------|-------|
| **Born** | [Year] | [Specificity: exact/circa/quarter-century] |
| **Died** | [Year] | [Circumstance if noteworthy] |
| **Aged** | [Age at death] | [Calculate if both dates known] |
| **Reign/Active** | [Start]–[End] | [Primary period of influence] |

**Rules:**
- Use CE/Common Era for all dates
- Use "c." for circa (e.g., "c. 744")
- Use "?" for unknowns
- For ranges: "742–744" or "c. 790–c. 850"

---

### 4. Origins & Lineage

**Subsections (include all that apply):**

#### Birth & Early Life
- Place of birth
- Family background
- Tribal/clan affiliations

#### Ethnicity & Identity
- Tribal group(s)
- Language(s) spoken
- Cultural background

#### Family Relations
| Relation | Name | Notes |
|----------|------|-------|
| Father | | |
| Mother | | |
| Spouse(s) | | |
| Children | | |
| Siblings | | |
| Notable Relatives | | |

---

### 5. Biography/Chronology

**Format:** Chronological narrative  
**Structure:**
```
### Early Life / Rise
[Formative years, background]

### Primary Career / Reign
[Major period of activity]

### [Specific Phase]
[Thematic breakdown if needed]

### Death & Succession
[Final years, death circumstances, successor]
```

**Rules:**
- Use headings for major phases
- Include dates where known
- Focus on verified actions, not speculation

---

### 6. Political & Religious Role

**Include if applicable:**
- **Primary office:** Ruler, general, scholar, religious leader, etc.
- **Faction/Allegiance:** Primary political entity
- **Ideology:** Religious school, political philosophy
- **Controversies:** Disputed claims, heresies, political conflicts

---

### 7. Legacy & Significance

**Subsections:**
- **Historical Impact:** Lasting effects on Morocco/region
- **Modern Assessment:** How viewed today
- **Cultural Memory:** Folklore, popular perception

---

### 8. Game-Specific Information *(if applicable)*

**Sections:**
- **Role in Story:** Character's narrative function
- **Archetype:** RPG role (e.g., "The Pragmatic Founder")
- **Primary Location(s):** Where they appear in game
- **Associated Quests:** Key storylines
- **Abilities/Skills:** Combat, diplomacy, magic, etc.

---

### 9. Further Reading

**Format:**
```
- See Also: [[Link to related characters]], [[Link to factions]], [[Link to locations]]
- Historical Sources: [Primary Arabic/Non-Arabic sources]
- Academic References: [Modern scholarship]
```

---

## Optional Sections

Include these after required sections as needed:

### Appearance & Physical Description
- Based on contemporary descriptions or reasonable reconstruction
- Note if purely speculative

### Personality & Character
- Contemporary assessments
- Anecdotes illustrating traits

### Controversies & Debates
- Modern historiographical disputes
- Alternative interpretations

### Quotes
- Attributed sayings (with source citations)

### Symbolism & Iconography
- Heraldic symbols
- Religious significance
- Cultural representations

---

## Formatting Rules

### Markdown Standards
- **Headers:** `#` for title, `##` for sections, `###` for subsections
- **Tables:** Use for structured data (dates, family, stats)
- **Lists:** Use `-` for unordered, `1.` for ordered
- **Bold:** Use `**text**` for emphasis on key terms only
- **Italics:** Use `*text*` for titles of works, languages, or foreign terms
- **Links:** Use `[[Wiki/Path/To/Page|Display Text]]` for internal links

### Citation Style
- **In-text:** (Author, Year) or (Source, Date if medieval)
- **Footnotes:** Use markdown footnote syntax `[^1]`
- **Sources section:** Explicitly list primary/medieval sources used

### Language Usage
- **Default:** English (American or British, be consistent)
- **Arabic terms:** Italicize, provide transliteration with macrons (ā, ī, ū)
- **Tamazight terms:** Italicize, note language/variant
- **Place names:** Use modern names with historical variants in parentheses on first use

---

## Canon vs. Speculation

### Marking Uncertainty

| Marker | Meaning | Use For |
|--------|---------|---------|
| *(exact date)* | Historically attested | Confirmed facts |
| *(c. 750)* | Approximate | Inferred or scholarly consensus |
| *(tradition claims)* | From oral/narrative sources | Folklore, legendary material |
| *(unconfirmed)* | Suspected but unproven | Reasonable speculation |
| *(lore)* | Game-only addition | Fictional expansion for narrative |

**Never include:**
- ❌ "Possibly..." or "maybe..." without marking as speculation
- ❌ Contradictory views in Wiki (resolve in Lore, record decision here)
- ❌ "[Player decides]" or "[up to writer]"

---

## Workflow: Lore → Wiki

### Process

1. **Research Phase (Lore folder)**
   - Collect all sources
   - Note contradictions
   - Propose options
   - Document uncertainty

2. **Review Phase**
   - Phaylali reviews options
   - Decisions made on contradictions
   - Gaps filled with agreed assumptions

3. **Canonization Phase (Wiki folder)**
   - Write final profile following this schema
   - Remove all speculation markers
   - Record decisions made
   - Link to Lore source file for full research

4. **Validation**
   - Check all required sections present
   - Verify front matter complete
   - Ensure no "Options" remain
   - Test internal links

---

## Example Structure

```markdown
---
name: "Tarif al-Matghari"
alternate_names:
  - "طريف المطغري"
  - "Barbati (legendary nickname)"
title: "Founder of the Barghawata Confederacy"
dynasty: "Barghawata"
faction: "Barghawata Confederacy"
type: "Historical Figure"
status: "Canon"
last_updated: "2026-03-04"
---

# Tarif al-Matghari

## Overview
Tarif al-Matghari (d. c. 744 CE) was a Masmuda Berber chieftain who founded the Barghawata tribal confederation in the Tamesna region of Atlantic Morocco. Following participation in the Great Berber Revolt against Umayyad authority, he established an autonomous political entity that endured for over three centuries until the Almoravid conquest.

## Dates & Vital Statistics
| Event | Date | Notes |
|-------|------|-------|
| Birth | c. 700 CE | Estimated; indigenous to Tamesna region |
| Died | c. 744 CE | Circumstances unrecorded |
| Reign | 744 CE | Brief; immediate succession by son Salih |

## Origins & Lineage

### Birth & Early Life
Tarif was born into the **Matghara** subtribe of the Masmuda confederation, indigenous to the Atlantic coastal plains of Morocco. The claim that the Barghawata name derived from "Barbati" (Barbate, Spain) is a later legend; his lineage traces to the **Baquates** people attested in Roman-era sources near Volubilis.

### Family Relations
| Relation | Name | Notes |
|----------|------|-------|
| Son | Salih ibn Tarif | Succeeded as prophet-king |

## Biography

### Early Years & Tribal Affiliation
[Content...]

### The Great Berber Revolt (740–743)
[Content...]

### Founding the Confederacy (744)
[Content...]

### Death & Succession
Tarif died c. 744, with leadership passing directly to his son Salih, establishing the hereditary Barghawata dynasty.

## Political & Religious Role
- **Position:** Tribal confederate leader, founding emir
- **Innovation:** Established political autonomy distinct from Umayyad and later caliphal authority
- **Religious Alignment:** Initially associated with Sufri Kharijite movement; later pragmatic tolerance

## Game-Specific Information

### Role in Story
Tarif appears in flashback/narrative sequences establishing the Barghawata state's founding principles.

### Associated Quests
- "The Twenty-Nine Tribes" — Diplomatic unification challenge
- "Withdrawal from Revolt" — Strategic decision narrative

## Further Reading
- See Also: [[Wiki/Characters/Salih_ibn_Tarif]], [[Wiki/Tribes/Masmuda]], [[Wiki/Locations/Tamesna]]
- Lore Source: `Lore/Characters/Tarif_al-Matghari.md` (contradictions resolved per 2026-03-04: indigenous origin confirmed)
```

---

## Schema Version

**Version:** 1.0  
**Effective Date:** 2026-03-04  
**Maintainer:** OmniversifyBot  
**Review Cycle:** As needed for new character types

---

*This schema ensures consistency across all character profiles in the Deserted Tales lore database.*