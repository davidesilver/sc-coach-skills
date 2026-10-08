---
name: football-cod-footwork
description: "Change-of-direction biomechanics and running back footwork skill. Covers braking over the last 2–3 steps, positive tibia angle, the Big Three cuts (Speed Cut, Jump Cut, Pressure Step), vision/field-reading, and contact-balance footwork integration."
compatibility: "Amp (.agents/skills, ~/.config/agents/skills) and Claude Code (~/.claude/skills)"
argument-hint: [COD drill, footwork cue, cutting mechanics, field vision]
---

# Football COD & Footwork

## Mission

The primary limiter in elite agility is not raw speed, but deceleration efficiency. Changes of direction are an exercise in gravitational management and multiplanar force dissipation.

**Evidence tags.** `[Source Year, doi, grade]`; grades VERIFIED, UNVERIFIABLE, OPINION (coaching practice), C (internal rule). Audit: 2026-10-08. Cut taxonomy, vision, drills and fault tables are coaching practice [OPINION].

## Braking over the last 2–3 steps

Braking is spread over the last two or three foot contacts before the plant, not done by one step:
- In a 180° turn (505 test), "Greater peak braking forces in shorter ground contact times were demonstrated over the APFC compared to the PFC and FFC" (APFC = antepenultimate, third-to-last contact); the authors recommend "braking strategies that emphasise greater magnitudes of posteriorly directed APFC GRFs" [Dos'Santos 2021, doi:10.1080/02640414.2020.1823130, abstract, VERIFIED; university soccer players].
- For sharper angles, brake early (antepenultimate and penultimate); for shallower cuts the penultimate step carries more of the braking [OPINION for the shallow-angle part].
- The figure "GRF up to 2.7× body weight at the penultimate step" has no source found [UNVERIFIABLE]; do not use it.

Braking needs eccentric capacity of the quadriceps and posterior chain. Good early braking leaves the final plant free to act as a propulsive lever [OPINION].

### Kinematic Markers to Monitor
- Controlled lowering of the center of mass in the steps leading into the braking action.
- Positive tibia angle: a sharp shin inclination toward the exit direction, to project the force vector horizontally.
- Trunk lean consistent with the exit vector.
- No knee valgus collapse (an ACL risk factor).

## The Big Three Cuts

### Speed Cut
Used to accelerate through open space without losing speed. Principle: exit faster than you entered. Executed by planting the foot firmly outside the body's framework, creating the lever to redirect weight without decelerating. The reference metric is not the 40-yard dash but the 10-yard split: a runner who uses the speed cut well looks faster on the field than his stopwatch time would suggest.

### Jump Cut
A 90-degree lateral shift used when there's no room for the feet (a collapsed line of scrimmage). Requires literally lifting the cleats off the ground to shift the entire body into an adjacent gap. Sacrifices forward momentum to gain immediate lateral displacement — it's the "reset button" when the initial hole has closed.

### Pressure Step (Hesitation/Hesi)
The art of manipulation in one-on-one situations. Three-phase mechanics: (1) Load — load the weight onto the outside leg while approaching the defender; (2) Shimmy — a tilt of the head and shoulders to deceive the defender's visual attention, freezing his feet; (3) Explode — drive off the loaded leg to accelerate in the opposite direction once the defender is locked in.

### Decision Matrix

| Cut type | Ideal situation | Key benefit |
|---|---|---|
| Speed Cut | Space available between runner and defender | Maintains/builds momentum, eliminates pursuit angles |
| Jump Cut | Crowded line, defensive penetration, no room for the feet | Immediate lateral displacement |
| Pressure Step | One-on-one in open space | Manipulates the defender's tackling surface |

## Vision and Field Reading

Cutting technique is useless without vision. The elite athlete reads "the level beyond the level": not just the offensive line but the second-level defenders. When a linebacker abandons his position to chase a play-fake, a void is created that must be attacked immediately, rather than mechanically following the path prescribed by the scheme.

### Avoiding the "Fool's Gold"
A common mistake is attacking the first gap that appears open. A gap may look free but hide an unblocked defender right behind it. The correct technique is to "press the hole": run toward the line to draw the linebacker in, then execute the jump cut toward the true open lane.

## Integration with Contact Balance

Keeping the hips squared to the line of scrimmage for as long as possible makes the athlete unreadable to the defense, keeping all three cuts available until the last millisecond. Patience (waiting for blocks to develop) and contact balance (staying on your feet through contact) are complementary to the quality of the footwork.

## Progression Order (COD)

[OPINION]
1. Slow-speed directional markers (cone walks)
2. Deceleration + cut (no sprint out)
3. COD with sprint out to 5 m
4. Reactive COD (light cue, mirror drill)
5. Ball in hand / sport-specific application

## Common RB-Specific Faults

[OPINION]

| Fault | Cause | Correction |
|---|---|---|
| Rounding the cut | Insufficient deceleration before plant | Reduce approach speed, brake earlier over the last 2–3 steps |
| Early hip sink | No horizontal drive out of cut | Hip thrust strength, cue "drive out not down" |
| Arm drift | Arms cross midline during cut | Arm mechanics drill, compact 90° elbow cue |

## Reference Drills

- **Line Response Drill**: quick feet on a fixed line, for neural reaction frequency.
- **Sweep Drill**: weaving between cones while receiving the ball, always transferring it to the side opposite the simulated defender — automates ball security during lateral movement.
- **Cone Hops**: single-leg lateral hops over two cones followed by a 5-yard burst, for the explosive transition from lateral power to linear acceleration.

## References

- Dos'Santos T, Thomas C, Jones PA. 2021. J Sports Sci. doi:10.1080/02640414.2020.1823130

Change-of-direction biomechanics also draws on: braking-step principles from athletic development literature; tibia angle and GRF management (force-dissipation framework); the Big Three cuts taxonomy (Speed Cut, Jump Cut, Pressure Step) as operationalized in elite RB coaching; and sports-vision decision-making frameworks (e.g., anticipation training and defensive prediction models). Core sources: athletic biomechanics consensus (ACSM, NSCA), football coaching kinetics, and elite-sport vision research.

## Scope

Skill dedicated to COD and footwork for football/RB. For the general overview of the role use `football-rb-system`. For programming governance use `programming-audit-council`. For tendon architecture (stiffness, RFD) use `tendon-power-architecture`.
