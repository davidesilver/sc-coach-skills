# Elite Strength & Conditioning — Skill Package

Pacchetto completo di 16 skill modulari per costruire un "coach S&C personale" per qualunque profilo atleta: powerlifting, weightlifting olimpico, football americano/running back, atleti ibridi/HYROX, popolazione generale.

Le skill vivono in `skills/<nome>/SKILL.md` (layout flat, compatibile con la discovery di [skills.sh](https://www.skills.sh/) e con Claude Code / Amp).

**Nessun dato personale di atleti reali è incluso.** Solo framework metodologici verificati, generici, riutilizzabili.

## Come iniziare (per qualunque atleta)

Carica sempre per prima la skill `coach-builder-router`: pone una domanda di profilazione e assembla automaticamente lo stack di skill corretto per il tuo caso (powerlifter, weightlifter, football/RB, HYROX, general population, o preparatore multi-atleta).

## Struttura del pacchetto

| # | Skill | Livello | Profilo target |
|---|---|---|---|
| 0 | `coach-builder-router` | **Entry point** | Tutti — instrada al profilo corretto |
| 1 | `elite-sc-system` | Base sempre attiva | Tutti |
| 2 | `programming-audit-council` | Governance | Tutti |
| 3 | `athlete-profiling-benchmarking` | Assessment | Tutti |
| 4 | `powerlifting-peaking-system` | Dominio sport-specifico | Powerlifter |
| 5 | `olympic-weightlifting-technique` | Dominio tecnico | Weightlifter olimpico |
| 6 | `football-rb-system` | Dominio sport-specifico | Football / RB |
| 7 | `football-cod-footwork` | Dominio tecnico | Football / RB |
| 8 | `tendon-power-architecture` | Dominio biomeccanico | Power/speed atleti |
| 9 | `vbt-rfd-open-sets` | Dominio metodologico | Atleti avanzati (tutti i profili) |
| 10 | `clinical-prehab-system` | Dominio clinico | Football, power athlete |
| 11 | `energy-systems-recovery` | Dominio fisiologico | Football, HYROX |
| 12 | `hyrox-hybrid-system` | Dominio sport-specifico | Atleti ibridi / HYROX |
| 13 | `general-population-fitness` | Dominio popolazione generale | Non-atleti / fitness |
| 14 | `periodization-block-planner` | Governance macrociclo | Tutti (scelta modello: Block/Lineare/DUP/Coniugato) |
| 15 | `biomechanics-movement-screen` | Dominio clinico/assessment | Tutti (screening 6 pattern FMS) |

## Stack raccomandati per profilo

**Powerlifter**: `coach-builder-router` → `elite-sc-system` → `athlete-profiling-benchmarking` → `biomechanics-movement-screen` → `periodization-block-planner` → `programming-audit-council` → `powerlifting-peaking-system` → `vbt-rfd-open-sets` → `tendon-power-architecture`

**Weightlifter olimpico**: `coach-builder-router` → `elite-sc-system` → `athlete-profiling-benchmarking` → `periodization-block-planner` → `programming-audit-council` → `olympic-weightlifting-technique` → `vbt-rfd-open-sets` → `tendon-power-architecture`

**Football/RB**: `coach-builder-router` → `elite-sc-system` → `athlete-profiling-benchmarking` → `biomechanics-movement-screen` → `periodization-block-planner` → `programming-audit-council` → `football-rb-system` → `football-cod-footwork` → `tendon-power-architecture` → `clinical-prehab-system` → `vbt-rfd-open-sets`

**Atleta ibrido/HYROX**: `coach-builder-router` → `elite-sc-system` → `athlete-profiling-benchmarking` → `periodization-block-planner` → `programming-audit-council` → `hyrox-hybrid-system` → `energy-systems-recovery` → `vbt-rfd-open-sets`

**Popolazione generale**: `coach-builder-router` → `elite-sc-system` (semplificato) → `biomechanics-movement-screen` → `general-population-fitness`

## Coverage e limiti dichiarati

Coperti con fonti verificate: football/RB, COD/footwork, tendine/RFD, VBT/open sets, clinica/prehab (Sanford, Copenhagen), HYROX/ibridi, bioenergetica/recupero, profiling/assessment, movement screening (FMS 6-pattern), periodizzazione macrociclo (Block/Lineare/DUP/Coniugato), powerlifting (RTS block model, peaking, tapering), weightlifting olimpico (fasi tecniche, correzione early arm bend), popolazione generale (NSCA movement patterns).

Non coperti in questa versione, perché mancano fonti verificate sufficienti nello Space o online al momento della ricerca: throwing sports specifici (lancio del peso, giavellotto), youth/adolescent athletic development, endurance puro (maratona/triathlon non ibrido), sport di combattimento.

## Strumenti complementari

- `notion/` — template di database Notion importabile per tracciare atleti, settimane di programmazione e feedback sheet.
- `data/` — schema SQL compatibile MotherDuck/DuckDB per analisi quantitativa dei log di allenamento nel tempo.

## Fonti

Framework derivati da: report tecnici dello Space Perplexity (tendon resilience, football/RB, footwork, MTSS/Sanford, Copenhagen protocol, VBT/Squillante-Bosco, HYROX), integrati con fonti esterne verificate su powerlifting peaking (RTS/Emerging Strategies, JTS, tapering research), weightlifting tecnico (Catalyst Athletics, TrainHeroic), popolazione generale (NSCA), movement screening (functionalmovement.com, Indiana State University Scholars) e periodizzazione a blocchi (TrainingPeaks, Thibarmy, phase.fitness).

## Licenza

MIT — vedi `LICENSE`.

## Compatibilità

Ogni `SKILL.md` include header YAML compatibile con Amp (`.agents/skills`, `~/.config/agents/skills`) e Claude Code (`~/.claude/skills`). Il layout `skills/<nome>/SKILL.md` segue lo standard di discovery di [skills.sh](https://www.skills.sh/) (CLI `vercel-labs/skills`), che richiede le skill dentro una cartella `skills/` (flat o a catalogo) e non direttamente nella root del repo.
