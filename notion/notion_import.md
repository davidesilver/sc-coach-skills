# Notion Import — S&C Coach Workspace

Questo file è un template importabile in Notion (File > Import > Markdown) per creare un workspace di coaching strutturato attorno al repository di skill.

## Come importare
1. In Notion: crea una nuova pagina vuota.
2. Menu "..." in alto a destra → Import → Markdown & CSV.
3. Seleziona questo file (`notion_import.md`).
4. Notion ricreerà automaticamente le sezioni come sottopagine/blocchi.

---

# 🏋️ S&C Coach Workspace

## 📌 Come iniziare
Leggi prima `coach-builder-router` nel repository GitHub collegato. Identifica il tuo profilo (powerlifter, weightlifter, football/RB, HYROX, general population) e segui lo stack di skill consigliato nel README.

## 🗂️ Database Atleti
Crea qui un database Notion con queste proprietà (replica la tabella `athletes` dello schema DuckDB):
- Nome/Codename (Title)
- Profilo (Select: Powerlifter, Weightlifter, Football/RB, Hybrid/HYROX, General Population)
- Data Onboarding (Date)
- Note (Text)
- Link Repo Skill (URL)

## 📅 Database Programmazione Settimanale
Proprietà consigliate (replica `weekly_programs` + `exercises_log`):
- Settimana (Number)
- Fase (Select: Accumulation, Intensification, Realization, Peaking, Taper, In-Season, Off-Season)
- Versione (Select: v1, v2)
- Focus (Text)
- File CSV allegato (Files & Media)
- Stato Audit Council (Select: Da Auditare, Auditato, Emesso v2)

## 📝 Database Feedback Sheet
Proprietà consigliate (replica `feedback_sheet`):
- Data (Date)
- Atleta (Relation → Database Atleti)
- Bodyweight AM (Number)
- Ore Sonno (Number)
- Fatigue Pre (Number, 0-10)
- Soreness (Number, 0-10)
- Pain Check (Number, 0-10)
- Field Readiness (Number, 0-10)
- ⚑ Sanford Flag (Formula: `if(prop("Pain Check") >= 3, "🚩 REVIEW", "✅ OK")`)

## 🔗 Collegamento con GitHub
Aggiungi un blocco "Embed" o link diretto al repository GitHub pubblico contenente le skill, per mantenere Notion come layer di gestione operativa/dati e GitHub come layer di versioning delle skill.

## 🔗 Collegamento con MotherDuck
Per analisi quantitative avanzate su più atleti nel tempo, esporta periodicamente i database Notion in CSV e caricali nello schema DuckDB/MotherDuck fornito in `data/schema.sql`, oppure usa Notion API + script di sync se preferisci l'automazione.
