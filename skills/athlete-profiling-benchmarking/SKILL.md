---
name: athlete-profiling-benchmarking
description: "Athlete intake, assessment, and benchmarking skill. Covers the NFL-style pre-onboarding interview structure, injury history screening, combine-style physical testing, mobility/asymmetry screening, positional performance benchmarks (RB combine data), neuromuscular profiling (energy-system dominance, tendon status, readiness), and the deconditioned-athlete loading rule. Use at the start of any new coaching relationship, after a long layoff, injury, or season transition, and before writing any program for building a criterion-based rebuilding phase — no load should ever be prescribed without this data."
compatibility: "Amp (.agents/skills, ~/.config/agents/skills) and Claude Code (~/.claude/skills)"
argument-hint: [intake interview, assessment, combine testing, benchmarking, deconditioned athlete, neuromuscular profile]
---

# Athlete Profiling & Benchmarking

## Missione

Non si scrive una programmazione prima di avere dati. Un preparatore che prende in carico un atleta reduce da stop o mai valutato deve condurre un'intervista strutturata e una batteria di test minima prima di qualunque prescrizione di carico. Nessuna delle skill di programmazione (`programming-audit-council`, `periodization-block-planner`, `hyrox-hybrid-system`) può funzionare senza dati di baseline reali: prescrivere carichi senza intake è la causa più comune di programmazione "a scatola chiusa".

## Struttura dell'intervista di intake

L'intervista precede sempre la programmazione. Deve raccogliere dati per blocchi:

1. **Profilo attuale e obiettivo specifico**: ruolo primario/secondario, obiettivo competitivo con orizzonte temporale, percezione soggettiva dei 3 limiti fisici principali, priorità fisica singola su cui investire, tempo settimanale reale disponibile.
2. **Storia di infortuni e salute**: chirurgie pregresse, distorsioni ricorrenti, infortuni a ginocchio/anca/bacino/lombari/spalle/polsi, concussioni, condizioni mediche croniche, allergie/intolleranze, scala soggettiva di integrità articolare/tendinea.
3. **Decondizionamento attuale**: tempo reale di inattività, causa dello stop (infortunio, off-season, personale), test qualitativi immediati (camminata, push-up, scale), dolori/rigidità al risveglio, variazione di peso e composizione corporea, qualità del sonno e stress.
4. **Dati di performance passata**: 1RM o stime su squat/hinge/press/pull, test di salto (CMJ, squat jump, broad jump) con data, tempi di sprint (10m/20m/40yd) e agility (3-cone, shuttle) con metodo di cronometraggio, ruolo nella rotazione e utilizzo tattico.
5. **Profilo tecnico di gioco**: tipo di atleta (power/COD/elusive/all-round), pattern preferiti, feedback ricevuti da coach precedenti su limiti fisici.
6. **Forza, potenza e storico sala pesi**: RPE medi tenuti sulle alzate principali, pattern di forza più lavorati, familiarità con alzate olimpiche, esercizi problematici, forza relativa (kg/kg BW), familiarità con RPE/RIR e autoregolazione.
7. **Mobilità, postura e asimmetrie**: screening funzionale pregresso, limitazioni in squat profondo, half-kneeling, mobilità toracica, asimmetrie destra/sinistra, note posturali.
8. **Capacità condizionali**: percezione di forza in accelerazione/velocità media/top speed, fiducia nei cambi di direzione, lavoro pregresso su meccanica di corsa, dati video disponibili.
9. **Capacità metabolica**: risposta a carichi ripetuti in game situation, preferenza tra conditioning specifico vs generico, dati di frequenza cardiaca, tolleranza a protocolli tipo gasser/shuttle.
10. **Lifestyle e recupero**: ore di sonno reali, stress non fisico, alimentazione (pasti, proteine, tracking), alcol/sostanze, integrazione già in uso, accesso a strumenti di recupero.
11. **Ambiente, attrezzatura e logistica**: accesso palestra e tipo di attrezzatura, accesso campo/pista, strumenti di monitoraggio disponibili, disponibilità a tracciare dati.
12. **Preferenze di comunicazione**: livello di dettaglio desiderato nella programmazione, propensione a dare feedback (proattivo vs "stringere i denti"), vincoli non negoziabili di tempo/mindset.

## Batteria di test: ordine di esecuzione consigliato

| Ordine | Test | Cosa misura | Collegamento |
|---|---|---|---|
| 1 | Screening 6 pattern | Qualità di movimento, asimmetrie, dolore | `biomechanics-movement-screen` |
| 2 | Test isometrici tendinei | SL heel raises, SL hops, Squat 60%BW 6sx6 | `clinical-prehab-system` |
| 3 | 1RM o stima RPE-based | Squat, Hinge, Press, Pull principali | `periodization-block-planner` |
| 4 | Test di velocità/potenza | Sprint 10-20m, salto verticale/orizzontale | `vbt-rfd-open-sets` (se disponibile encoder) |
| 5 | Test energetico specifico | RSA se sport di squadra, LT1/LT2 stimato se ibrido | `energy-systems-recovery` / `hyrox-hybrid-system` |

### Batteria minima anche da decondizionato

Test eseguibili senza rischio anche in stato di decondizionamento, per stabilire una baseline minima prima della Fase 1:

- **Generali**: peso corporeo mattutino su 3 giorni, push-up massimali tecnici, plank isometrico a tecnica pulita, squat a corpo libero fino a RPE 8.
- **Forza (RPE 7-8, non 1RM)**: squat o variante sicura per 5 reps comode, hinge (trap bar/RDL) 5 reps, panca piana 5 reps, trazioni massime (con eventuale assistenza quantificata).
- **Campo**: 3 sprint da 10m cronometrati (miglior tempo), 3 sprint da 20m, opzionale 300yd shuttle o 6x40yd se l'atleta si sente pronto (altrimenti differire 2-3 settimane).

Prima di somministrare la batteria completa, verificare sempre: disponibilità dell'atleta a testarsi subito vs necessità di riattivazione soft preliminare, e presenza di limitazioni attuali che sconsigliano sprint/eccentrici immediati.

## Profiling neuromuscolare: cosa classificare

- **Dominanza energetica**: potenza pura (ATP-CP) vs RSA vs aerobico-dominante — determina il bias iniziale di programmazione (vedi `energy-systems-recovery`).
- **Stato tendineo**: verde (nessun dolore, benchmark raggiunti) / giallo (dolore lieve intermittente) / rosso (dolore riproducibile, richiede il filtro clinico di `clinical-prehab-system` attivo da subito).
- **Livello di readiness generale**: decondizionato (>4 settimane stop) vs mantenuto vs in pieno carico.

### Regola operativa per atleta decondizionato

Se l'intake rivela >4 settimane di stop: RPE main lift ≤6.5 per le prime 2 settimane, nessuna eccezione — questa regola sovrascrive qualsiasi entusiasmo dell'atleta di "recuperare il tempo perso".

## Benchmark di riferimento per posizione (Running Back)

Valori di riferimento storici/da combine utili per contestualizzare i test dell'atleta (fonte: dati combine e report di profiling posizionale):

| Test | Riferimento indicativo |
|---|---|
| 40-yard dash | Variabile per ruolo, il valore isolato è meno informativo del 10-yard split |
| Vertical Jump | Riferimento di esplosività verticale |
| Broad Jump | Riferimento di potenza orizzontale |
| L-Cone Drill | Riferimento di COD/agility |
| Pro Shuttle (5-10-5) | Riferimento di cambio di direzione a corto raggio |

Il valore diagnostico più utile per un RB non è il 40-yard dash assoluto, ma lo split sui 10 yard, che riflette meglio il first-step dominance realmente utile in game.

## Output dell'intake: cosa deve produrre

Un intake completo deve produrre 4 output scritti prima di procedere a qualsiasi v1 di programmazione:

1. Profilo di readiness (verde/giallo/rosso per tendini, decondizionato sì/no)
2. Massimali/stime di riferimento per i pattern principali
3. Flag clinici attivi (dolore, asimmetrie, aree da monitorare)
4. Obiettivo primario dichiarato (ipertrofia, forza, HYROX, football, ibrido)

Collegare sempre l'output di questa skill a `programming-audit-council` per la generazione della prima settimana, e a `clinical-prehab-system` se emergono flag di dolore o storico infortuni rilevanti.

## Errore da evitare

Non generare mai una v1 di microciclo senza i 4 output sopra. Se l'utente chiede direttamente un programma senza aver fornito questi dati, la risposta corretta è raccogliere prima l'intake, non presumere valori di default.

## Scope

Skill dedicata all'assessment iniziale. Per la logica di programmazione generale usa `elite-sc-system`. Per l'audit e la governance settimanale usa `programming-audit-council`. Per football/RB specifico usa `football-rb-system`. Per lo screening biomeccanico dettagliato usa `biomechanics-movement-screen`.
