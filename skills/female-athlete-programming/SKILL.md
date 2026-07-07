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

### Follicular Phase (approx. days 1-14 of cycle)
Window that often tolerates higher intensity and strength. Estrogen rising, metabolic rate may increase, perceived effort may feel lower relative to load.

**Practical modulation:** if the athlete reports feeling strong and recovered, this window can bias toward:
- Higher-intensity strength work
- Peak power/RFD days
- Maximum effort sessions

### Ovulatory Phase (approx. day 12-16)
Often a secondary strength peak before luteal fatigue sets in.

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

Female-athlete programming framework grounded in: menstrual-cycle physiology and performance variation per sports endocrinology; RED-S (Relative Energy Deficiency in Sport) screening and clinical thresholds per ACSM/IOC/FASEB; autoregulation via RPE and feedback data; and individual cycle-response tracking per sports science consensus. Core frameworks: ACSM menstrual-function screening, sports medicine RED-S protocols, and female-athlete health standards.
