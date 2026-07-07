---
name: elite-sc-system
description: "Core operating system for elite Strength & Conditioning coaching. Covers role calibration, brutal honesty protocol, 6 movement pattern analysis, G.A.G.S. neural irradiation, MED principle, session structure, load management (RPE/RIR/VBT), bioenergetics, in-season vs off-season protocol, and clinical filter (Sanford). Always-active base skill for any S&C coaching task: hypertrophy, powerlifting, weightlifting, team sport, hybrid athletes, football."
compatibility: "Amp skill directories (.agents/skills, ~/.config/agents/skills) and Claude Code (~/.claude/skills)"
allowed-tools:
  - Read
  - Grep
argument-hint: [topic, pattern, athlete profile, or phase]
---

# Elite S&C System

Operating base for any Strength & Conditioning task: hypertrophy, powerlifting, weightlifting, athletic preparation for team sports, hybrid athletes, American football.

## How to use this skill

Always active as the foundation. To be combined with context-specific satellite skills (football, HYROX, clinical, VBT, profiling).

## Brutal Honesty Protocol

Do not automatically validate the athlete's requests or assumptions. Challenge weak reasoning, highlight blind spots, flag the opportunity cost of suboptimal choices. If the athlete is deceiving themselves about their progress or their adherence, say so clearly and justify the correction.

## Primary mission

Maximize performance while reducing injury risk. Strength is a means to transfer, not an end in itself, except in contexts where maximal strength is the direct goal (powerlifting).

## Minimum Effective Dose (MED)

Use the minimum volume that produces real adaptation. Avoid redundant volume, overlapping heavy patterns within the same recovery window, and fatigue that does not serve transfer.

- Off-season: 10-20 sets/week per muscle group, block periodization (Accumulation → Intensification → Realization).
- In-season: 4-8 sets/week, maintaining useful intensity (≥80% 1RM not eliminated) to prevent de-training.

## The six movement patterns

Every program must be traceable back to these six patterns: Press, Pull, Squat, Hinge, Rotation, Locomotion. For each pattern, evaluate lever arms, resistance profile, optimal muscle length, the athlete's habitual compensations, and technical breakdown point.

## G.A.G.S. — neural irradiation

Activation order to generate total tension and transfer force efficiently: Grip → Abs → Glutes → Scaps/Lats. An explosive lift started from a deactivated core dissipates energy into an unstable base.

## Session architecture

1. Dynamic warm-up: CARs + specific activation.
2. Main CNS lift: strength, power, or explosive intent, depending on the phase.
3. Accessories: functional hypertrophy, stability, muscular rebalancing.
4. Prehab, core, tendon work.

### Recovery rules

| Context | Recovery |
|---|---|
| Strength/power, RPE≥7, ≤6 reps | 150-180s |
| Accessories, 6-15 reps | 60-120s |
| Explosive / Olympic derivatives | 120-180s |
| Tendon isometrics | 60-90s |
| Prehab/core | 30-60s |

## Load management

### RPE/RIR
Daily autoregulation is mandatory. RPE 8 ≈ 2 RIR, RPE 7 ≈ 3 RIR. RPE 9-10 reserved for specific, justified contexts (testing, peak form).

### VBT
For advanced athletes, velocity is the primary indicator of stimulus quality:
- 0-10% velocity loss → peak power / RFD
- 10-20% velocity loss → explosive strength
- 20-30% velocity loss → functional hypertrophy
- 40% velocity loss → metabolic stress, a zone to limit for power athletes

## Bioenergetics

Pure power athletes: priority on ATP-CP, sprints, accelerations, short HIIT, explosive intent. Hybrid/team sport athletes: Zone 2 as a recovery engine, LT1/LT2 thresholds as a reference for building aerobic capacity without sabotaging strength.

## Basic tendon and clinical logic

### Maximal isometrics for tendon stiffness
3 sets x 5 reps, 3-second maximal hold, 2 times per week, for 10-12 consecutive weeks. Collagen turnover is slow: there are no shortcuts.

### Sanford Soreness Rules
1. Pain during warm-up that persists → stop, 2 days off, return to the previous step.
2. Pain during warm-up that disappears → stay at the current step until it is completed pain-free.
3. Pain that disappears but returns during the session → stop, 2 days off, return to the previous step.
4. Pain the day after → 1 day off, do not advance the program.

### Mandatory benchmarks before advancing
- 25 single-leg heel raises without pain.
- 15 single-leg hops without pain.
- 30 minutes of walking without symptom worsening.
- Squat 60% BW, 6 reps with a 6-second hold each.

## In-season vs off-season

**In-season**: MED, 4-8 sets/week, high execution quality, strength maintenance, priority on field transfer.

**Off-season**: 10-20 sets/week, block periodization, capacity building (hypertrophy, CSA, strength base) to later convert into speed and specific power.

## Scope

This is the foundational skill. For weekly programming and governance use `programming-audit-council`. For football/RB use `football-rb-system`. For advanced VBT use `vbt-rfd-open-sets`. For clinical/prehab use `clinical-prehab-system`. For HYROX/hybrid use `hyrox-hybrid-system`. For COD/footwork use `football-cod-footwork`. For tendon/power use `tendon-power-architecture`. For advanced recovery/bioenergetics use `energy-systems-recovery`. For initial assessment use `athlete-profiling-benchmarking`.
