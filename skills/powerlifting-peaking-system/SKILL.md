---
name: powerlifting-peaking-system
description: "Powerlifting-specific programming skill. Covers block periodization (RTS Development/Pivot Block model), linear peaking phases (volume→strength→power), tapering protocols pre-meet, RPE-based autoregulation, and competition-day attempt selection for squat/bench/deadlift."
compatibility: "Amp (.agents/skills, ~/.config/agents/skills) and Claude Code (~/.claude/skills)"
argument-hint: [meet prep, peaking block, tapering, RPE autoregulation, attempt selection]
---

# Powerlifting Peaking System

## Mission

A powerlifter doesn't train to "feel strong" — they train to express maximum strength on three lifts on one specific day. Every block must serve that date, not some abstract ideal of general strength.

## Development Block / Pivot Block Model (RTS)

A bottom-up approach to periodization, an alternative to classic linear periodization.

### Development Block
A microcycle (1 week) is repeated until performance drops on a reference lift (e.g., a single at RPE8 + 4x4 back-off). The number of times the microcycle is repeated before performance drops defines the athlete's individual "time to peak" (TTP).

- If the TTP is long (e.g., 11 weeks), it becomes difficult to react to changes in a timely manner.
- To shorten the TTP and make it more manageable, increase the weekly frequency of the target lift (e.g., an A+B scheme within the same microcycle).
- The first Development Block should be carried past the peak: exceeding the peak is recognized when performance drops for two or more consecutive weeks.

### Pivot Block
Not a deload — it's a change of stimulus that reduces fatigue, lowers intensity, varies the training structure, and prepares the athlete for the next Development Block. Typical duration: roughly one-third the length of the preceding Development Block. Example RPE distribution in a Pivot Block: 10 reps @RPE6, 10 reps @RPE7, 10 reps @RPE8, plus an unload set.

## Classic Linear Periodization (alternative)

A phased model spanning 12-16 weeks, with rising intensity and declining volume:

| Phase | Typical duration | Rep range | Intensity |
|---|---|---|---|
| Hypertrophy/volume | Early weeks | 8-12 reps | Moderate |
| Strength | Middle phase | 3-6 reps | High |
| Power/peaking | Final weeks pre-meet | 1-3 reps | ≥90% 1RM |

Simpler, higher-volume movements should be placed in the early phases, when it's easier to accumulate work without excessive technical risk.

## Key Peaking Principle (JTS)

Intensity preserves fitness better than volume. Reaching maximal strength requires both high volume and high intensity in the correct phases, but in the final peaking phase volume must be cut while maintaining high intensity, to dissipate fatigue without losing the neural adaptations already acquired.

## Pre-Competition Tapering

Tapering (or in some cases a temporary cessation of training) before a major competition serves to improve performance by dissipating accumulated fatigue while retaining strength adaptations. Practical rules:
- Progressively reduce volume in the final 1-3 weeks pre-meet, keeping intensity peaks low in frequency but still present (openers at meet weight).
- Never introduce new exercises or technical patterns during the taper phase.
- The goal of the taper is to arrive on meet day "fresh but not stale": a taper that's too long or too aggressive can cause a loss of neural specificity.

## RPE Autoregulation

Every main session should be managed with daily RPE/RIR (see also `elite-sc-system` and `vbt-rfd-open-sets` for integration with velocity). If actual RPE systematically exceeds the target by more than 0.5-1 point across multiple sessions, the block needs to be reassessed: either the prescribed load was poorly calibrated, or accumulated fatigue calls for an early Pivot Block.

## Attempt Selection on Meet Day

General principles derived from competitive practice:
- First attempt: 90-93% of estimated max, a near-certain lift, to build confidence and "open up" the nervous system.
- Second attempt: toward the personal record or slightly above, based on how the first attempt felt.
- Third attempt: a maximal attempt, decided only after seeing the technical quality of the second.
- Never change attempt selection strategy under the emotional pressure of meet day: the decision should be made with a clear head, ideally pre-planned with the coach.

## Training Splits

For beginners: a 3-day split, one main lift per session. For intermediate/advanced lifters: a 4-day split or Push-Pull-Squat, with greater exercise variety and frequency per pattern. Recovery rule: 2-3 days between sessions that heavily stress the same muscle group.

## Periodic Assessment

Every 12-16 weeks, objectively assess: absolute strength progress, technical quality, plateaus, and any need to modify exercise selection, split, or periodization strategy.

## Scope

Skill dedicated to competitive powerlifting. For core biomechanical logic use `elite-sc-system`. For weekly governance and auditing use `programming-audit-council`. For integrated RPE/velocity management use `vbt-rfd-open-sets`. For tendon architecture and RFD use `tendon-power-architecture`.
