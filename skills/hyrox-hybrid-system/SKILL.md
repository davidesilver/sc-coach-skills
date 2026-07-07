---
name: hyrox-hybrid-system
description: "Hybrid athlete and HYROX-specific training system. Covers aerobic engine development, LT1/LT2 thresholds, compromised running, strength reserve, station-specific pacing, and fatigue management for concurrent training. Strength is a means, not the end, for hybrid competitors."
compatibility: "Amp (.agents/skills, ~/.config/agents/skills) and Claude Code (~/.claude/skills)"
argument-hint: [HYROX prep, hybrid athlete, compromised running, race pacing]
---

# HYROX Hybrid System

## Missione

Nell'atleta ibrido/HYROX la forza pura è un mezzo, non un fine. La priorità va data all'engine aerobico, alle soglie LT1/LT2, al compromised running e alla gestione della strength reserve sulle stazioni.

## Errore più comune

Fare training con bias eccessivo sulla forza pura e conditioning insufficiente. HYROX è una gara dominata dalla componente endurance: 8km di corsa intervallati da 8 stazioni funzionali, il vero limitante nella maggior parte degli atleti è l'engine, non la forza massimale.

## Soglie fisiologiche

**LT1 (soglia aerobica)**: la base del motore, lavoro prevalentemente Zone 2, costruisce capacità di smaltire lattato a intensità sub-massimali e supporta il recupero tra le stazioni. **LT2 (soglia anaerobica)**: la soglia che determina il ritmo gara sostenibile su 8km compromessi; il lavoro qui deve essere specifico e non eccessivo, per non compromettere il recupero generale.

## Compromised running

La corsa in HYROX non è mai "fresca": ogni tratto degli 8km viene eseguito dopo una stazione che ha già affaticato pattern specifici (es. corsa dopo sled push, corsa dopo wall balls). Il transfer allenante deve includere sessioni di corsa eseguite in stato di pre-fatica indotta, non solo corsa isolata a fondo lento.

## Strength reserve

La forza va programmata come riserva funzionale per le stazioni, non come obiettivo estetico o massimale fine a sé stesso. Ogni stazione ha un profilo di forza-resistenza specifico (es. sled push/pull richiede forza-potenza orizzontale ripetuta, wall balls richiede resistenza muscolare locale su pattern squat-throw). La forza massimale in palestra serve solo se si traduce in efficienza e risparmio energetico sulla stazione specifica.

## Gestione della fatica in training concorrente

Il training concorrente forza-endurance genera interferenza se non gestito con criterio. Regole pratiche:
- Separare temporalmente sessioni di forza pesante e sessioni aerobiche ad alta intensità quando possibile (non nello stesso giorno o con adeguato distanziamento).
- Usare la Zone 2 come strumento di recupero attivo, non come stimolo che compete con la forza.
- Monitorare il costo neurologico della forza (vedi `vbt-rfd-open-sets`) per non intaccare la qualità del lavoro aerobico successivo.

## Periodizzazione per HYROX

Un blocco di preparazione tipico segue una logica di costruzione progressiva: base aerobica e forza generale nelle fasi iniziali, poi specificità di stazione e pacing di gara nelle fasi finali, con un taper che preserva la capacità aerobica riducendo il volume di forza pesante.

## Pacing e benchmark competitivi

I benchmark di riferimento per il tiering competitivo si basano su tempi di stazione e split di corsa comparati a standard di categoria (open, pro, elite). La programmazione deve indirizzarsi verso il miglioramento specifico degli split più deboli dell'atleta (running vs stazioni), identificati tramite test e simulazioni di gara parziali.

## Scope

Skill dedicata ad atleti ibridi e HYROX. Per la logica biomeccanica di base usa `elite-sc-system`. Per governance della programmazione usa `programming-audit-council`. Per VBT e gestione del carico neurale usa `vbt-rfd-open-sets`. Per bioenergetica e recupero approfonditi usa `energy-systems-recovery`.
