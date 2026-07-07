---
name: literature-lookup
description: "On-demand retrieval of primary sports-science / sports-medicine literature to support or check a recommendation, via a connected research tool (e.g., a PubMed / ClinicalTrials MCP) when available; falls back to naming the framework/guideline when no such tool is connected."
compatibility: "Amp (.agents/skills, ~/.config/agents/skills) and Claude Code (~/.claude/skills)"
argument-hint: [evidence, literature, research, pubmed, study, claim verification]
---

# Literature Lookup

## When to use

- An athlete or coach asks: "What's the evidence for this recommendation?"
- A claim needs to be checked against published research before acting on it
- A specific condition or intervention lacks sourced guidance and primary literature would help
- A recommendation conflicts with an athlete's prior experience, and literature can clarify the state of evidence

## How to query

Structure the query with three elements:

1. **Condition / problem**: e.g., "MTSS management", "female athlete menstrual dysfunction", "velocity-based training for RFD"
2. **Intervention**: e.g., "soleus eccentric loading", "oral contraceptives", "accommodating resistance"
3. **Population**: e.g., "running backs", "distance runners", "strength athletes"

Example query: "soleus eccentric strengthening for MTSS management in American football players"

## How to cite what it finds

- **Real study**: title, authors (first author + et al. if >3), year, journal. Do NOT invent DOIs, authors, or publication venues.
- **Framework/guideline**: name it explicitly (e.g., "ACSM RED-S screening guidelines", "Copenhagen adduction protocol literature")
- **No result found**: state it clearly: "No matched studies found for this specific population, but the framework is [named framework]."

**Explicit rule:** if no research tool is connected, or if a search returns nothing, SAY SO. Never fabricate a citation, author name, or year. Named frameworks are fine; invented studies are not.

## If a connected research tool is available

Use it to pull PubMed, ClinicalTrials.gov, or equivalent. Return the most relevant 3-5 results, ranked by relevance to the query.

## If no research tool is connected

Name the relevant framework, guideline, or known consensus position instead. Example:
> "No literature tool is available in this environment. The evidence base for soleus work in MTSS management comes from: (1) biomechanics literature on tibial load distribution, (2) APTA clinical practice guidelines for MTSS, and (3) the Copenhagen adduction protocol framework, which applies to groin injury but shares the eccentric-loading principle."

## Integration with the system

Cross-reference `elite-sc-system` and any domain skill. This skill is a lookup tool, not a generator; it answers "what does the research say?" not "what should the athlete do?"

## Scope

On-demand evidence retrieval. For programming logic use `programming-audit-council`. For clinical decisions use `clinical-prehab-system`. For sport-specific claims use the corresponding domain skill.

## References

Sports-science and sports-medicine primary literature, accessed through PubMed, Google Scholar, ClinicalTrials.gov, or equivalent research databases. The skill is a retrieval and citation interface, not itself a source. Real citations only — frameworks named explicitly, invented sources never.
