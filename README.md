# sc-coach-skills: a Strength & Conditioning coach for Claude

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Validate skills](https://github.com/davidesilver/sc-coach-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/davidesilver/sc-coach-skills/actions/workflows/validate.yml)
![Skills: 20](https://img.shields.io/badge/skills-20-blue.svg)
![Format: Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-orange.svg)

**A Strength & Conditioning coach for Claude that refuses to program without data and stops when something hurts.**

sc-coach-skills is an open-source pack of 20 Claude Agent Skills. Together they cover the full coaching cycle: intake, clinical screening, periodization, weekly programming governance, and sport-specific programming for powerlifting, Olympic weightlifting, American football (running back), hybrid/HYROX athletes, and general population fitness.

No real athlete data lives in this repository. Every skill is a generic, reusable methodology, and every number in it is tagged with how well it was checked (see [Where this comes from](#where-this-comes-from-and-why-you-should-trust-it)).

## Install in 1 command

```bash
npx skills add davidesilver/sc-coach-skills
```

Then, in any conversation with an agent that supports Agent Skills (Claude Code, Amp, and others):

```
Use coach-builder-router to build my S&C coach
```

`coach-builder-router` asks one profiling question and assembles the right skill stack for your case.

## What a session looks like

This is an illustrative example of the flow, not a transcript of a real athlete.

```
You:    Use coach-builder-router to build my S&C coach.
Claude: What are you training for: powerlifting, Olympic weightlifting, football,
        HYROX/hybrid, or general fitness?
You:    HYROX, first race in four months.
Claude: Loading the hybrid stack. Before I write anything I need four things:
        readiness, current maxes, clinical flags, and a stated goal.
        Start with clinical flags: any pain, injury, or medical history I should know?
You:    My left knee is sore after long runs.
Claude: That goes through the clinical filter first. I will not progress running
        volume until the knee is assessed. Here is what I can do now: ...
```

The order matters. The intake is a hard prerequisite, and a pain flag changes the plan before any load is prescribed.

## How the skills fit together

```
coach-builder-router (entry point, profiles the athlete)
        │
        ▼
athlete-profiling-benchmarking + biomechanics-movement-screen   (assessment: no data, no program)
        │
        ▼
periodization-block-planner + programming-audit-council          (governance: macrocycle + weekly 3-judge audit)
        │
        ▼
sport-specific domain skill                                       (powerlifting / weightlifting / football-RB / HYROX / general population)
        │
        ▼
energy-systems-recovery + clinical-prehab-system + vbt-rfd-open-sets   (cross-cutting: recovery, clinical filter, autoregulation)
```

Each skill's `SKILL.md` says when it should activate and which skills it works alongside, so there is nothing to wire up by hand.

Plans can be delivered as CSV (the default), Excel, Markdown, or PDF. You pick the format once at the start. For female athletes, the stack adds `female-athlete-programming`, which handles menstrual-cycle-aware load modulation and RED-S screening.

## What makes this different from a generic AI coaching prompt

Three rules hold across the whole pack, and none of them are optional.

1. Load is never prescribed without an intake. `athlete-profiling-benchmarking` is a hard prerequisite: no v1 program gets written until readiness, maxes, clinical flags, and a stated goal exist.
2. Pain outranks the calendar. The clinical filter in `clinical-prehab-system` (Sanford soreness rules, Copenhagen protocol) stops progression however motivated the athlete feels.
3. Every week gets audited. `programming-audit-council` runs three internal judges (Strength Science, Sport-Specific, Clinical/Prehab) before a v2 goes out.

Loads are autoregulated. RPE, RIR, and VBT (`vbt-rfd-open-sets`) drive the numbers, and programming shifts as recovery markers come in.

## Where this comes from, and why you should trust it

Anything that touches an athlete's body deserves scrutiny, so here is how the pack was built.

The core framework started from one real athlete's own S&C dossier, a competitive American football running back. I generalized it and checked it against published sports science: the Sanford MTSS guideline and soreness rules, the Copenhagen adduction trials, tendon-loading research, energy-system physiology, velocity-based training research, and the official HYROX rulebook. Each skill lists its sources at the bottom of its `SKILL.md`.

Part of the research was done with AI tools: Perplexity to find sources, NotebookLM to organize them. Those summaries were sometimes wrong. In October 2026 I re-checked every factual claim against the original texts (full text where open, otherwise the verbatim abstract or the official rulebook). Wrong numbers were corrected or removed. Every number that remains carries a tag in the form `[Source Year, doi, grade]`:

- VERIFIED: the passage is quoted verbatim from the source ("abstract" when only the abstract was read).
- UNVERIFIABLE: no original text supports it. Kept only as a warning, never as a prescription.
- OPINION: coaching practice that is useful but untested.
- C: an internal rule of this skill set (governance, not science).

This is educational and methodological content, not medical advice, and it does not replace an in-person assessment by a qualified coach or clinician. Every skill hands off to a human when pain, injury, or any medical red flag shows up. Before you apply a specific number or protocol to a real athlete, check it against the cited source.

## Package structure

Skills live in `skills/<name>/SKILL.md`, a flat layout compatible with [skills.sh](https://www.skills.sh/) discovery and with Claude Code and Amp.

| # | Skill | Level | Target profile |
|---|---|---|---|
| 0 | `coach-builder-router` | Entry point | Everyone, routes to the correct profile |
| 1 | `elite-sc-system` | Always-on base | Everyone |
| 2 | `programming-audit-council` | Governance | Everyone |
| 3 | `athlete-profiling-benchmarking` | Assessment | Everyone |
| 4 | `powerlifting-peaking-system` | Sport-specific domain | Powerlifter |
| 5 | `olympic-weightlifting-technique` | Technical domain | Olympic weightlifter |
| 6 | `football-rb-system` | Sport-specific domain | Football / RB |
| 7 | `football-cod-footwork` | Technical domain | Football / RB |
| 8 | `tendon-power-architecture` | Biomechanical domain | Power/speed athletes |
| 9 | `vbt-rfd-open-sets` | Methodological domain | Advanced athletes (any profile) |
| 10 | `clinical-prehab-system` | Clinical domain | Football, power athletes |
| 11 | `energy-systems-recovery` | Physiological domain | Football, HYROX |
| 12 | `hyrox-hybrid-system` | Sport-specific domain | Hybrid / HYROX athletes |
| 13 | `general-population-fitness` | General population domain | Non-athletes / fitness clients |
| 14 | `periodization-block-planner` | Macrocycle governance | Everyone (Block/Linear/DUP/Conjugate model choice) |
| 15 | `biomechanics-movement-screen` | Clinical/assessment domain | Everyone (6-pattern FMS screening) |
| 16 | `exercise-library-video` | Output domain | Everyone (exercise naming, video-link standards for program export) |
| 17 | `female-athlete-programming` | Physiological domain | Female athletes (menstrual-cycle modulation, RED-S screening) |
| 18 | `council-escalation` | Decision escalation | High-stakes decisions (return-to-run, peak-vs-extend, goal conflicts, first macrocycle) |
| 19 | `literature-lookup` | Evidence retrieval | Everyone (on-demand literature for claims verification) |

## Recommended stacks by profile

Skills in each stack are listed in the order they come into play.

- Powerlifter: `coach-builder-router`, `elite-sc-system`, `athlete-profiling-benchmarking`, `biomechanics-movement-screen`, `periodization-block-planner`, `programming-audit-council`, `powerlifting-peaking-system`, `vbt-rfd-open-sets`, `tendon-power-architecture`
- Olympic weightlifter: `coach-builder-router`, `elite-sc-system`, `athlete-profiling-benchmarking`, `periodization-block-planner`, `programming-audit-council`, `olympic-weightlifting-technique`, `vbt-rfd-open-sets`, `tendon-power-architecture`
- Football/RB: `coach-builder-router`, `elite-sc-system`, `athlete-profiling-benchmarking`, `biomechanics-movement-screen`, `periodization-block-planner`, `programming-audit-council`, `football-rb-system`, `football-cod-footwork`, `tendon-power-architecture`, `clinical-prehab-system`, `vbt-rfd-open-sets`
- Hybrid/HYROX athlete: `coach-builder-router`, `elite-sc-system`, `athlete-profiling-benchmarking`, `periodization-block-planner`, `programming-audit-council`, `hyrox-hybrid-system`, `energy-systems-recovery`, `vbt-rfd-open-sets`
- General population: `coach-builder-router`, `elite-sc-system` (simplified), `biomechanics-movement-screen`, `general-population-fitness`

## Coverage and stated limits

Covered with verified sources: football/RB, COD/footwork, tendon/RFD, VBT/open sets, clinical/prehab (Sanford, Copenhagen), HYROX/hybrid training (physiological thresholds, HR zones, Brick protocol, technique cues for all 8 stations, Open/Pro benchmarks), bioenergetics/recovery (energy systems, RSA protocols, creatine, elite recovery stack), profiling/assessment (NFL-style interview, ordered test battery, neuromuscular profiling, deconditioned-athlete rule), movement screening (FMS 6-pattern), macrocycle periodization (Block/Linear/DUP/Conjugate), powerlifting (RTS block model, peaking, tapering), Olympic weightlifting (technical phases, early-arm-bend correction), and general population (NSCA movement patterns).

Left out of this version because I did not have verified sources solid enough when I wrote it: throwing events (shot put, javelin), youth and adolescent athletic development, pure endurance (non-hybrid marathon and triathlon), and combat sports. If you can fill one of those gaps properly, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Frequently asked questions

**Does this replace a real coach?** No. It is a methodology layer for an AI agent that makes programming more rigorous and evidence-based. It does not replace in-person coaching, physical therapy, or a medical evaluation. The clinical gates exist to send pain and injury flags to a human.

**Which agents can run these skills?** Anything that supports the Agent Skills format (`SKILL.md` with YAML frontmatter), including Claude Code and Amp. Install with `npx skills add davidesilver/sc-coach-skills`, or add the repo as a Claude Code plugin through `.claude-plugin/plugin.json`.

**Can I use this on a real athlete?** Yes, as a programming and governance framework, with human oversight: you as the coach, or a qualified professional. Do not override the clinical-gate rules in `clinical-prehab-system` and `athlete-profiling-benchmarking`.

**Where do the numbers and protocols come from?** Published sources, listed in each `SKILL.md` under "References" and tagged inline with their evidence grade. See [Where this comes from](#where-this-comes-from-and-why-you-should-trust-it) for how the research was put together.

**Can I add a sport or population the pack does not cover?** Yes. See [Coverage and stated limits](#coverage-and-stated-limits) and [CONTRIBUTING.md](CONTRIBUTING.md).

## Complementary tools

- `notion/`: an importable Notion database template for tracking athletes, weekly programming, and feedback sheets.
- `data/`: a MotherDuck/DuckDB-compatible SQL schema for analyzing training logs over time.
- `scripts/validate-skills.sh`: checks frontmatter and cross-references between skills before every commit or PR. CI runs it too.

## Compatibility

Every `SKILL.md` has a YAML header compatible with Amp (`.agents/skills`, `~/.config/agents/skills`) and Claude Code (`~/.claude/skills`, or as a plugin via `.claude-plugin/plugin.json`). The `skills/<name>/SKILL.md` layout follows the discovery standard used by [skills.sh](https://www.skills.sh/) (the `vercel-labs/skills` CLI), which looks for skills inside a `skills/` folder rather than at the repo root.

## License

MIT. See [LICENSE](LICENSE).

*Last updated: October 2026.*
