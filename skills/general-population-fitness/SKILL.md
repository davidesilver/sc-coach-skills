---
name: general-population-fitness
description: "General population program design skill based on NSCA guidelines. Covers the 10 fundamental movement patterns, needs analysis, safe progressive overload for non-athletes, facility/equipment considerations, and adherence-focused coaching for fitness/health-oriented clients."
compatibility: "Amp (.agents/skills, ~/.config/agents/skills) and Claude Code (~/.claude/skills)"
argument-hint: [general population, beginner client, fitness goal, movement pattern]
---

# General Population Fitness

## Missione

Un cliente non-atleta non ha bisogno di essere trattato come un atleta d'élite in miniatura. L'obiettivo primario è aderenza sostenibile, sicurezza, e progresso verso obiettivi di salute/composizione corporea, non massimizzazione della performance competitiva.

## I 10 pattern di movimento fondamentali (NSCA)

Secondo le linee guida NSCA per la programmazione della popolazione generale, un programma completo deve coprire un set di pattern di movimento fondamentali che rispecchiano le esigenze motorie della vita quotidiana, non solo dei pattern da sala pesi [web:56]. Questo approccio garantisce che il cliente sviluppi capacità funzionale trasferibile, non solo numeri su singoli esercizi isolati.

Nel costruire un programma per popolazione generale, verifica sempre la copertura di: pattern di spinta orizzontale e verticale, pattern di trazione orizzontale e verticale, pattern di squat, pattern di hinge (cerniera d'anca), pattern di locomozione, pattern di rotazione/anti-rotazione core, pattern di carry/trasporto carico [web:56].

## Differenze rispetto alla programmazione per atleti

| Dimensione | Atleta competitivo | Popolazione generale |
|---|---|---|
| Obiettivo primario | Performance/transfer sport-specifico | Salute, aderenza, composizione corporea |
| Tolleranza al rischio | Più alta, giustificata da performance | Bassa, priorità a sicurezza |
| Intensità (RPE/RIR) | Spinta fino a RPE 8-10 in fasi mirate | Generalmente RPE 6-8, raramente al limite |
| Complessità tecnica | Alta (Olympic lifts, sprint, COD) | Progressiva, semplificata dove serve |
| Monitoraggio | VBT, RPE, benchmark di campo | Aderenza, feedback soggettivo, progressione lineare semplice |

## Progressive overload sicuro

Per clienti generici il principio di sovraccarico progressivo va applicato con margini di sicurezza più ampi rispetto a un atleta competitivo: incrementi di carico piccoli e frequenti, priorità alla qualità tecnica prima dell'incremento di carico, e attenzione a segnali di affaticamento non giustificati dal volume prescritto.

## Considerazioni di sicurezza in palestra (NSCA facility guidelines)

Per chi programma o gestisce l'ambiente di allenamento, alcune linee guida NSCA su spazio e sicurezza sono rilevanti anche per il coaching individuale [web:53]:
- Esercizi che richiedono spotter vanno collocati lontano da finestre, specchi e porte per evitare distrazioni.
- Nell'area di sollevamento pesi liberi, mantenere spazio sufficiente tra le attrezzature (2-3 piedi) per movimenti sicuri.
- L'area di stretching richiede 40-60 piedi quadrati per utente.
- Considerare sempre l'accessibilità e la sicurezza dell'ambiente, specialmente per clienti meno esperti che potrebbero non avere familiarità con la disposizione della sala pesi.

## Struttura di sessione per cliente generico

1. Riscaldamento generale e attivazione (più breve e meno specifico rispetto a un atleta).
2. Pattern fondamentali principali (2-4 esercizi multiarticolari coprendo push/pull/squat/hinge).
3. Lavoro accessorio mirato all'obiettivo specifico (ipertrofia, dimagrimento, capacità funzionale).
4. Componente cardiovascolare se richiesta dall'obiettivo.
5. Mobilità/defaticamento.

## Adesione come priorità strategica

Per la popolazione generale, il fattore predittivo più forte di successo a lungo termine non è la sofisticazione del programma ma la sostenibilità dell'aderenza. Regole pratiche:
- Preferire una programmazione semplice ma costante rispetto a una complessa ma difficile da seguire.
- Adattare frequenza e volume al tempo realmente disponibile del cliente, verificato tramite intake (vedi `athlete-profiling-benchmarking` per la struttura dell'intervista, adattata a contesto non agonistico).
- Costruire piccole vittorie iniziali per rinforzare la motivazione, prima di aumentare complessità o intensità.

## Quando la popolazione generale converge verso metodologie da atleta

Alcuni clienti generici con obiettivi specifici (dimagrimento aggressivo, ricomposizione corporea avanzata, preparazione a eventi come gare amatoriali) possono beneficiare di elementi presi da skill più specialistiche: RPE/RIR strutturato e VBT base (`vbt-rfd-open-sets`), logica di periodizzazione a blocchi semplificata (`programming-audit-council`), o principi di allenamento ibrido se l'obiettivo è una gara tipo HYROX amatoriale (`hyrox-hybrid-system`).

## Scope

Skill dedicata a clienti non-atleti e popolazione generale. Per fondamenti biomeccanici trasversali usa `elite-sc-system`. Per clienti che si avvicinano a obiettivi competitivi usa le skill specialistiche corrispondenti.
