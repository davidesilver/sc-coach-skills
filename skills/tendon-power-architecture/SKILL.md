---
name: tendon-power-architecture
description: "Tendon biomechanics and power development skill. Covers the evidence-based isometric loading protocol for tendon adaptation, why plyometrics alone is a weak tendon stimulus, the muscle-specific stiffness/compliance picture, eccentric overload, total body tension (G.L.A.G.S.), and foot mechanics for power-speed athletes."
compatibility: "Amp (.agents/skills, ~/.config/agents/skills) and Claude Code (~/.claude/skills)"
argument-hint: [tendon stiffness, isometrics, eccentric overload, RFD]
---

# Tendon Power Architecture

**Evidence tags.** Every number carries `[Source Year, doi, grade]`. Grades: VERIFIED (verbatim in the source; "abstract" when only the abstract was read), UNVERIFIABLE, OPINION (coaching practice), C (internal rule). Audit: 2026-10-08.

## Mission

The tendon is the transmission, the muscle is the engine. Tendon stiffness is associated with how fast force rises: tendon mechanical properties "may account for up to 30% of the variance" in rate of torque development [Bojsen-Møller 2005, doi:10.1152/japplphysiol.01305.2004, abstract, VERIFIED]. It is one factor, not the determinant.

## Functions of the tendon

Energy storage and return in the stretch-shortening cycle, power amplification, and power absorption during sudden stops [textbook mechanism, OPINION in this skill: not graded against a primary source].

## Stiffness vs compliance: muscle-specific, not athlete-type

There is no simple "stiff = sprinter, compliant = endurance" rule:
- In sprinters, "the tendon structures of VL are more compliant than that for controls at low force production levels", and "the compliance of VL was negatively correlated to 100-m sprint time" [Kubo 2000, doi:10.1046/j.1365-201x.2000.00653.x, abstract, VERIFIED].
- The most economical runners showed "a higher normalised tendon stiffness ... in the triceps surae MTU and a higher compliance of the quadriceps tendon" [Arampatzis 2006, doi:10.1242/jeb.02340, abstract, VERIFIED].

Rule: decide per muscle-tendon unit and per task. Do not ban compliance work for a running back.

## Isometric loading for tendon adaptation

The tendon needs "a high strain magnitude, an appropriate strain duration and repetitive loading" [Bohm 2014, doi:10.1242/jeb.112268, full text, VERIFIED]. Longer strain duration per contraction "leads to superior tendon adaptational responses" [Arampatzis 2010, doi:10.1016/j.jbiomech.2010.08.014, abstract, VERIFIED].

**Tested protocol** (triceps surae, knee extended) [Arampatzis 2007, doi:10.1242/jeb.003814, full text, VERIFIED]:
- 5 sets of 4 repetitions, 3 s loading + 3 s relaxation;
- about 90% of maximal voluntary contraction;
- 4 sessions per week;
- 14 weeks.

The meta-analysis lists the same protocol ("90% MVC | 3 s | 4 | 5 | 14 | 4") and notes that "longer durations (≥12 weeks) seem to be more efficient" [Bohm 2015, doi:10.1186/s40798-015-0009-9, full text, VERIFIED].

Practical lower doses (for example 2 sessions per week alongside field training) are a coaching compromise with less evidence [OPINION].

**Plyometrics.** "Plyometric training using jumps does not provide an optimal mechanical stimulus for tendon adaptation compared with training using longer durations of repetitive loading" [Bohm 2014, full text, VERIFIED]. Keep plyometrics for the stretch-shortening skill, not as the main tendon stimulus.

**Not verified:** gains in "type I collagen quality" (the studies above measure stiffness, modulus and cross-sectional area) [UNVERIFIABLE]; the idea that too much isometric work "over-stiffens" the system and hurts the force-time curve [OPINION]. Balance isometrics with ballistic work [OPINION].

## Eccentric overload

Supra-maximal eccentrics (around 120% of 1RM, controlled lowering of a load the athlete cannot lift concentrically) to prepare for force absorption [OPINION, no primary source checked]. Advanced-phase tool only: not for deconditioned athletes or the first weeks of a block [C].

### Reference lifts
[OPINION]
1. **Two-Box Cleans**: the catch trains stabilization under sudden load.
2. **High Bar Squat**: vertical force production.
3. **RDL**: posterior chain for the first steps of acceleration.

## Total body tension — G.L.A.G.S.

[OPINION, coaching cue]

Activation sequence for a stable platform: **G**rip → **L**ats → **A**bs → **G**lutes → **S**caps.
- Grip: squeezing the bar stabilizes the shoulder.
- Lats: link the upper body and the pelvis.
- Abs: intra-abdominal pressure for force transfer.
- Glutes: hip drive and stability.
- Scaps: shoulder-blade stability in pressing and pulling.

## Foot mechanics

"Short foot" arch activation and barefoot or minimal-shoe work for foot proprioception [OPINION]. A link to ACL protection in lateral cuts is not established: only one study on women with dynamic valgus was found [UNVERIFIABLE for football cutting].

## References

- Arampatzis A et al. 2006. J Exp Biol 209:3345–57. doi:10.1242/jeb.02340
- Arampatzis A, Karamanidis K, Albracht K. 2007. J Exp Biol 210:2743–53. doi:10.1242/jeb.003814
- Arampatzis A et al. 2010. J Biomech 43:3073–9. doi:10.1016/j.jbiomech.2010.08.014
- Bohm S et al. 2014. J Exp Biol 217:4010–7. doi:10.1242/jeb.112268
- Bohm S, Mersmann F, Arampatzis A. 2015. Sports Med Open 1:7. doi:10.1186/s40798-015-0009-9
- Bojsen-Møller J et al. 2005. J Appl Physiol 99:986–94. doi:10.1152/japplphysiol.01305.2004
- Kubo K et al. 2000. Acta Physiol Scand 168:327–35. doi:10.1046/j.1365-201x.2000.00653.x

## Scope

Skill dedicated to tendon adaptation and power architecture. For the football/RB framework use `football-rb-system`. For velocity-based training use `vbt-rfd-open-sets`. For clinical care and prevention use `clinical-prehab-system`.
