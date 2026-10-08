---
name: elite-sc-system
description: "Core operating system for elite Strength & Conditioning coaching. Covers role calibration, brutal honesty protocol, 6 movement pattern analysis, G.L.A.G.S. total-body tension, MED principle, session structure, load management (RPE/RIR/VBT), bioenergetics, in-season vs off-season protocol, and clinical filter (Sanford). Always-active base skill for any S&C coaching task: hypertrophy, powerlifting, weightlifting, team sport, hybrid athletes, football."
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

- Off-season: 10-20 sets/week per muscle group, block periodization (Accumulation → Intensification → Realization). Volume shows "a graded dose-response relationship" with hypertrophy [Schoenfeld 2017, doi:10.1080/02640414.2016.1210197, abstract, VERIFIED]; the 20-set ceiling is [OPINION].
- In-season: 4-8 sets/week, keeping some heavy work (≥80% 1RM) [OPINION]. In untrained adults, one-ninth of the training dose preserved hypertrophy in the young, and "strength gained during phase 1 was largely retained throughout detraining" [Bickel 2011, doi:10.1249/MSS.0b013e318207c15d, abstract, VERIFIED]. Strength is robust to reduced volume, so the in-season minimum is a coaching call.

## The six movement patterns

Every program must be traceable back to these six patterns: Press, Pull, Squat, Hinge, Rotation, Locomotion. For each pattern, evaluate lever arms, resistance profile, optimal muscle length, the athlete's habitual compensations, and technical breakdown point.

## G.L.A.G.S. — total-body tension

Activation order to generate total tension [OPINION, coaching cue]: Grip → Lats → Abs → Glutes → Scaps. Details in `tendon-power-architecture`.

## Session architecture

1. Dynamic warm-up: CARs + specific activation.
2. Main CNS lift: strength, power, or explosive intent, depending on the phase.
3. Accessories: functional hypertrophy, stability, muscular rebalancing.
4. Prehab, core, tendon work.

### Recovery rules

[OPINION, starting points.] Longer rests favour strength and hypertrophy over short ones: "longer rest periods promote greater increases in muscle strength and hypertrophy" [Schoenfeld 2016, doi:10.1519/JSC.0000000000001272, abstract, VERIFIED]. Shorten rests only to save time.

| Context | Recovery |
|---|---|
| Strength/power, RPE≥7, ≤6 reps | 150-180s |
| Accessories, 6-15 reps | 60-120s |
| Explosive / Olympic derivatives | 120-180s |
| Tendon isometrics | 60-90s |
| Prehab/core | 30-60s |

### Superset logic

Pair supersets by relationship and session type:
- **Antagonist pairs** (push/pull, quad/hamstring): useful for saving time without degrading the priority lift.
- **Non-competing patterns** (e.g., main lower lift + upper accessory): allows efficient workload without interference.
- **Never pair two heavy competing patterns** that share the same recovery demand (e.g., heavy squat + heavy deadlift). This silently cuts recovery on the main lift.
- **Rest applies AFTER the pair**, and the priority/CNS lift keeps its full prescribed rest. Supersets must not reduce the recovery time on the main lift.

## Load management

### RPE/RIR
Daily autoregulation is mandatory. RPE 8 ≈ 2 RIR, RPE 7 ≈ 3 RIR [Zourdos 2016, doi:10.1519/JSC.0000000000001049, abstract, VERIFIED: "RPE-10 = 0-RIR, RPE-9 = 1-RIR, and so forth"]. RPE 9-10 reserved for specific, justified contexts (testing, peak form).

### VBT
For athletes with a velocity device. Only one comparison is tested: 20% vs 40% velocity loss in the squat. VL20 gave similar strength gains and greater jump gains (CMJ 9.5% vs 3.5%); VL40 gave more hypertrophy and a loss of type IIX fibres [Pareja-Blanco 2017, doi:10.1111/sms.12678, abstract, VERIFIED]. Finer zones (0-10, 10-20, 20-30%) and their labels are [UNVERIFIABLE]. Details in `vbt-rfd-open-sets`.

## Bioenergetics

Pure power athletes: priority on ATP-CP, sprints, accelerations, short HIIT, explosive intent. Hybrid/team sport athletes: Zone 2 as a recovery engine, LT1/LT2 thresholds as a reference for building aerobic capacity without sabotaging strength.

## Basic tendon and clinical logic

### Isometrics for tendon adaptation
Tested protocol: 5 sets × 4 reps, 3 s loading + 3 s rest, about 90% MVC, 4×/week, 14 weeks [Arampatzis 2007, doi:10.1242/jeb.003814, full text, VERIFIED; Bohm 2015, doi:10.1186/s40798-015-0009-9, VERIFIED]. Tendon adaptation is slow: there are no shortcuts. Details in `tendon-power-architecture`.

### Sanford Soreness Rules
For pain at the site of an injury during a return program [Sanford Health MTSS guideline 2024, p.5, VERIFIED].
1. Pain during warm-up that persists → stop, 2 days off, return to the previous step.
2. Pain during warm-up that disappears → stay at the current step until it is completed pain-free.
3. Pain that disappears but returns during the session → stop, 2 days off, return to the previous step.
4. Pain the day after → 1 day off, do not advance the program.

### Mandatory benchmarks before advancing (MTSS, end of Phase II)
[Sanford 2024, p.3, VERIFIED]
- More than 25 single-leg heel raises (>25) on each leg.
- 15 single-leg hops without pain.
- 30 minutes of walking without symptom worsening.
- Squat at 60% body weight: 6 repetitions, 6 seconds.

## In-season vs off-season

**In-season**: MED, 4-8 sets/week, high execution quality, strength maintenance, priority on field transfer.

**Off-season**: 10-20 sets/week, block periodization, capacity building (hypertrophy, CSA, strength base) to later convert into speed and specific power.

## References

Evidence tags: `[Source Year, doi, grade]`, grades VERIFIED / UNVERIFIABLE / OPINION / C (internal rule). Audit 2026-10-08. Sources cited inline: Sanford Health MTSS guideline (rev. 01/2024); Zourdos 2016; Schoenfeld 2016, 2017; Bickel 2011; Pareja-Blanco 2017; Arampatzis 2007; Bohm 2015. The six-pattern taxonomy, G.L.A.G.S., session architecture and in-season volumes are coaching practice [OPINION].

## Scope

This is the foundational skill. For weekly programming and governance use `programming-audit-council`. For football/RB use `football-rb-system`. For advanced VBT use `vbt-rfd-open-sets`. For clinical/prehab use `clinical-prehab-system`. For HYROX/hybrid use `hyrox-hybrid-system`. For COD/footwork use `football-cod-footwork`. For tendon/power use `tendon-power-architecture`. For advanced recovery/bioenergetics use `energy-systems-recovery`. For initial assessment use `athlete-profiling-benchmarking`.
