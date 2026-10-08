---
name: vbt-rfd-open-sets
description: "Velocity-based training skill for RFD, explosive strength, open sets methodology, readiness management, and velocity-loss based load prescription. Use for advanced load prescription, CNS monitoring, and power-oriented programming (Squillante VBT protocol, Bosco open sets)."
compatibility: "Amp (.agents/skills, ~/.config/agents/skills) and Claude Code (~/.claude/skills)"
argument-hint: [exercise, target velocity, velocity loss, power focus, readiness]
---

# VBT RFD Open Sets

**Status: standby.** Use only when the athlete has a velocity device (encoder or validated app). Without one, prescribe by RPE/RIR (`elite-sc-system`).

**Evidence tags.** `[Source Year, doi, grade]`; grades VERIFIED, UNVERIFIABLE, OPINION (coaching practice), C (internal rule). Audit: 2026-10-08.

## Mission

Use velocity as the language of neural quality. Training power without at least reasoning in terms of velocity means proceeding by feel, without objective feedback.

## VBT as biofeedback

Velocity-based training is not a technological luxury: it is the most reliable monitor for understanding daily readiness, stimulus quality, fatigue accumulation, and the difference between useful work and junk reps.

### Intent to move
Explosive intent is non-negotiable. Even with heavy loads (typical of powerlifting), the neural intention must remain to move the load as fast as possible.

### Average velocity vs peak velocity
- Average velocity: "grinding" lifts, non-ballistic (squat, bench, deadlift).
- Peak velocity: ballistic lifts (clean, snatch, jump, throw).

## Velocity loss zones

Only one comparison is tested: in the squat, 20% vs 40% velocity loss. "VL20 resulted in similar squat strength gains than VL40 and greater improvements in CMJ" (9.5% vs 3.5%); "VL40 training elicited a greater hypertrophy" and "a reduction of myosin heavy chain IIX percentage" [Pareja-Blanco 2017, doi:10.1111/sms.12678, abstract, VERIFIED].

The finer zones, their labels and the target velocities in the table below have no source [UNVERIFIABLE]. Treat them as a coaching map, not as data.

| Velocity loss | Neuromuscular state | Goal | Indicative target velocity |
|---|---|---|---|
| 0-10% | Maximum readiness | Peak power / RFD | ~1.3 m/s |
| 10-20% | Minimal fatigue | Explosive strength | ~1.0-1.2 m/s |
| 20-30% | Moderate fatigue | Functional hypertrophy | ~1.0 m/s |
| 40%+ | Extreme fatigue | End the set — high metabolic risk | N/A |

The often-quoted peak-power velocity of 1.0-1.3 m/s has no source; Cormie 2007 reports optimal loads as % of 1RM, not these velocities [UNVERIFIABLE].

## Open Sets (Bosco/Squillante methodology)

[OPINION: method attributed to Bosco and Squillante, not checked against their texts.]

Reps are not fixed by coach convention: the set continues as long as the athlete's velocity stays within the preset quality range. The moment velocity drops below the target threshold (e.g., -20%), the set ends immediately.

Why it works: it respects the day's real readiness, eliminates junk reps, preserves the central nervous system, and keeps the session's adaptive goal clean.

## Prescription logic

**Power/RFD focus**: low velocity loss (0-10%), contained volumes, maximum intent, full recovery (120-180s). **Functional hypertrophy focus**: 20-30% velocity loss, more volume but always with a quality threshold. To be avoided: using high velocity loss when the stated goal is speed-power; doing fixed reps while ignoring actual velocity decay; confusing accumulated fatigue with stimulus quality.

## Readiness management

If the session's baseline velocity is clearly below the athlete's norm, reduce load or volume, or change the session's goal. A useful complementary proxy is the rolling average of Countermovement Jump (CMJ): if jump height is significantly below the athlete's average, load must be adjusted to prevent overtraining. Hard rule: don't chase the number on the bar if velocity or CMJ signal that the system isn't ready.

## Transfer by context

**Football/RB**: VBT protects the 200ms window, improves first-step power, avoids volume that slows transfer, monitors neural state without relying on subjective perceptions. **Hybrid/HYROX**: VBT avoids wasting the neural budget within a concurrent strength-endurance program, maintains the strength reserve needed for stations, and controls the neurological cost of strength relative to the aerobic engine.

## References

- Pareja-Blanco F et al. 2017. Scand J Med Sci Sports 27:724–35. doi:10.1111/sms.12678
- Cormie P et al. 2007. Med Sci Sports Exerc 39:340–9. doi:10.1249/01.mss.0000246993.71599.bf

Velocity-based training framework also draws on: average vs. peak velocity distinction in biomechanics and power physiology; velocity-loss zones and neuromuscular fatigue management (Sports Physiology); open-sets methodology (Bosco, Squillante protocols); Rate of Force Development (RFD) as a power-speed metric; and readiness monitoring via velocity trends and countermovement jump (CMJ). Core frameworks: NSCA velocity-based training principles, elite-sport power monitoring, and neural-fatigue assessment.

## Scope

Skill dedicated to VBT logic. For periodization and weekly audit use `programming-audit-council`. For specific football transfer use `football-rb-system`. For clinical care and return from pain use `clinical-prehab-system`. For tendon architecture use `tendon-power-architecture`.
