---
name: exercise-library-video
description: "Exercise naming and demonstration-link standard for generated programs. Enforces a canonical exercise name for every prescribed movement, a mapping of common variants/synonyms to that canonical name, and a video-link policy: verify a link demonstrates the exact prescribed movement, never link a different exercise, and always provide a descriptive fallback when no reliable link exists. Use whenever a program with a VIDEO_LINK or exercise-name column is generated."
compatibility: "Amp (.agents/skills, ~/.config/agents/skills) and Claude Code (~/.claude/skills)"
argument-hint: [exercise naming, video link, demonstration, CSV export]
---

# Exercise Library & Video

## Mission

Every prescribed movement gets one unambiguous canonical name and, where used, a demonstration link that actually shows that exact movement. Vague naming and mismatched video links break program clarity and athlete adherence.

## Canonical Naming Rule

Format: `PrimaryPattern + Implement + Variant` (e.g., "Barbell Back Squat", "Dumbbell Romanian Deadlift", "Trap-Bar Deadlift").

The canonical name is durable and does not change based on who is watching. It is the baseline against which all variants and synonyms are normalized.

### Common movements with canonical names and typical synonyms

| Canonical name | Common synonyms / variants |
|---|---|
| Barbell Back Squat | Back squat, high-bar squat, low-bar squat, BB squat |
| Barbell Front Squat | Front squat, goblet squat (different implement) |
| Dumbbell Goblet Squat | Goblet squat, dumbbell squat |
| Barbell Deadlift | Conventional deadlift, deadlift, DL |
| Trap-Bar Deadlift | Hex-bar deadlift, hexbar DL |
| Dumbbell Romanian Deadlift | RDL, single-leg RDL (variant) |
| Barbell Bench Press | Bench press, flat bench, BB bench |
| Dumbbell Bench Press | DB bench, dumbbell bench |
| Barbell Bent-Over Row | Barbell row, bent-over row, BB row |
| Dumbbell Single-Arm Row | Single-arm dumbbell row, unilateral row |
| Pull-up | Unweighted pull-up, kipping pull-up (variant) |
| Dumbbell Curl | Biceps curl, DB curl |
| Barbell Back Squat, high bar | High-bar squat, high bar back squat |
| Barbell Incline Bench Press | Incline bench press, incline press |
| Cable Chest Fly | Pec fly, cable fly |

## Video-Link Policy

1. **A link must demonstrate the exact canonical movement**, same implement and variant. If the link shows a different exercise (e.g., a "leg press" link used for a "squat" movement), do NOT include it.
2. **If unsure the link matches, DO NOT include it** — write the canonical name only, so the athlete can search it themselves.
3. **Never reuse a link across biomechanically different movements.** A squat video is not a leg-press video, even if they "look similar."
4. **Prefer stable, reputable demonstration sources:** coaching/educational channels, peer-reviewed biomechanics demonstrations, established strength-training platforms. Avoid single short-form videos without attribution.
5. **Always keep the canonical name as the durable fallback** even when a link is present. The athlete reads the name first; the link is secondary clarity.

## Integration

`programming-audit-council` calls this skill to fill the `VIDEO_LINK` column and to normalize the `EXERCISE` column before emitting a program. When a program is generated, every exercise in the `EXERCISE` column must be verified against this canonical list, and a `VIDEO_LINK` is populated only when a reliable, verified link exists.

## Scope

Cross-reference `programming-audit-council` and `elite-sc-system`. This skill ensures that programs are clear, reproducible, and that athletes can find accurate demonstrations of every prescribed movement without guessing.

## References

Exercise naming framework grounded in: biomechanical movement taxonomy (primary pattern, implement, mechanical variant); exercise-demonstration standards from coaching education; and practical naming conventions in strength-training literature (NSCA, IWF, APTA). The goal is clarity and reproducibility: one name, one movement, one video per exercise.
