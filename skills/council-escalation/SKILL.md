---
name: council-escalation
description: "Optional multi-expert council for ambiguous, high-stakes S&C decisions. Convenes five advisor lenses, runs a peer-review pass, and a chairman synthesis that states a recommendation plus the strongest dissent. Gated to decisions where a single pass is risky: return-to-run after injury, peak-now vs extend-the-block, conflicting goals, and the first macrocycle for a deconditioned athlete. Not for routine week generation."
compatibility: "Amp (.agents/skills, ~/.config/agents/skills) and Claude Code (~/.claude/skills)"
argument-hint: [return-to-run, peak vs extend, goal conflict, first macrocycle, high-stakes decision]
---

# Council Escalation

## When to use (gate)

This skill is an OPT-IN escalation, not an automatic wrapper. Use ONLY for these decision types:

1. **Return-to-run / return-to-play after injury** — the decision to advance from clinical management to loaded sport-specific work
2. **Peak now vs extend the block** — conflicting signals about readiness: is the athlete ready to peak, or should the block be extended?
3. **Conflicting goals** — e.g., maximal strength vs HYROX endurance in the same window; requires trade-off arbitration
4. **First macrocycle design for a deconditioned athlete** — the initial high-stakes structure sets the trajectory

For everything else (routine week generation, minor load adjustments, standard progressions), the internal 3-judge audit in `programming-audit-council` is sufficient. Do not escalate.

## The Five Advisor Lenses

Each advisor produces an independent short analysis (300-400 words). They do NOT know each other's analysis in advance.

### 1. Strength Scientist
Checks: load/volume/adaptation trajectory, periodization logic, energy-system specificity, recovery sufficiency. Asks: "Does the load prescription match the adaptive stimulus we're trying to drive?"

### 2. Sport-Specific Coach
Checks: transfer to the actual sport/event, field demands, technical readiness, tactical readiness. Asks: "Is the athlete ready to handle the sport's actual demands, not just the gym simulation?"

### 3. Clinician / Physio
Checks: tissue tolerance, injury risk, Sanford gates, pain thresholds, medical clearance. Asks: "Are there any structural, systemic, or medical contraindications to this decision?"

### 4. Adherence / Psychology
Checks: athlete buy-in, history of adherence, stress/life load, motivation, likelihood of actually executing the plan. Asks: "Will the athlete actually do this, given their history and current headspace?"

### 5. Devil's Advocate
Explicitly argues the strongest case AGAINST the leading recommendation. This advisor's job is to surface risks, worst-case scenarios, and hidden assumptions. Asks: "What could go wrong, and what would we regret if we ignore it?"

## Peer Review

Each of the five advisors spends 200-300 words critiquing the others' analyses, not attacking them but asking: "What am I missing from your perspective? Where do we disagree, and why?"

## Chairman Synthesis

A single recommendation: the action, the core reasoning, and the likelihood of success. Then, explicitly name the single strongest remaining dissent — do not hide or soft-pedal disagreement.

Example:
> **Recommendation:** Extend the block by 2 weeks rather than peak now. The athlete's sleep is still <7h (continuity check red flag), and the clinic advises another 10 days before full plyometric load.
>
> **Strongest dissent:** The Sport-Specific Coach argues the athlete could handle sport-specific work now (non-ballistic field drills, footwork, vision work) while keeping CNS-heavy strength on hold, which would bridge the gap without a full 2-week stall.

## Cost Note

This is heavier than a normal single pass; it is designed to be run deliberately on the gated decisions above, and the structured multi-lens process is the value, not raw model horsepower. It can run on a cheaper model.

## Scope

Cross-reference `programming-audit-council` and `coach-builder-router`.

## References

Multi-expert council / LLM-parliament methodology for high-stakes decisions in domains with competing objectives and uncertain outcomes. The five-lens structure (science, domain expertise, clinical safety, behavioral realism, adversarial challenge) is inspired by clinical-decision-support and medical-ethics frameworks.
