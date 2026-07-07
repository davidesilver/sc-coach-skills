# Notion Import — S&C Coach Workspace

This file is a template you can import into Notion (File > Import > Markdown) to build a coaching workspace structured around the skill repository.

## How to import
1. In Notion: create a new empty page.
2. Top-right "..." menu → Import → Markdown & CSV.
3. Select this file (`notion_import.md`).
4. Notion will automatically recreate the sections as sub-pages/blocks.

---

# 🏋️ S&C Coach Workspace

## 📌 Getting started
Read `coach-builder-router` in the linked GitHub repository first. Identify your profile (powerlifter, weightlifter, football/RB, HYROX, general population) and follow the recommended skill stack in the README.

## 🗂️ Athletes database
Create a Notion database here with these properties (mirrors the `athletes` table in the DuckDB schema):
- Name/Codename (Title)
- Profile (Select: Powerlifter, Weightlifter, Football/RB, Hybrid/HYROX, General Population)
- Onboarding Date (Date)
- Notes (Text)
- Skill Repo Link (URL)

## 📅 Weekly Programming database
Recommended properties (mirrors `weekly_programs` + `exercises_log`):
- Week (Number)
- Phase (Select: Accumulation, Intensification, Realization, Peaking, Taper, In-Season, Off-Season)
- Version (Select: v1, v2)
- Focus (Text)
- Attached CSV File (Files & Media)
- Audit Council Status (Select: To Audit, Audited, v2 Issued)

## 📝 Feedback Sheet database
Recommended properties (mirrors `feedback_sheet`):
- Date (Date)
- Athlete (Relation → Athletes database)
- Bodyweight AM (Number)
- Sleep Hours (Number)
- Fatigue Pre (Number, 0-10)
- Soreness (Number, 0-10)
- Pain Check (Number, 0-10)
- Field Readiness (Number, 0-10)
- ⚑ Sanford Flag (Formula: `if(prop("Pain Check") >= 3, "🚩 REVIEW", "✅ OK")`)

## 🔗 Linking to GitHub
Add an "Embed" block or a direct link to the public GitHub repository containing the skills, so Notion stays the operational/data management layer and GitHub stays the versioning layer for the skills.

## 🔗 Linking to MotherDuck
For advanced quantitative analysis across multiple athletes over time, periodically export the Notion databases to CSV and load them into the DuckDB/MotherDuck schema provided in `data/schema.sql`, or use the Notion API + a sync script if you prefer automation.
