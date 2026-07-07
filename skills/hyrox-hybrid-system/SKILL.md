---
name: hyrox-hybrid-system
description: "Hybrid athlete and HYROX-specific training system. Covers the 70/30 aerobic/strength split, VO2max/LT1/LT2 thresholds, 5-zone heart rate table, compromised running, brick session design, strength reserve, station-by-station technique cues for all 8 stations, Open/Pro benchmarks, 12-week periodization, and race pacing. Use whenever the athlete races HYROX, trains as a hybrid strength+endurance competitor, or needs a fixed run+functional-station format programmed. Strength is a means, not the end, for hybrid competitors."
compatibility: "Amp (.agents/skills, ~/.config/agents/skills) and Claude Code (~/.claude/skills)"
argument-hint: [HYROX prep, hybrid athlete, compromised running, brick session, station cues, race pacing]
---

# HYROX Hybrid System

## When to activate this skill

Together with `elite-sc-system` (always the base) when the athlete:
- Trains for HYROX Open or Pro
- Is a "hybrid" who does both strength and endurance work in the same mesocycle
- Needs to manage the interference effect between maximal strength and aerobic capacity

## Mission and core principle: the 70/30 split

In the hybrid/HYROX athlete, pure strength is a means, not an end. About 70% of race duration is aerobic (running + SkiErg + Row), while only 30% is pure strength/power. This figure overturns the most common mistake: programming like a powerlifter instead of like a middle-distance runner with strength stations. Priority goes to the aerobic engine, LT1/LT2 thresholds, compromised running, and managing strength reserve across the stations.

## Most common mistake

Training with excessive bias toward pure strength and insufficient conditioning. HYROX is a race dominated by the endurance component: 8km of running interspersed with 8 functional stations — the real limiter in most athletes is the engine, not maximal strength.

## The three physiological pillars

1. **VO2max** — the size of the engine, the genetically-capped but trainable ceiling.
2. **LT1 (aerobic threshold)** — the base of the engine, mostly Zone 2 work, builds the capacity to clear lactate at sub-maximal intensities and supports recovery between stations.
3. **LT2 (anaerobic threshold)** — the maximum sustainable pace for ~60 minutes; the true predictor of race time. Work here must be specific and not excessive, so as not to compromise overall recovery.
4. **Fractional utilization** — the % of VO2max sustainable for the entire duration; it separates the Elite athlete from the Intermediate more than absolute VO2max does.

## Operational heart rate zones (5 zones)

| Zone | %HRmax | Talk test | Use |
|---|---|---|---|
| 1 | 50-60% | Can sing a song | Active recovery, clearance |
| 2 | 60-70% | Full conversation | Aerobic base, capillary/mitochondrial density |
| 3 | 70-80% | Short sentences | LT1 / sustainable race pace |
| 4 | 80-90% | 1-2 words | LT2 / lactate clearance, the true engine of the Row |
| 5 | 90-100% | No words | VO2max, final 100 Wall Balls |

## Compromised running

Running in HYROX is never "fresh": every stretch of the 8km is run after a station that has already fatigued specific patterns (e.g., running after sled push, running after wall balls). Training transfer must include running sessions performed in an induced pre-fatigue state, not just isolated easy-paced running. Compromised running is the variable that separates Intermediate from Advanced: those with specific training degrade their pace less after heavy stations.

**Practical race pacing rule**: run the fresh kilometer 10-15 seconds/km slower than your 10k PR, to stay close to LT2 without going into the red too early.

### Brick Protocol (this skill's signature session)

- 4-6 rounds of 800m-1km at race pace, immediately followed by 1 leg-heavy station (sled push, lunge)
- Start at 60-80% of race volume, build to 100% in the final 3-4 weeks before the race
- No more than 1 full brick session per week: it is the highest systemic-cost session in the microcycle

## Strength reserve: why strength still matters

Strength should be programmed as a functional reserve for the stations, not as an aesthetic or maximal goal in its own right. Each station has a specific strength-endurance profile (e.g., sled push/pull requires repeated horizontal strength-power, wall balls require local muscular endurance on the squat-throw pattern). Maximal strength in the gym is only useful if it translates into efficiency and energy savings on the specific station.

The Strength Reserve concept states that the higher the absolute 1RM, the lower the % of effort required by fixed race loads (e.g., 152kg sled). If your max is 200kg, the Pro sled represents 76% instead of the 100%+ faced by someone with a 150kg max: less drain on the central nervous system, fresher legs for the run that follows.

| Athlete profile | Typical weakness | Training priority |
|---|---|---|
| Endurance-dominant | Sled push/pull, wall ball | Structural hypertrophy, maximal strength |
| Strength-dominant | Run endurance, pacing, LT2 | Zone 2 aerobic base, running economy |

## The 8 stations: technique cue and mistake to avoid

| Station | Technique cue | Common mistake |
|---|---|---|
| SkiErg 1000m | Hip-hinge, hands "in pockets" at the end of the pull | Pulling with the arms only |
| Sled Push 50m | Rigid shoulder-to-ankle line, short and powerful steps | Long strides that break the push line |
| Sled Pull 50m | Walking backward, using body weight as leverage | Pulling with the arms, burning out the shoulders for the Row |
| Burpee Broad Jump 80m | Step-up (one foot at a time) instead of jumping | Explosive jump that spikes heart rate |
| Rowing 1000m | Powerful leg drive, controlled slide (active recovery) | Treating it like a sprint instead of an active recovery station |
| Farmers Carry 200m | Chest up, scapulae retracted, short steps | Slow, unbalanced walk |
| Sandbag Lunges 100m | Upright torso, sandbag high on the traps | Torso leaning forward, knee "slamming" into the ground |
| Wall Balls 75-100 | Power from the legs, arms only guide | Unbroken single sets (use blocks of 20 with 5s micro-pauses) |

### Roxzone: the hidden station

Time spent in the Roxzone (transition) should be treated as active recovery, not passive rest: light jog, rhythmic breathing 3-in/2-out, resetting heart rate before starting the next kilometer.

## Managing fatigue in concurrent training

Concurrent strength-endurance training generates interference if not managed carefully. Practical rules:
- Separate heavy strength sessions and high-intensity aerobic sessions in time when possible (not on the same day, or with adequate spacing).
- Use Zone 2 as an active recovery tool, not as a stimulus that competes with strength.
- Monitor the neurological cost of strength work (see `vbt-rfd-open-sets`) so it does not undermine the quality of subsequent aerobic work.

## The 10% rule and prevention

Weekly running volume increases should not exceed 10%, to protect muscle-tendon integrity during the accumulation of brick-specific load. Always integrate with `clinical-prehab-system` for Copenhagen/tibialis work when running volume increases.

## Periodization for HYROX

A typical preparation block follows a logic of progressive build-up: aerobic base and general strength in the early phases, then station-specific work and race pacing in the final phases, with a taper that preserves aerobic capacity while reducing heavy strength volume.

| Phase | Weeks | Focus |
|---|---|---|
| Foundation | 1-4 | Zone 2 aerobic base, foundational strength 3x10 RPE 7-8 |
| Power and specificity | 5-8 | LT2 intervals, functional power, sled/burpee |
| Simulation | 9-11 | Full brick, compromised running Zone 4-5 |
| Tapering | 12 | -40/50% volume, intensity maintained, CNS/sleep focus |

## Pacing and competitive benchmarks

Reference benchmarks for competitive tiering are based on station times and running splits compared against category standards (open, pro, elite). Programming should target specific improvement of the athlete's weakest splits (running vs. stations), identified through testing and partial race simulations.

| Station | Women Open | Women Pro | Men Open | Men Pro |
|---|---|---|---|---|
| Sled Push 50m | 102 kg | 152 kg | 152 kg | 202 kg |
| Sled Pull 50m | 78 kg | 103 kg | 103 kg | 153 kg |
| Farmers Carry | 2x16kg | 2x24kg | 2x24kg | 2x32kg |
| Sandbag Lunges | 10kg | 20kg | 20kg | 30kg |
| Wall Balls | 4kg/75 | 6kg/100 | 6kg/100 | 9kg/100 |

Clinical recommendation: sub-75 minutes in Open before moving up to Pro, to ensure foundational strength can handle the heavier loads without compromising running mechanics.

## Clinical notes for female athletes

Follicular phase (days 1-14): optimal window for maximal strength PRs and high-intensity work. Luteal phase: higher perceived RPE due to body temperature, shift emphasis toward Zone 2 volume and recovery.

## Scope

Skill dedicated to hybrid athletes and HYROX. For basic biomechanical logic use `elite-sc-system`. For programming governance use `programming-audit-council`. For VBT and neural load management use `vbt-rfd-open-sets`. For in-depth bioenergetics and recovery use `energy-systems-recovery`.

## References

Hybrid athlete and HYROX training framework grounded in: aerobic-threshold physiology (VO2max, LT1/LT2, lactate dynamics); concurrent strength-endurance training and interference management (Sports Medicine); compromised-running and brick-session protocols from elite HYROX coaching; station-specific technique and strength-reserve concepts; heart-rate zone operational guidelines; and menstrual-cycle phase modulation for female athletes (see `female-athlete-programming`). Core frameworks: NSCA concurrent training, APTA zone-based training, and elite-hybrid athletic programming consensus.
