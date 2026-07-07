---
name: hyrox-hybrid-system
description: "Hybrid athlete and HYROX-specific training system. Covers the 70/30 aerobic/strength split, VO2max/LT1/LT2 thresholds, 5-zone heart rate table, compromised running, brick session design, strength reserve, station-by-station technique cues for all 8 stations, Open/Pro benchmarks, 12-week periodization, and race pacing. Use whenever the athlete races HYROX, trains as a hybrid strength+endurance competitor, or needs a fixed run+functional-station format programmed. Strength is a means, not the end, for hybrid competitors."
compatibility: "Amp (.agents/skills, ~/.config/agents/skills) and Claude Code (~/.claude/skills)"
argument-hint: [HYROX prep, hybrid athlete, compromised running, brick session, station cues, race pacing]
---

# HYROX Hybrid System

## Quando attivare questa skill

Insieme a `elite-sc-system` (sempre base) quando l'atleta:
- Si allena per HYROX Open o Pro
- È un "ibrido" che fa sia forza che endurance nello stesso mesociclo
- Ha bisogno di gestire l'interference effect tra forza massimale e capacità aerobica

## Missione e principio cardine: il 70/30

Nell'atleta ibrido/HYROX la forza pura è un mezzo, non un fine. Circa il 70% della durata di gara è a componente aerobica (corsa + SkiErg + Row), mentre solo il 30% è forza/potenza pura. Questo dato ribalta l'errore più comune: programmare come un powerlifter invece che come un mezzofondista con stazioni di forza. La priorità va data all'engine aerobico, alle soglie LT1/LT2, al compromised running e alla gestione della strength reserve sulle stazioni.

## Errore più comune

Fare training con bias eccessivo sulla forza pura e conditioning insufficiente. HYROX è una gara dominata dalla componente endurance: 8km di corsa intervallati da 8 stazioni funzionali, il vero limitante nella maggior parte degli atleti è l'engine, non la forza massimale.

## I tre pilastri fisiologici

1. **VO2max** — la dimensione del motore, il tetto genetico-allenabile.
2. **LT1 (soglia aerobica)** — la base del motore, lavoro prevalentemente Zone 2, costruisce capacità di smaltire lattato a intensità sub-massimali e supporta il recupero tra le stazioni.
3. **LT2 (soglia anaerobica)** — il ritmo massimo sostenibile per ~60 minuti; è il vero predittore del tempo gara. Il lavoro qui deve essere specifico e non eccessivo, per non compromettere il recupero generale.
4. **Fractional utilization** — % di VO2max sostenibile per tutta la durata; separa l'atleta Elite dall'Intermedio più della VO2max assoluta.

## Zone cardiache operative (5 zone)

| Zona | %FCmax | Talk test | Uso |
|---|---|---|---|
| 1 | 50-60% | Canta una canzone | Recupero attivo, smaltimento |
| 2 | 60-70% | Conversazione piena | Base aerobica, densità capillare/mitocondriale |
| 3 | 70-80% | Frasi brevi | LT1 / ritmo gara sostenibile |
| 4 | 80-90% | 1-2 parole | LT2 / lattato clearance, il vero motore del Row |
| 5 | 90-100% | Nessuna parola | VO2max, ultimi 100 Wall Ball |

## Compromised running

La corsa in HYROX non è mai "fresca": ogni tratto degli 8km viene eseguito dopo una stazione che ha già affaticato pattern specifici (es. corsa dopo sled push, corsa dopo wall balls). Il transfer allenante deve includere sessioni di corsa eseguite in stato di pre-fatica indotta, non solo corsa isolata a fondo lento. La corsa compromessa è la variabile che separa Intermedio da Advanced: chi ha training specifico degrada meno il passo dopo le stazioni pesanti.

**Regola pratica di pacing gara**: correre il km fresco 10-15 secondi/km più lento del proprio PR sui 10k, per restare vicino a LT2 senza andare in rosso troppo presto.

### Protocollo Brick (sessione firma di questa skill)

- 4-6 round di 800m-1km a ritmo gara, immediatamente seguiti da 1 stazione leg-heavy (sled push, lunge)
- Iniziare al 60-80% del volume gara, salire al 100% nelle ultime 3-4 settimane pre-gara
- Non più di 1 sessione brick completa a settimana: è la sessione a costo sistemico più alto del microciclo

## Strength reserve: perché la forza conta comunque

La forza va programmata come riserva funzionale per le stazioni, non come obiettivo estetico o massimale fine a sé stesso. Ogni stazione ha un profilo di forza-resistenza specifico (es. sled push/pull richiede forza-potenza orizzontale ripetuta, wall balls richiede resistenza muscolare locale su pattern squat-throw). La forza massimale in palestra serve solo se si traduce in efficienza e risparmio energetico sulla stazione specifica.

Il concetto di Strength Reserve dice che più alto è il 1RM assoluto, minore è la % di sforzo richiesta dai carichi fissi di gara (es. sled 152kg). Se il tuo max è 200kg, il sled Pro rappresenta il 76% invece del 100%+ di chi ha un max di 150kg: meno drenaggio del sistema nervoso centrale, gambe più fresche per la corsa successiva.

| Profilo atleta | Debolezza tipica | Priorità di training |
|---|---|---|
| Endurance-dominante | Sled push/pull, wall ball | Ipertrofia strutturale, forza massimale |
| Strength-dominante | Run endurance, pacing, LT2 | Base aerobica Zona 2, running economy |

## Le 8 stazioni: cue tecnico + errore da evitare

| Stazione | Cue tecnico | Errore comune |
|---|---|---|
| SkiErg 1000m | Hip-hinge, mani "in tasca" a fine tirata | Tirare solo con le braccia |
| Sled Push 50m | Linea rigida spalla-caviglia, passi corti e potenti | Falcate lunghe che rompono la linea di spinta |
| Sled Pull 50m | Camminata all'indietro, peso corporeo come leva | Tirare con le braccia, bruciando le spalle per il Row |
| Burpee Broad Jump 80m | Step-up (un piede alla volta) invece del salto | Salto esplosivo che fa impennare la FC |
| Rowing 1000m | Spinta gambe potente, slitta controllata (recupero attivo) | Trattarlo come sprint invece che come stazione di recupero attivo |
| Farmers Carry 200m | Petto alto, scapole retratte, passi corti | Camminata lenta e sbilanciata |
| Sandbag Lunges 100m | Busto verticale, sacco alto sui trapezi | Busto flesso in avanti, ginocchio che "sbatte" a terra |
| Wall Balls 75-100 | Potenza dalle gambe, braccia solo guida | Serie uniche senza spezzare (usare blocchi da 20 con micro-pause 5s) |

### Roxzone: la stazione nascosta

Il tempo speso in Roxzone (transizione) va trattato come recupero attivo, non sosta passiva: jog leggero, respirazione ritmica 3-in/2-out, reset della FC prima di riattaccare il km successivo.

## Gestione della fatica in training concorrente

Il training concorrente forza-endurance genera interferenza se non gestito con criterio. Regole pratiche:
- Separare temporalmente sessioni di forza pesante e sessioni aerobiche ad alta intensità quando possibile (non nello stesso giorno o con adeguato distanziamento).
- Usare la Zone 2 come strumento di recupero attivo, non come stimolo che compete con la forza.
- Monitorare il costo neurologico della forza (vedi `vbt-rfd-open-sets`) per non intaccare la qualità del lavoro aerobico successivo.

## Regola del 10% e prevenzione

L'incremento di volume settimanale di corsa non deve superare il 10%, per tutelare la tenuta muscolo-tendinea durante l'accumulo del carico brick-specifico. Integrare sempre con `clinical-prehab-system` per Copenhagen/tibialis quando il volume di corsa sale.

## Periodizzazione per HYROX

Un blocco di preparazione tipico segue una logica di costruzione progressiva: base aerobica e forza generale nelle fasi iniziali, poi specificità di stazione e pacing di gara nelle fasi finali, con un taper che preserva la capacità aerobica riducendo il volume di forza pesante.

| Fase | Settimane | Focus |
|---|---|---|
| Fondazione | 1-4 | Base aerobica Zona 2, forza fondativa 3x10 RPE 7-8 |
| Potenza e specificità | 5-8 | Intervalli LT2, potenza funzionale, sled/burpee |
| Simulazione | 9-11 | Brick completo, corsa compromessa Zona 4-5 |
| Tapering | 12 | -40/50% volume, mantenimento intensità, focus CNS/sonno |

## Pacing e benchmark competitivi

I benchmark di riferimento per il tiering competitivo si basano su tempi di stazione e split di corsa comparati a standard di categoria (open, pro, elite). La programmazione deve indirizzarsi verso il miglioramento specifico degli split più deboli dell'atleta (running vs stazioni), identificati tramite test e simulazioni di gara parziali.

| Stazione | Donne Open | Donne Pro | Uomini Open | Uomini Pro |
|---|---|---|---|---|
| Sled Push 50m | 102 kg | 152 kg | 152 kg | 202 kg |
| Sled Pull 50m | 78 kg | 103 kg | 103 kg | 153 kg |
| Farmers Carry | 2x16kg | 2x24kg | 2x24kg | 2x32kg |
| Sandbag Lunges | 10kg | 20kg | 20kg | 30kg |
| Wall Balls | 4kg/75 | 6kg/100 | 6kg/100 | 9kg/100 |

Raccomandazione clinica: sub-75 minuti in Open prima di passare a Pro, per assicurare che la forza fondativa gestisca i carichi più pesanti senza compromettere la meccanica di corsa.

## Note cliniche donna

Fase follicolare (giorni 1-14): finestra ottimale per PR di forza massimale e lavoro ad alta intensità. Fase luteale: RPE percepito più alto per via della temperatura corporea, spostare enfasi su volume Zona 2 e recupero.

## Scope

Skill dedicata ad atleti ibridi e HYROX. Per la logica biomeccanica di base usa `elite-sc-system`. Per governance della programmazione usa `programming-audit-council`. Per VBT e gestione del carico neurale usa `vbt-rfd-open-sets`. Per bioenergetica e recupero approfonditi usa `energy-systems-recovery`.

## Riferimenti

Framework concettuale (soglie, strength reserve, gestione fatica) e dati/protocolli tattici (zone HR, protocollo Brick, cue tecnici delle 8 stazioni, benchmark Open/Pro, periodizzazione 12 settimane) integrati da report interni sullo Space su HYROX/hybrid training.
