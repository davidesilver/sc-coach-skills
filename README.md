# sc-coach-skills — Strength & Conditioning AI coach skill pack for Claude

sc-coach-skills is an open-source pack of 18 Claude Agent Skills that turns Claude into a Strength & Conditioning (S&C) coach. It covers the full coaching cycle — intake, clinical screening, periodization, weekly programming governance, and sport-specific programming — for powerlifting, Olympic weightlifting, American football (running back), hybrid/HYROX athletes, and general population fitness.

No real athlete data lives in this repository. Every skill is a verified, generic, reusable methodology, not anyone's personal training log.

## Quickstart

```bash
npx skills add davidesilver/sc-coach-skills
```

Then, in any conversation with your agent (Claude Code, Amp, or any harness that supports Agent Skills):

```
Use coach-builder-router to build my S&C coach
```

`coach-builder-router` asks one profiling question and assembles the right skill stack for your case automatically.

## How does it work?

```
coach-builder-router (entry point, profiles the athlete)
        │
        ▼
athlete-profiling-benchmarking + biomechanics-movement-screen   (assessment: never program without data)
        │
        ▼
periodization-block-planner + programming-audit-council          (governance: macrocycle + weekly 3-judge audit)
        │
        ▼
sport-specific domain skill                                       (powerlifting / weightlifting / football-RB / HYROX / general population)
        │
        ▼
energy-systems-recovery + clinical-prehab-system + vbt-rfd-open-sets   (cross-cutting layers: recovery, clinical filter, autoregulation)
```

Each skill's `SKILL.md` states on its own when it should activate and which other skills it works alongside, so there's nothing to wire up manually.

**Program delivery:** Plans can be generated in CSV (default), Excel, Markdown, or PDF format — your choice, set once at the start. **Female athletes:** the stack includes `female-athlete-programming` for menstrual-cycle-aware load modulation and RED-S screening.

## What makes this different from a generic AI coaching prompt?

A few rules hold across the whole pack, and none of them are optional.

Load never gets prescribed without an intake first. `athlete-profiling-benchmarking` is a hard prerequisite: no v1 program gets written until four things exist — readiness, maxes, clinical flags, and a stated goal. Pain outranks everything else, too. The clinical filter in `clinical-prehab-system` (Sanford Soreness Rules, Copenhagen protocol) stops progression regardless of how motivated the athlete feels or what the calendar says.

Loads are autoregulated, not pulled from a spreadsheet someone wrote three weeks ago. RPE, RIR, and VBT (`vbt-rfd-open-sets`) drive the actual numbers, and programming shifts with recovery markers as they come in. And the governance is explicit: `programming-audit-council` runs every week through three internal judges — Strength Science, Sport-Specific, Clinical/Prehab — before a v2 ever goes out.

## Where this comes from, and why you should trust it

Anything touching an athlete's body and health deserves scrutiny, so here's exactly how this pack got built.

The core framework started from one real athlete's own S&C dossier — a competitive American football running back — then got generalized and checked against published sports-science literature: RTS block periodization, NSCA movement-pattern guidelines, the Sanford Soreness Rules, the Copenhagen adduction protocol, velocity-based training research, and combine/positional benchmark data. Every skill lists its specific sources at the bottom of its `SKILL.md`, so nothing here is unsourced.

Part of the research — searching and synthesizing existing literature — was done with AI tools: Perplexity for finding sources, NotebookLM for organizing them. Those tools didn't generate any claims; they helped find and summarize what's already published, and everything they surfaced was reviewed before being structured into a skill. This gets said out loud rather than left unmentioned, because in a domain like this one, being upfront about method is part of being trustworthy, not a liability.

One more thing worth being direct about: this is educational and methodological content, not medical advice, and it doesn't replace an in-person assessment by a qualified coach or clinician. Every skill hands off to a human the moment pain, injury, or any medical red flag shows up. If you're going to apply a specific number or protocol to a real athlete, check it against the source cited for it first.

## Package structure

Skills live in `skills/<name>/SKILL.md` (flat layout, compatible with [skills.sh](https://www.skills.sh/) discovery and with Claude Code / Amp).

| # | Skill | Level | Target profile |
|---|---|---|---|
| 0 | `coach-builder-router` | **Entry point** | Everyone — routes to the correct profile |
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

## Recommended stacks by profile

**Powerlifter**: `coach-builder-router` → `elite-sc-system` → `athlete-profiling-benchmarking` → `biomechanics-movement-screen` → `periodization-block-planner` → `programming-audit-council` → `powerlifting-peaking-system` → `vbt-rfd-open-sets` → `tendon-power-architecture`

**Olympic weightlifter**: `coach-builder-router` → `elite-sc-system` → `athlete-profiling-benchmarking` → `periodization-block-planner` → `programming-audit-council` → `olympic-weightlifting-technique` → `vbt-rfd-open-sets` → `tendon-power-architecture`

**Football/RB**: `coach-builder-router` → `elite-sc-system` → `athlete-profiling-benchmarking` → `biomechanics-movement-screen` → `periodization-block-planner` → `programming-audit-council` → `football-rb-system` → `football-cod-footwork` → `tendon-power-architecture` → `clinical-prehab-system` → `vbt-rfd-open-sets`

**Hybrid/HYROX athlete**: `coach-builder-router` → `elite-sc-system` → `athlete-profiling-benchmarking` → `periodization-block-planner` → `programming-audit-council` → `hyrox-hybrid-system` → `energy-systems-recovery` → `vbt-rfd-open-sets`

**General population**: `coach-builder-router` → `elite-sc-system` (simplified) → `biomechanics-movement-screen` → `general-population-fitness`

## Coverage and stated limits

Covered with verified sources: football/RB, COD/footwork, tendon/RFD, VBT/open sets, clinical/prehab (Sanford, Copenhagen), HYROX/hybrid training (physiological thresholds, HR zones, Brick protocol, technique cues for all 8 stations, Open/Pro benchmarks), bioenergetics/recovery (energy systems, RSA protocols, creatine, elite recovery stack), profiling/assessment (NFL-style interview, ordered test battery, neuromuscular profiling, deconditioned-athlete rule), movement screening (FMS 6-pattern), macrocycle periodization (Block/Linear/DUP/Conjugate), powerlifting (RTS block model, peaking, tapering), Olympic weightlifting (technical phases, early-arm-bend correction), general population (NSCA movement patterns).

Left out of this version, simply because I didn't have verified sources solid enough at the time of writing: throwing events (shot put, javelin), youth/adolescent athletic development, pure endurance (non-hybrid marathon/triathlon), combat sports. If you can fill one of those gaps properly, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Frequently asked questions

**Is this a replacement for a real coach?** No. It's a methodology layer for an AI agent that makes programming more rigorous and evidence-based — it doesn't replace in-person coaching, physical therapy, or a medical evaluation. The clinical gates built into it exist specifically to route pain and injury flags to a human.

**Which agents or tools can run these skills?** Anything that supports the Agent Skills format (`SKILL.md` with YAML frontmatter), Claude Code and Amp included. Install with `npx skills add davidesilver/sc-coach-skills`, or add the repo as a Claude Code plugin through `.claude-plugin/plugin.json`.

**Can I actually use this on a real athlete?** Yes, as a programming and governance framework, but keep human oversight in the loop — yourself as coach, or a qualified professional — and don't override the clinical-gate rules in `clinical-prehab-system` and `athlete-profiling-benchmarking`.

**Where do the numbers and protocols come from?** Published, checkable sources, listed per skill under each `SKILL.md`'s "References" section. See [Where this comes from](#where-this-comes-from-and-why-you-should-trust-it) above for how the research itself was put together.

**Can I add a sport or population this pack doesn't cover yet?** Yes — see [Coverage and stated limits](#coverage-and-stated-limits) and [CONTRIBUTING.md](CONTRIBUTING.md) for how to propose one.

## Complementary tools

- `notion/` — importable Notion database template for tracking athletes, weekly programming, and feedback sheets.
- `data/` — MotherDuck/DuckDB-compatible SQL schema for quantitative analysis of training logs over time.
- `scripts/validate-skills.sh` — validates frontmatter and cross-references between skills before every commit/PR (also run in CI).

## License

MIT — see [LICENSE](LICENSE).

## Compatibility

Every `SKILL.md` includes a YAML header compatible with Amp (`.agents/skills`, `~/.config/agents/skills`) and Claude Code (`~/.claude/skills`, or as a plugin via `.claude-plugin/plugin.json`). The `skills/<name>/SKILL.md` layout follows the discovery standard used by [skills.sh](https://www.skills.sh/) (the `vercel-labs/skills` CLI), which looks for skills inside a `skills/` folder (flat or catalog layout) rather than directly at the repo root.

---
*Last updated: July 2026.*
