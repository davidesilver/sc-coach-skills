# sc-coach-skills

Il coaching Strength & Conditioning a livello elite è riservato a chi ha accesso a un programma pro o college. Questo repo lo rende open source: **16 Claude Agent Skill** che coprono l'intero ciclo di un coach S&C — intake, screening clinico, periodizzazione, programmazione settimanale, dominio sport-specifico, bioenergetica/recupero — per qualunque profilo atleta: powerlifting, weightlifting olimpico, football americano/running back, atleti ibridi/HYROX, popolazione generale.

**Nessun dato personale di atleti reali è incluso.** Solo framework metodologici verificati, generici, riutilizzabili.

## Quickstart

```bash
npx skills add davidesilver/sc-coach-skills
```

Poi, in qualunque conversazione con il tuo agente (Claude Code, Amp, ecc.):

```
usa coach-builder-router per costruire il mio coach S&C
```

`coach-builder-router` fa una domanda di profilazione e assembla automaticamente lo stack di skill corretto per il tuo caso.

## Come funziona

```
coach-builder-router (entry point, profila l'atleta)
        │
        ▼
athlete-profiling-benchmarking + biomechanics-movement-screen   (assessment: mai programmare senza dati)
        │
        ▼
periodization-block-planner + programming-audit-council          (governance: macrociclo + audit settimanale a 3 giudici)
        │
        ▼
skill di dominio sport-specifico                                  (powerlifting / weightlifting / football-RB / HYROX / general population)
        │
        ▼
energy-systems-recovery + clinical-prehab-system + vbt-rfd-open-sets   (livelli trasversali: recupero, filtro clinico, autoregolazione)
```

Ogni skill dichiara nel proprio `SKILL.md` quando attivarsi e con quali altre skill collabora — non serve orchestrarle a mano.

## Filosofia

Principi non negoziabili applicati in tutto il pacchetto:

- **Mai prescrivere carico senza intake.** `athlete-profiling-benchmarking` è un prerequisito operativo, non un opzionale: niente v1 di programmazione senza i 4 output richiesti (readiness, massimali, flag clinici, obiettivo).
- **Il dolore ha sempre veto.** Il filtro clinico (Sanford Soreness Rules, Copenhagen protocol) in `clinical-prehab-system` interrompe la progressione indipendentemente dall'entusiasmo dell'atleta o dal calendario.
- **Autoregolazione, non tabelle rigide.** RPE/RIR/VBT (`vbt-rfd-open-sets`) governano il carico reale; la programmazione si adatta ai marker di recupero, non al foglio Excel.
- **Governance esplicita.** `programming-audit-council` audita ogni settimana attraverso 3 giudici interni (Strength Science, Sport-Specific, Clinical/Prehab) prima di emettere la v2 — nessuna settimana viene generata e usata senza revisione.

## Struttura del pacchetto

Le skill vivono in `skills/<nome>/SKILL.md` (layout flat, compatibile con la discovery di [skills.sh](https://www.skills.sh/) e con Claude Code / Amp).

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

Coperti con fonti verificate: football/RB, COD/footwork, tendine/RFD, VBT/open sets, clinica/prehab (Sanford, Copenhagen), HYROX/ibridi (soglie fisiologiche, zone HR, protocollo Brick, cue tecnici delle 8 stazioni, benchmark Open/Pro), bioenergetica/recupero (sistemi energetici, protocolli RSA, creatina, recovery elite stack), profiling/assessment (intervista NFL-style, batteria test ordinata, profiling neuromuscolare, regola atleta decondizionato), movement screening (FMS 6-pattern), periodizzazione macrociclo (Block/Lineare/DUP/Coniugato), powerlifting (RTS block model, peaking, tapering), weightlifting olimpico (fasi tecniche, correzione early arm bend), popolazione generale (NSCA movement patterns).

Non coperti in questa versione, perché mancano fonti verificate sufficienti al momento della ricerca: throwing sports specifici (lancio del peso, giavellotto), youth/adolescent athletic development, endurance puro (maratona/triathlon non ibrido), sport di combattimento. Proposte benvenute — vedi [CONTRIBUTING.md](CONTRIBUTING.md).

## Strumenti complementari

- `notion/` — template di database Notion importabile per tracciare atleti, settimane di programmazione e feedback sheet.
- `data/` — schema SQL compatibile MotherDuck/DuckDB per analisi quantitativa dei log di allenamento nel tempo.
- `scripts/validate-skills.sh` — valida frontmatter e riferimenti incrociati tra skill prima di ogni commit/PR (eseguito anche in CI).

## Fonti

Framework derivati da report tecnici su tendon resilience, football/RB, footwork, MTSS/Sanford, Copenhagen protocol, VBT/Squillante-Bosco, HYROX, integrati con fonti esterne verificate su powerlifting peaking (RTS/Emerging Strategies, JTS, tapering research), weightlifting tecnico (Catalyst Athletics, TrainHeroic), popolazione generale (NSCA), movement screening (functionalmovement.com, Indiana State University Scholars) e periodizzazione a blocchi (TrainingPeaks, Thibarmy, phase.fitness).

## Licenza

MIT — vedi [LICENSE](LICENSE).

## Compatibilità

Ogni `SKILL.md` include header YAML compatibile con Amp (`.agents/skills`, `~/.config/agents/skills`) e Claude Code (`~/.claude/skills`, o come plugin via `.claude-plugin/plugin.json`). Il layout `skills/<nome>/SKILL.md` segue lo standard di discovery di [skills.sh](https://www.skills.sh/) (CLI `vercel-labs/skills`), che richiede le skill dentro una cartella `skills/` (flat o a catalogo) e non direttamente nella root del repo.
