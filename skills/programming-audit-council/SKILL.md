---
name: programming-audit-council
description: "Governance skill for weekly S&C programming. Generates week v1, audits it through a 3-judge internal council (Strength Science, Sport-Specific, Clinical/Prehab), then emits corrected v2 with Sanford gates and a mandatory feedback sheet. Use for weekly planning, microcycles, mesocycles, macrocycles, and progression decisions."
compatibility: "Amp (.agents/skills, ~/.config/agents/skills) and Claude Code (~/.claude/skills)"
allowed-tools:
  - Read
  - Grep
argument-hint: [week, athlete profile, sport, phase, previous week feedback]
---

# Programming Audit Council

## Missione

Nessuna settimana di allenamento viene emessa senza audit. Il processo obbligatorio è: genera v1 → audit del Council → emetti v2 → allega feedback sheet.

## Formato output

Ogni settimana va prodotta in formato CSV con questo template di colonne:

`EXE | EXERCISE | SETS | REPS | INTENSITY (%/RPE) | VELOCITY (m/s) | TEMPO | REST | NOTES/ACTUALS`

Naming file con focus esplicito, esempio: `W1_D3_LowerPower_Posterior.csv`.

## Regole TEMPO (fonte di errori frequenti)

| Tipo esercizio | Formato TEMPO | Esempio |
|---|---|---|
| Bilaterale pesante (squat, panca, stacco, row) | E-PB-C-PA (secondi) | 3-1-X-0 |
| Tirata/pull (row, curl, trazioni) | Eccentrica lenta 2-3s, concentrica sempre X | 3-0-X-1 |
| Isometrico | Nessun TEMPO — durata solo nel campo REPS | REPS: 20s |
| Esplosivo/balistico (jump, sprint, clean) | Nessun TEMPO codificabile | "—" o BALIST |
| Locomotore (farmer walk, skip, sled) | Nessun TEMPO | WALK |

Errori tipici da evitare: pausa eccentrica su lift concentrici veloci (RDL, trap bar), tempo fisso su isometrici che hanno già durata in REPS, TEMPO identico su esercizi biomeccanicamente diversi (es. hip thrust vs squat).

## Struttura del Council

### JUDGE_1 — Strength Science
Verifica: ridondanze di pattern pesante nella stessa finestra di 48h, rapporto anterior/posterior, coerenza dei recuperi, focus chiaro per giornata, progressione intra-mesociclo logica.

### JUDGE_2 — Sport-Specific
Verifica: almeno un giorno power/intent esplosivo, presenza di un field day specifico (meccanica, accelerazione, COD, decelerazione), upper body con elemento di transfer, assenza di settimane "da palestra" senza transfer di campo.

### JUDGE_3 — Clinical/Prehab
Verifica: Sanford gate esplicito prima dei main lift e del field day, prehab presente ma non ridondante, presenza di una vera giornata di recupero (CARs, respirazione, mobilità, downregulation), assenza di doppioni Copenhagen/tibialis/soleo nello stesso microciclo.

## Workflow obbligatorio

1. **Genera v1** — completa ma non ancora perfetta, deve essere auditabile.
2. **Council audit** — ogni giudice produce 3-5 errori principali, correzione proposta, struttura target.
3. **Emetti v2** — con correzioni applicate, focus esplicito nel nome file, Sanford gate (⚑) in testa ai giorni rilevanti.

## Sanford Gate

Ogni giorno rilevante deve aprirsi con `⚑ SANFORD CHECK` prima di: field day, sprint day, lower heavy, return-to-run progressions, atleti con dolore o storico recente.

## Feedback sheet

Ogni settimana produce `W*_FEEDBACK_SHEET.csv` con campi minimi: bodyweight AM, sonno, fatigue pre, soreness, pain check, field readiness, carichi principali sui main lift, note coach.

## Continuità tra settimane

La settimana successiva è sempre funzione di: settimana precedente (v2) + feedback reale. Non si riparte mai da zero. Prima di generare la settimana N+1:
1. Leggi v2 della settimana N.
2. Leggi il feedback sheet della settimana N.
3. Identifica adattamento, fatica residua, gap di transfer.
4. Modifica una sola variabile chiave per volta quando possibile (o poche, se i dati lo giustificano chiaramente).

## Regola di progressione

Progressione aggressiva solo se tutti questi criteri sono soddisfatti:
1. RPE reale ≤ RPE target +0.5 su almeno 3 set principali.
2. Nessun pain check ≥3/10.
3. Sonno medio ≥7h.

Se anche un solo criterio manca: mantieni o scala, mai avanzare per calendario.

## Aggiustamenti guidati dai dati (weekly continuity check)

- Sonno <7h per ≥3 giorni → -10/15% volume.
- Fatigue ≥7/10 per ≥2 giorni → elimina il giorno opzionale.
- Pain ≥3/10 → attiva Sanford Gate.
- Dolore stinco dopo tibialis → mantieni volume, non progredire.
- DOMS >48h dopo Nordic → stesso volume, non progredire.
- RPE sprint >target+1 per ≥2 sessioni → riduci target RPE di 0.5.
- Atterraggio instabile su jump → non aumentare volume.
- Dolore inguinale dopo Copenhagen → 48h di gap obbligatorio prima del prossimo stimolo aduttorio.

## Scope

Questa skill governa la programmazione. Per la logica biomeccanica di base usa `elite-sc-system`. Per specificità football/RB usa `football-rb-system`. Per VBT avanzato usa `vbt-rfd-open-sets`. Per clinica/return-to-run usa `clinical-prehab-system`. Per HYROX/ibridi usa `hyrox-hybrid-system`.
