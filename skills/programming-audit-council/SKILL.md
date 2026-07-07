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

## Mission

No training week is issued without an audit. The mandatory process is: generate v1 → Council audit → issue v2 → attach feedback sheet.

## Output format

Each week must be produced in CSV format with this column template:

`EXE | EXERCISE | VIDEO_LINK | SETS | REPS | INTENSITY (%/RPE) | VELOCITY (m/s) | TEMPO | REST | NOTES/ACTUALS`

Populate `EXERCISE` and `VIDEO_LINK` using `exercise-library-video` — canonical name required, link only when it verifiably shows that exact movement, otherwise leave `VIDEO_LINK` blank.

File naming with explicit focus, example: `W1_D3_LowerPower_Posterior.csv`.

## TEMPO rules (frequent source of errors)

| Exercise type | TEMPO format | Example |
|---|---|---|
| Heavy bilateral (squat, bench, deadlift, row) | E-PB-C-PA (seconds) | 3-1-X-0 |
| Pull (row, curl, pull-ups) | Slow eccentric 2-3s, concentric always X | 3-0-X-1 |
| Isometric | No TEMPO — duration only in the REPS field | REPS: 20s |
| Explosive/ballistic (jump, sprint, clean) | No codifiable TEMPO | "—" or BALIST |
| Locomotor (farmer walk, skip, sled) | No TEMPO | WALK |

Typical errors to avoid: eccentric pause on fast concentric lifts (RDL, trap bar), fixed tempo on isometrics that already have duration in REPS, identical TEMPO on biomechanically different exercises (e.g. hip thrust vs squat).

## Council structure

### JUDGE_1 — Strength Science
Checks: heavy pattern redundancies within the same 48h window, anterior/posterior ratio, recovery consistency, clear daily focus, logical intra-mesocycle progression.

### JUDGE_2 — Sport-Specific
Checks: at least one power/explosive intent day, presence of a specific field day (mechanics, acceleration, COD, deceleration), upper body with a transfer element, absence of "gym-only" weeks with no field transfer.

### JUDGE_3 — Clinical/Prehab
Checks: explicit Sanford gate before main lifts and field day, prehab present but not redundant, presence of a genuine recovery day (CARs, breathing, mobility, downregulation), absence of duplicate Copenhagen/tibialis/soleus work in the same microcycle.

## Mandatory workflow

1. **Generate v1** — complete but not yet perfect, must be auditable.
2. **Council audit** — each judge produces 3-5 main errors, proposed correction, target structure.
3. **Issue v2** — with corrections applied, explicit focus in the file name, Sanford gate (⚑) at the top of relevant days.

## Sanford Gate

Every relevant day must open with `⚑ SANFORD CHECK` before: field day, sprint day, lower heavy, return-to-run progressions, athletes with pain or recent history.

## Feedback sheet

Each week produces a `W*_FEEDBACK_SHEET.csv` with minimum fields: AM bodyweight, sleep, pre-session fatigue, soreness, pain check, field readiness, main lift loads, coach notes.

## Continuity between weeks

The following week is always a function of: previous week (v2) + real feedback. Never start from scratch. Before generating week N+1:
1. Read week N's v2.
2. Read week N's feedback sheet.
3. Identify adaptation, residual fatigue, transfer gaps.
4. Change only one key variable at a time when possible (or a few, if the data clearly justifies it).

## Progression rule

Aggressive progression only if all of these criteria are met:
1. Actual RPE ≤ target RPE +0.5 on at least 3 main sets.
2. No pain check ≥3/10.
3. Average sleep ≥7h.

If even one criterion is missing: maintain or scale back, never advance on a calendar basis.

## Data-driven adjustments (weekly continuity check)

- Sleep <7h for ≥3 days → -10/15% volume.
- Fatigue ≥7/10 for ≥2 days → eliminate the optional day.
- Pain ≥3/10 → activate the Sanford Gate.
- Shin pain after tibialis → maintain volume, do not progress.
- DOMS >48h after Nordic → same volume, do not progress.
- Sprint RPE >target+1 for ≥2 sessions → reduce target RPE by 0.5.
- Unstable landing on jumps → do not increase volume.
- Groin pain after Copenhagen → mandatory 48h gap before the next adductor stimulus.

## Scope

This skill governs programming. For the underlying biomechanical logic use `elite-sc-system`. For football/RB specifics use `football-rb-system`. For advanced VBT use `vbt-rfd-open-sets`. For clinical/return-to-run use `clinical-prehab-system`. For HYROX/hybrid use `hyrox-hybrid-system`.
