---
name: female-athlete-programming
description: "Programming considerations for female athletes: menstrual-cycle phase modulation (follicular / ovulatory / luteal), RPE drift and autoregulation across the cycle, RED-S and amenorrhea red-flag screening, and when to refer to a clinician. Use when programming for a female athlete, when cycle-related energy/strength changes are reported, or when screening for low energy availability."
compatibility: "Amp (.agents/skills, ~/.config/agents/skills) and Claude Code (~/.claude/skills)"
argument-hint: [female athlete, menstrual cycle, luteal phase, RED-S, amenorrhea]
---

# Female Athlete Programming

## Mission

Individualize load and intensity around the athlete's real reported cycle response. Never impose a generic hormonal template. Data from the athlete's own logs overrides the textbook.

## Cycle Phases and Practical Modulation

**Evidence.** A meta-analysis found that performance "might be trivially reduced during the early follicular phase of the MC, compared to all other phases", and that "general guidelines on exercise performance across the MC cannot be formed; rather, it is recommended that a personalised approach should be taken" [McNulty 2020, doi:10.1007/s40279-020-01319-3, full text, VERIFIED]. No phase is a fixed "best window" for PRs. The phase notes below are prompts for what to ask and track, not rules [OPINION].

### Follicular Phase (approx. days 1-14 of cycle)
Some athletes report feeling stronger later in this phase; the early days (menstruation) may be slightly worse on average (McNulty 2020).

**Practical modulation:** only if the athlete's own logs show she feels strong and recovered, bias toward:
- Higher-intensity strength work
- Peak power/RFD days
- Maximum effort sessions

### Ovulatory Phase (approx. day 12-16)
Some athletes report a strength peak here [OPINION].

**Practical modulation:** maintain intensity from follicular if the athlete is feeling capable. Monitor closely for fatigue signals.

### Luteal Phase (approx. days 15-28)
If the athlete reports higher perceived effort, fatigue, or increased recovery time, bias toward:
- Zone 2 aerobic work instead of high-intensity
- Technical work rather than maximal loads
- Longer recovery periods between sets
- Autoregulation by RPE rather than forcing target loads

**Critical principle:** individual response varies dramatically. Some athletes report no cycle effect, others have a pronounced difference. Use the athlete's own data (RPE, performance logs, subjective energy) as the ground truth, not hormonal theory.

## RED-S / Low Energy Availability Screening

Relative Energy Deficiency in Sport (RED-S) and low energy availability are safety gates. Screen for these red flags:

- **Amenorrhea or oligomenorrhea**: absent or lost menstruation (missed ≥3 cycles)
- **Persistent fatigue**: disproportionate to training load
- **Frequent injury/stress reactions**: rapid return of bone/soft-tissue injuries
- **Underfueling**: intentional or inadvertent caloric restriction, rapid weight loss

**If ≥2 flags are present:** do NOT push volume. Refer to a qualified sports medicine clinician, sports nutritionist, or gynecologist. Low energy availability is a medical condition, not a coaching problem.

## Autoregulation Rule

Track RPE and cycle phase together in the weekly feedback sheet:
- Record the cycle day if the athlete is tracking it
- Record perceived effort and energy relative to the prescribed load
- Adjust the following week's intensity per the Continuity Check in `programming-audit-council`, factoring in cycle phase

The feedback sheet becomes the most reliable predictor of individual cycle response.

## Integration with the System

- **coach-builder-router**: for female athletes, also consult this skill during the intake sequence and capture cycle regularity / response.
- **athlete-profiling-benchmarking**: add menstrual cycle questions to the intake interview.
- **programming-audit-council**: weigh RED-S flags in the Clinical/Prehab judge's assessment.
- **hyrox-hybrid-system**: references cycle-phase modulation for hybrid athletes.

## Scope

Skill dedicated to female-athlete programming. Cross-reference `elite-sc-system`, `programming-audit-council`, `athlete-profiling-benchmarking`, and `hyrox-hybrid-system`.

## References

Female-athlete programming framework grounded in: menstrual-cycle physiology and performance variation per sports endocrinology; RED-S (Relative Energy Deficiency in Sport) screening per the IOC consensus (RED-S was "first introduced in 2014 by the International Olympic Committee's expert writing panel" [Mountjoy 2023, doi:10.1136/bjsports-2023-106994, abstract, VERIFIED]); autoregulation via RPE and feedback data; and individual cycle-response tracking per sports science consensus. Core frameworks: ACSM menstrual-function screening, sports medicine RED-S protocols, and female-athlete health standards.
