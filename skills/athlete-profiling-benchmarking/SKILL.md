---
name: athlete-profiling-benchmarking
description: "Athlete intake, assessment, and benchmarking skill. Covers the NFL-style pre-onboarding interview structure, injury history screening, combine-style physical testing, mobility/asymmetry screening, positional performance benchmarks (RB combine data), neuromuscular profiling (energy-system dominance, tendon status, readiness), and the deconditioned-athlete loading rule. Use at the start of any new coaching relationship, after a long layoff, injury, or season transition, and before writing any program for building a criterion-based rebuilding phase — no load should ever be prescribed without this data."
compatibility: "Amp (.agents/skills, ~/.config/agents/skills) and Claude Code (~/.claude/skills)"
argument-hint: [intake interview, assessment, combine testing, benchmarking, deconditioned athlete, neuromuscular profile]
---

# Athlete Profiling & Benchmarking

## Mission

No program is written before there is data. A coach taking on an athlete returning from a layoff or never previously assessed must conduct a structured interview and a minimum test battery before any load prescription. None of the programming skills (`programming-audit-council`, `periodization-block-planner`, `hyrox-hybrid-system`) can function without real baseline data: prescribing loads without an intake is the most common cause of "black box" programming.

## Intake interview structure

The interview always precedes programming. It must collect data in blocks:

1. **Current profile and specific goal**: primary/secondary role, competitive goal with a time horizon, subjective perception of the 3 main physical limitations, single physical priority to invest in, real weekly time available.
2. **Injury and health history**: prior surgeries, recurring sprains, knee/hip/pelvis/lower back/shoulder/wrist injuries, concussions, chronic medical conditions, allergies/intolerances, subjective scale of joint/tendon integrity.
3. **Current deconditioning**: actual time of inactivity, cause of the layoff (injury, off-season, personal), immediate qualitative tests (walking, push-ups, stairs), pain/stiffness on waking, weight and body composition changes, sleep quality and stress.
4. **Past performance data**: 1RM or estimates on squat/hinge/press/pull, jump tests (CMJ, squat jump, broad jump) with date, sprint times (10m/20m/40yd) and agility (3-cone, shuttle) with timing method, role in the rotation and tactical usage.
5. **Technical game profile**: type of athlete (power/COD/elusive/all-round), preferred patterns, feedback received from previous coaches on physical limitations.
6. **Strength, power, and weight-room history**: average RPE held on main lifts, most-trained strength patterns, familiarity with Olympic lifts, problematic exercises, relative strength (kg/kg BW), familiarity with RPE/RIR and autoregulation.
7. **Mobility, posture, and asymmetries**: prior functional screening, limitations in deep squat, half-kneeling, thoracic mobility, left/right asymmetries, postural notes.
8. **Conditional capacities**: perceived strength in acceleration/mid-speed/top speed, confidence in changes of direction, prior work on running mechanics, available video data.
9. **Metabolic capacity**: response to repeated loads in game situations, preference between specific vs generic conditioning, heart rate data, tolerance to gasser/shuttle-type protocols.
10. **Lifestyle and recovery**: actual hours of sleep, non-physical stress, nutrition (meals, protein, tracking), alcohol/substances, supplementation already in use, access to recovery tools.
10.5. **Menstrual cycle and energy availability (female athletes only)**: cycle regularity (regular/irregular/absent), cycle-related changes in energy, strength, or fatigue, history of amenorrhea or missed cycles, perceived underfueling or rapid weight changes — feed into `female-athlete-programming` for cycle-modulation and RED-S screening.
11. **Environment, equipment, and logistics**: gym access and equipment type, field/track access, available monitoring tools, willingness to track data.
12. **Communication preferences**: desired level of detail in programming, tendency to give feedback (proactive vs "grit your teeth"), non-negotiable time/mindset constraints.

## Test battery: recommended execution order

| Order | Test | What it measures | Link |
|---|---|---|---|
| 1 | 6-pattern screening | Movement quality, asymmetries, pain | `biomechanics-movement-screen` |
| 2 | Tendon isometric tests | SL heel raises, SL hops, Squat 60%BW 6x6 | `clinical-prehab-system` |
| 3 | 1RM or RPE-based estimate | Main squat, hinge, press, pull | `periodization-block-planner` |
| 4 | Speed/power tests | 10-20m sprint, vertical/horizontal jump | `vbt-rfd-open-sets` (if an encoder is available) |
| 5 | Specific energy-system test | RSA if team sport, estimated LT1/LT2 if hybrid | `energy-systems-recovery` / `hyrox-hybrid-system` |

### Minimum battery even for a deconditioned athlete

Tests that can be performed with no risk even in a deconditioned state, to establish a minimum baseline before Phase 1:

- **General**: morning bodyweight over 3 days, maximal technical push-ups, isometric plank with clean technique, bodyweight squat up to RPE 8.
- **Strength (RPE 7-8, not 1RM)**: squat or safe variant for 5 comfortable reps, hinge (trap bar/RDL) 5 reps, flat bench press 5 reps, maximal pull-ups (with any assistance quantified).
- **Field**: 3 timed 10m sprints (best time), 3 x 20m sprints, optional 300yd shuttle or 6x40yd if the athlete feels ready (otherwise defer 2-3 weeks).

Before administering the full battery, always verify: the athlete's readiness to test immediately vs the need for preliminary soft reactivation, and the presence of current limitations that advise against immediate sprints/eccentrics.

## Neuromuscular profiling: what to classify

- **Energy dominance**: pure power (ATP-CP) vs RSA vs aerobic-dominant — determines the initial programming bias (see `energy-systems-recovery`).
- **Tendon status**: green (no pain, benchmarks reached) / yellow (mild intermittent pain) / red (reproducible pain, requires the clinical filter of `clinical-prehab-system` active from the start).
- **General readiness level**: deconditioned (>4 weeks off) vs maintained vs at full load.

### Operating rule for a deconditioned athlete

If the intake reveals >4 weeks off: main lift RPE ≤6.5 for the first 2 weeks, no exceptions — this rule overrides any of the athlete's enthusiasm to "make up for lost time."

## Positional reference benchmarks (Running Back)

Historical/combine reference values useful for contextualizing the athlete's tests (source: combine data and positional profiling reports):

| Test | Indicative reference |
|---|---|
| 40-yard dash | Variable by role, the isolated value is less informative than the 10-yard split |
| Vertical Jump | Reference for vertical explosiveness |
| Broad Jump | Reference for horizontal power |
| L-Cone Drill | Reference for COD/agility |
| Pro Shuttle (5-10-5) | Reference for short-range change of direction |

The most useful diagnostic value for an RB is not the absolute 40-yard dash, but the 10-yard split, which better reflects the first-step dominance that is actually useful in-game.

## Intake output: what it must produce

A complete intake must produce 4 written outputs before proceeding to any programming v1:

1. Readiness profile (green/yellow/red for tendons, deconditioned yes/no)
2. Maxes/reference estimates for the main patterns
3. Active clinical flags (pain, asymmetries, areas to monitor)
4. Stated primary goal (hypertrophy, strength, HYROX, football, hybrid)

Always link this skill's output to `programming-audit-council` for generating the first week, and to `clinical-prehab-system` if pain flags or relevant injury history emerge.

## Error to avoid

Never generate a microcycle v1 without the 4 outputs above. If the user directly asks for a program without having provided this data, the correct response is to collect the intake first, not to assume default values.

## References

Athlete assessment and profiling framework grounded in: NFL Combine testing protocols and running back position-specific benchmarks; intake interview structure and health-history screening per sports medicine standards; neuromuscular classification (energy dominance, tendon status, readiness levels); criterion-based testing batteries (FMS, functional movement patterns, sprint/jump testing); and deconditioned-athlete loading rules (RPE management, phased reactivation). Core frameworks: APTA return-to-sport standards, NSCA assessment guidelines, and clinical sports medicine intake protocols.

## Scope

Skill dedicated to initial assessment. For general programming logic use `elite-sc-system`. For weekly audit and governance use `programming-audit-council`. For football/RB specifics use `football-rb-system`. For detailed biomechanical screening use `biomechanics-movement-screen`.
