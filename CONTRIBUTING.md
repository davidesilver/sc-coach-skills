# Contributing to sc-coach-skills

## Proposing a new sport-specific skill

Right now the pack covers powerlifting, Olympic weightlifting, football/RB, HYROX/hybrid, and general population. Missing on purpose: throwing events (shot put, javelin), youth/adolescent athletic development, pure endurance (non-hybrid marathon/triathlon), combat sports. Not an editorial choice — I just didn't have verified sources for them when I wrote this.

To propose one:
1. Open an issue with the "New skill request" template: sport/domain, and the sources you'd actually use.
2. Match the structure of the existing skills (`skills/<name>/SKILL.md`) — frontmatter with `name` matching the folder and a `description` that states when it should activate, then a body with a mission, concrete protocols/tables, and a "Scope" section pointing at whatever other skills it works with.
3. No real athlete data, ever. Generic frameworks only.

## Correcting an existing skill

Open an issue with the "Correction" template, or just send a PR. If your fix touches a cross-reference to another skill (something like `` `skill-name` `` in the text), double-check that name still exists under `skills/`.

## Before opening a PR

```bash
bash scripts/validate-skills.sh
```

It needs to pass clean: it checks that every `SKILL.md`'s frontmatter is consistent (folder name matches `name`, `description` isn't empty) and flags any reference to a skill that no longer exists — which tends to happen after a rename or a merge. The same check runs in CI on every push and PR.
