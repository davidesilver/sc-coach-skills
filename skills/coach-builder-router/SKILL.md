---
name: coach-builder-router
description: "Master routing skill. Use this FIRST to build a personalized S&C coach for any athlete profile (powerlifter, weightlifter, football/RB, HYROX/hybrid, general population). Runs a short intake, maps the athlete to the correct skill stack from this repository, and defines the operating sequence for programming."
compatibility: "Amp (.agents/skills, ~/.config/agents/skills) and Claude Code (~/.claude/skills)"
argument-hint: [new athlete, sport, goal, "build my coach"]
---

# Coach Builder Router

## Mission

This is the entry-point skill of the system. Any athlete or coach who wants to "build their own coach" starts here: the skill identifies the user's profile and assembles the correct skill stack from the repository, without requiring the user to know the internal structure of the system.

## Routing question

Always ask this minimum question before proceeding, unless already clear from context: "What is your primary profile? (1) Powerlifter/maximal strength, (2) Olympic weightlifter, (3) American football/running back, (4) Hybrid athlete/HYROX, (5) General population/fitness, (6) Strength coach managing multiple athletes."

## Profile → skill stack map

### Profile 1 — Powerlifter
Stack: `elite-sc-system` → `athlete-profiling-benchmarking` → `programming-audit-council` → `powerlifting-peaking-system` → `vbt-rfd-open-sets` → `tendon-power-architecture`.
Focus: peaking, attempt selection, RPE autoregulation, RTS block periodization.

### Profile 2 — Olympic weightlifter
Stack: `elite-sc-system` → `athlete-profiling-benchmarking` → `programming-audit-council` → `olympic-weightlifting-technique` → `vbt-rfd-open-sets` → `tendon-power-architecture`.
Focus: snatch/clean & jerk technique, early arm bend correction, jerk footwork.

### Profile 3 — American football / Running back
Stack: `elite-sc-system` → `athlete-profiling-benchmarking` → `programming-audit-council` → `football-rb-system` → `football-cod-footwork` → `tendon-power-architecture` → `clinical-prehab-system` → `vbt-rfd-open-sets`.
Focus: 200ms window, contact balance, ball security, COD, prehab.

### Profile 4 — Hybrid athlete / HYROX
Stack: `elite-sc-system` → `athlete-profiling-benchmarking` → `programming-audit-council` → `hyrox-hybrid-system` → `energy-systems-recovery` → `vbt-rfd-open-sets`.
Focus: aerobic engine, LT1/LT2, compromised running, strength reserve.

### Profile 5 — General population / Fitness
Stack: `elite-sc-system` (simplified use) → `general-population-fitness` → optionally `vbt-rfd-open-sets` and a reduced version of `programming-audit-council` if the client converges toward more specific goals.
Focus: 10 fundamental patterns, adherence, safety, conservative progression.

### Profile 6 — Multi-athlete coach
No fixed stack: use `coach-builder-router` for each individual athlete managed, keeping profiles separate. Use `programming-audit-council` as cross-cutting governance for all athletes.

## Standard operating sequence (any profile)

1. **Intake**: run `athlete-profiling-benchmarking` (or the reduced version for profile 5) to collect history, goals, performance data, clinical limitations. For female athletes, also consult `female-athlete-programming` and capture cycle regularity and cycle-related response.
2. **Preliminary clinical assessment**: if pain flags, recent injuries, or relevant history emerge, activate `clinical-prehab-system` before any load prescription.
3. **Output format choice**: before generating the first program, ask the user once: "In which format do you want your plans delivered? (1) CSV (default), (2) Excel .xlsx, (3) Markdown, (4) PDF." Record the choice and pass it to `programming-audit-council` for all subsequent programs.
4. **Building week 1**: use `programming-audit-council` to generate v1 in the chosen format, run the 3-judge audit, and issue v2 with the Sanford gate.
5. **Applying the domain skill**: integrate the profile's specialist skill (powerlifting, weightlifting, football, HYROX, general population) into the v2 logic.
6. **Continuous weekly cycle**: every following week requires the weekly continuity check described in `programming-audit-council`, never a reset from scratch.

## Skill combination rule

Never use an isolated domain skill without `elite-sc-system` as the base and without `programming-audit-council` as governance, except for specific, narrow requests (e.g. "just explain jerk technique to me").

## Auto-diagnosing the profile from free conversation

If the user does not explicitly state their profile, use these signals to route:
- Mentions 1RM on squat/bench/deadlift, meet, federation → Profile 1.
- Mentions snatch, clean & jerk, competitive CrossFit with an Olympic technical focus → Profile 2.
- Mentions a team role, football, RB, combine, race-day sprint/COD → Profile 3.
- Mentions HYROX, hybrid race, running + functional stations → Profile 4.
- Mentions weight loss, muscle tone, general health, no competitive goal → Profile 5.
- Manages multiple athletes or talks about them in the third person with requests for multiple programs → Profile 6.

## Scope

This is the repository's entry-point skill. Every other skill listed above is reachable starting from this router.
