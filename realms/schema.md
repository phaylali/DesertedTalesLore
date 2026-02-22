# Realm Schema

This document outlines the file structure and schema for each realm within the `realms` directory.

## Directory Structure

Each realm has its own directory, and within it, the following structure should be followed:

```
/realm_name
|-- index.md
|-- territory.md
|-- military.md
|-- /rulers
|   |-- 01_ruler_name.md
|   |-- 02_ruler_name.md
|   |-- ...
|-- /assets
|   |-- flag.png
```

## `index.md`

The main file for the realm.

```yaml
---
name: "Name of the Realm"
flag: "./assets/flag.png"
alliances:
  - "Name of allied realm/tribe"
enemies:
  - "Name of enemy realm/tribe"
---

# [Name of the Realm]

## Summary

A brief overview of the realm.

## Rulers

A list of rulers in chronological order, with links to their individual files in the `rulers/` directory.

## Territory

A summary of the realm's territory, with a link to `territory.md` for more details.

## Military

A summary of the realm's military, with a link to `military.md` for more details.
```

## `rulers/ruler_name.md`

A file for each ruler.

```yaml
---
name: "Ruler's Name"
reign: "start_year-end_year"
---

# [Ruler's Name]

## Reign

A summary of the ruler's reign.

## Events

A chronological list of significant events during the ruler's reign.

### [Year] - [Event Title]
*   **Type**: War / Battle / Diplomacy / Famine / etc.
*   **Description**: Details of the event.
*   **Outcome**: Result of the event.
```

## `territory.md`

Describes the realm's lands and their changes over time.

```markdown
# Territory of [Name of the Realm]

This document tracks the chronological changes in the realm's territory.

## [Year Range]

*   **Cities Controlled**: List of cities.
*   **Territorial Changes**: Description of lands gained or lost.

## [Year Range]

*   **Cities Controlled**: List of cities.
*   **Territorial Changes**: Description of lands gained or lost.
```

## `military.md`

Describes the realm's military.

```markdown
# Military of [Name of the Realm]

## Military Power at Height

A description of the realm's military strength at its peak, including estimated numbers, composition (cavalry, infantry, etc.), and overall strategy.

## Uniform and Equipment

Details about the typical uniform, armor, and equipment of the soldiers.

## Weapons

A list of common weapons used by the military, with a focus on any specific "weapon of choice" that might be characteristic of the realm's warriors.
```
