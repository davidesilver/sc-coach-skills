---
name: coach-builder-router
description: "Master routing skill. Use this FIRST to build a personalized S&C coach for any athlete profile (powerlifter, weightlifter, football/RB, HYROX/hybrid, general population). Runs a short intake, maps the athlete to the correct skill stack from this repository, and defines the operating sequence for programming."
compatibility: "Amp (.agents/skills, ~/.config/agents/skills) and Claude Code (~/.claude/skills)"
argument-hint: [new athlete, sport, goal, "build my coach"]
---

# Coach Builder Router

## Missione

Questa è la skill di ingresso del sistema. Qualunque atleta o coach che voglia "costruirsi il proprio coach" parte da qui: la skill identifica il profilo dell'utente e assembla lo stack di skill corretto dal repository, senza costringere l'utente a conoscere la struttura interna del sistema.

## Domanda di instradamento

Poni sempre questa domanda minima prima di procedere, se non già chiaro dal contesto: "Qual è il tuo profilo primario? (1) Powerlifter/forza massimale, (2) Weightlifter olimpico, (3) Football americano/running back, (4) Atleta ibrido/HYROX, (5) Popolazione generale/fitness, (6) Preparatore atletico che gestisce più atleti."

## Mappa profilo → skill stack

### Profilo 1 — Powerlifter
Stack: `elite-sc-system` → `athlete-profiling-benchmarking` → `programming-audit-council` → `powerlifting-peaking-system` → `vbt-rfd-open-sets` → `tendon-power-architecture`.
Focus: peaking, attempt selection, autoregolazione RPE, block periodization RTS.

### Profilo 2 — Weightlifter olimpico
Stack: `elite-sc-system` → `athlete-profiling-benchmarking` → `programming-audit-council` → `olympic-weightlifting-technique` → `vbt-rfd-open-sets` → `tendon-power-architecture`.
Focus: tecnica snatch/clean&jerk, correzione early arm bend, footwork jerk.

### Profilo 3 — Football americano / Running Back
Stack: `elite-sc-system` → `athlete-profiling-benchmarking` → `programming-audit-council` → `football-rb-system` → `football-cod-footwork` → `tendon-power-architecture` → `clinical-prehab-system` → `vbt-rfd-open-sets`.
Focus: 200ms window, contact balance, ball security, COD, prehab.

### Profilo 4 — Atleta ibrido / HYROX
Stack: `elite-sc-system` → `athlete-profiling-benchmarking` → `programming-audit-council` → `hyrox-hybrid-system` → `energy-systems-recovery` → `vbt-rfd-open-sets`.
Focus: engine aerobico, LT1/LT2, compromised running, strength reserve.

### Profilo 5 — Popolazione generale / Fitness
Stack: `elite-sc-system` (uso semplificato) → `general-population-fitness` → opzionalmente `vbt-rfd-open-sets` e `programming-audit-council` in versione ridotta se il cliente converge verso obiettivi più specifici.
Focus: 10 pattern fondamentali, aderenza, sicurezza, progressione conservativa.

### Profilo 6 — Preparatore multi-atleta
Nessuno stack fisso: usa `coach-builder-router` per ogni singolo atleta gestito, mantenendo profili separati. Usa `programming-audit-council` come governance trasversale per tutti gli atleti.

## Sequenza operativa standard (qualunque profilo)

1. **Intake**: esegui `athlete-profiling-benchmarking` (o versione ridotta per profilo 5) per raccogliere storico, obiettivi, dati di performance, limitazioni cliniche.
2. **Assessment clinico preliminare**: se emergono flag di dolore, infortuni recenti o storico rilevante, attiva `clinical-prehab-system` prima di qualunque prescrizione di carico.
3. **Costruzione settimana 1**: usa `programming-audit-council` per generare v1, eseguire l'audit a 3 giudici, ed emettere v2 con Sanford gate.
4. **Applicazione skill di dominio**: integra la skill specialistica del profilo (powerlifting, weightlifting, football, HYROX, general population) nella logica di v2.
5. **Ciclo settimanale continuo**: ogni settimana successiva richiede il weekly continuity check descritto in `programming-audit-council`, mai un reset da zero.

## Regola di combinazione skill

Non usare mai una skill di dominio isolata senza `elite-sc-system` come base e senza `programming-audit-council` come governance, salvo richieste puntuali e circoscritte (es. "spiegami solo la tecnica del jerk").

## Auto-diagnosi del profilo da conversazione libera

Se l'utente non dichiara esplicitamente il profilo, usa questi segnali per instradare:
- Menziona 1RM su squat/bench/deadlift, meet, federazione → Profilo 1.
- Menziona snatch, clean & jerk, CrossFit competitivo con focus tecnico olimpico → Profilo 2.
- Menziona ruolo in squadra, football, RB, combine, sprint/COD di gara → Profilo 3.
- Menziona HYROX, gara ibrida, running + stazioni funzionali → Profilo 4.
- Menziona dimagrimento, tono muscolare, salute generale, nessun obiettivo competitivo → Profilo 5.
- Gestisce più atleti o ne parla in terza persona con richieste di programmazione multipla → Profilo 6.

## Scope

Questa è la skill di ingresso del repository. Ogni altra skill elencata sopra è raggiungibile a partire da questo router.
