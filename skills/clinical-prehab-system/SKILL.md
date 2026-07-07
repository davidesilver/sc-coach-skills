---
name: clinical-prehab-system
description: "Clinical prehab and return-to-performance skill. Covers Sanford soreness rules, Copenhagen adduction protocol, soleus/MTSS management, tibialis and foot intrinsic work, collision shielding, and criterion-based return-to-run for football and power-speed athletes."
compatibility: "Amp (.agents/skills, ~/.config/agents/skills) and Claude Code (~/.claude/skills)"
argument-hint: [pain area, MTSS, adductors, tendon, return-to-run]
---

# Clinical Prehab System

## Mission

Reduce injury risk and manage the return to load with objective criteria, not optimism. Tissue does not negotiate with the coach's or athlete's narrative.

## Sanford Soreness Rules

1. Pain at warm-up that persists → stop, 2 days off, return to the previous step.
2. Pain at warm-up that disappears → stay at the current step, do not advance until pain-free.
3. Pain that disappears but returns during the session → stop, 2 days off, return to the previous step.
4. Pain the day after → 1 day off, do not advance the program.

These rules govern load objectively, regardless of the athlete's mood or motivation.

## MTSS and the soleus factor

### Clinical reframe
Medial Tibial Stress Syndrome (MTSS) should be treated as a low-risk bone stress injury, not as trivial "shin splints." Clinical diagnosis: tenderness along the posteromedial border of the tibia for more than 5cm, positive fulcrum test, pain during hop test. Focal tenderness under 5cm instead suggests a tibial stress fracture, which requires a completely different loading profile.

### The role of the soleus
The soleus absorbs significantly more tibial load than the gastrocnemius during running and is the main mechanical shield against repeated tibial stress. A weak or fatigued soleus lets shear forces reach the periosteum.

### Criterion-based progression (phases)
- **Phase I (acute, 7-14 days)**: if pain during ADL, boot/splint for 2-4 weeks. NWB strengthening (quads/glutes), foot intrinsic work, low-impact aerobic conditioning.
- **Phase II (subacute, weeks 2-6)**: progressive loading from 50%, heel raise progression (bilateral → eccentric → single-leg).
- **Phase III (weeks 2-8)**: organized return-to-run, single-leg plyometrics.
- **Phase IV**: Heavy Resisted Sprint Training (sled 60-80% BW) to optimize horizontal force production and 0-10m acceleration.

### Mandatory benchmarks before advancement
- 25 bilateral single-leg heel raises without pain.
- 15 single-leg hops without pain.
- 30 minutes of continuous walking without flare-up.
- Squat 60% BW, 6 reps with a 6-second hold each.

## Copenhagen Adduction Protocol

Non-negotiable protocol for sports with lateral cuts, jump cuts, braking, and twisting. Reference data in the sources: +35.7% eccentric adductor strength, -41% groin injury risk.

### Progressive volume (8 weeks)
1. Weeks 1-2: 2x6 reps/side, 2-3x/week — technical focus.
2. Weeks 3-5: 3x10 reps/side — load tolerance focus.
3. Weeks 6-8: 3x15 reps/side — volume accumulation.
4. Maintenance: 250 total reps/leg to preserve the adaptation.

Programming rule: integrate Copenhagen without duplicating redundant adductor work in the same microcycle. If groin pain appears, a mandatory 48h gap is required before the next adductor stimulus.

## Tibialis, foot, and distal control

Anterior tibialis work is necessary for decelerative control, ankle health, and braking tolerance. The foot is the first contact link: without foot activation (short foot / foot intrinsics), center-of-mass management worsens and unwanted tibial torsion increases, with negative effects on cutting quality.

## Collision shielding (spine protection)

For contact sports: cervical reinforcement (chin tucks, multiplanar isometrics) to reduce whiplash-type head acceleration during impacts; thoracic mobilization to restore extension and rotation, preventing the lumbar spine from compensating during rotations and stiff-arms.

## Return-to-run / return-to-field

The return is never time-based, it is always criterion-based. Mandatory checks: pain under control per Sanford, local benchmarks passed, acceptable running pattern, tolerance to progressions without flare-up. Gait modifiers to consider during the return phase: cadence management, surface choice (low-impact grass before turf), trunk control, reducing overly early chaotic exposures.

## Scope

Skill dedicated to the clinical/prehab side. For weekly programming use `programming-audit-council`. For football/RB transfer use `football-rb-system`. For open sets and velocity use `vbt-rfd-open-sets`. For in-depth tendon architecture use `tendon-power-architecture`.
