# Data Layer — MotherDuck / DuckDB

Questo schema permette di tracciare in modo quantitativo l'output delle skill `programming-audit-council` e `athlete-profiling-benchmarking` nel tempo, per più atleti.

## Setup rapido

### Locale (DuckDB CLI)
```bash
duckdb sc_coach.duckdb < schema.sql
```

### Cloud (MotherDuck)
1. Crea un account su https://motherduck.com
2. Connetti tramite CLI: `duckdb md:my_db`
3. Esegui: `.read schema.sql`

## Tabelle

- `athletes` — anagrafica atleta (usa iniziali/codename se il repo è pubblico, mai nomi completi)
- `weekly_programs` — metadati di ogni settimana generata da `programming-audit-council`
- `exercises_log` — riga per riga il contenuto del CSV settimanale (EXE|EXERCISE|SETS|REPS|...)
- `feedback_sheet` — dati soggettivi/oggettivi post-sessione (sonno, fatica, dolore, readiness)

## Viste incluse

- `sanford_flags` — righe con pain_check >= 3, da rivedere secondo le Sanford Soreness Rules
- `progression_readiness` — flag automatico ADVANCE_ELIGIBLE / HOLD_OR_SCALE basato sulla regola di progressione a 3 criteri di `programming-audit-council`

## Nota privacy

Se il repository è pubblico, non caricare mai file `.duckdb` popolati con dati reali di atleti. Usa questo schema solo come struttura, mantenendo i dati effettivi in un database privato o locale.
