---
name: powerlifting-peaking-system
description: "Powerlifting-specific programming skill. Covers block periodization (RTS Development/Pivot Block model), linear peaking phases (volume→strength→power), tapering protocols pre-meet, RPE-based autoregulation, and competition-day attempt selection for squat/bench/deadlift."
compatibility: "Amp (.agents/skills, ~/.config/agents/skills) and Claude Code (~/.claude/skills)"
argument-hint: [meet prep, peaking block, tapering, RPE autoregulation, attempt selection]
---

# Powerlifting Peaking System

## Missione

Un powerlifter non si allena per "sentirsi forte", si allena per esprimere il massimo su tre alzate in un giorno preciso. Ogni blocco deve essere funzionale a quella data, non a un ideale astratto di forza generica.

## Modello Development Block / Pivot Block (RTS)

Approccio bottom-up alla periodizzazione, alternativo alla periodizzazione lineare classica [web:49].

### Development Block
Un microciclo (1 settimana) viene ripetuto finché la performance non cala su un'alzata di riferimento (es. singola a RPE8 + back-off 4x4). Il numero di ripetizioni del microciclo prima del calo di performance definisce il "time to peak" (TTP) individuale dell'atleta [web:49].

- Se il TTP è lungo (es. 11 settimane), è difficile reagire ai cambiamenti in tempo utile.
- Per accorciare il TTP e renderlo più gestibile, aumenta la frequenza settimanale dell'alzata target (es. schema A+B nello stesso microciclo) [web:49].
- Il primo Development Block deve essere portato oltre il picco: si riconosce il superamento del picco quando la performance cala per due o più settimane consecutive [web:49].

### Pivot Block
Non è un deload — è un cambio di stimolo che riduce fatica, abbassa intensità, varia la struttura dell'allenamento, e prepara l'atleta al prossimo Development Block [web:49]. Durata indicativa: circa un terzo della lunghezza del Development Block precedente. Esempio di distribuzione RPE in un Pivot Block: 10 rip @RPE6, 10 rip @RPE7, 10 rip @RPE8, più un set di scarico [web:49].

## Periodizzazione lineare classica (alternativa)

Modello a fasi su 12-16 settimane, con intensità crescente e volume calante [web:52]:

| Fase | Durata indicativa | Rep range | Intensità |
|---|---|---|---|
| Ipertrofia/volume | Prime settimane | 8-12 rip | Moderata |
| Forza | Fase centrale | 3-6 rip | Alta |
| Potenza/peaking | Ultime settimane pre-meet | 1-3 rip | ≥90% 1RM |

Movimenti più semplici e ad alto volume vanno collocati nelle fasi iniziali, quando è più facile accumulare lavoro senza rischio tecnico eccessivo [web:52].

## Principio chiave del peaking (JTS)

L'intensità conserva la forma fisica meglio del volume. Per raggiungere la forza massima servono sia volume alto che intensità alta nelle fasi corrette, ma nella fase finale di peaking il volume va tagliato mantenendo intensità elevata, per dissipare la fatica senza perdere gli adattamenti neurali acquisiti [web:50].

## Tapering pre-competizione

Il tapering (o in alcuni casi la cessazione temporanea dell'allenamento) prima di una gara maggiore serve a migliorare la performance dissipando la fatica accumulata mantenendo gli adattamenti di forza [web:55]. Regole pratiche:
- Riduci il volume progressivamente nelle ultime 1-3 settimane pre-meet, mantenendo picchi di intensità bassi in frequenza ma presenti (aperture a peso di gara).
- Non introdurre mai nuovi esercizi o pattern tecnici nella fase di taper.
- L'obiettivo del taper è arrivare al giorno di gara "freschi ma non stantii": un taper troppo lungo o troppo aggressivo può causare perdita di specificità neurale.

## Autoregolazione RPE

Ogni sessione principale va gestita con RPE/RIR quotidiano (vedi anche `elite-sc-system` e `vbt-rfd-open-sets` per l'integrazione con la velocità). Se l'RPE reale supera sistematicamente il target di oltre 0.5-1 punto su più sessioni, il blocco va rivalutato: o il carico prescritto era mal calibrato, o la fatica accumulata richiede un Pivot Block anticipato [web:49].

## Attempt selection il giorno di gara

Principi generali derivati dalla pratica competitiva:
- Prima alzata: 90-93% del massimale stimato, un'alzata quasi certa, per costruire fiducia e "aprire" il sistema nervoso.
- Seconda alzata: verso il record personale o poco sopra, in base a come si è sentita la prima.
- Terza alzata: tentativo massimale, deciso solo dopo aver visto la qualità tecnica della seconda.
- Non cambiare mai la strategia di attempt selection sotto pressione emotiva del meet day: la decisione va presa a mente lucida, idealmente pre-pianificata con il coach.

## Split di allenamento

Per principianti: split a 3 giorni, un'alzata principale per sessione [web:52]. Per intermedi/avanzati: split a 4 giorni o Push-Pull-Squat, con maggiore varietà di esercizi e frequenza per pattern [web:52]. Regola di recupero: 2-3 giorni tra sessioni che sollecitano lo stesso gruppo muscolare pesante [web:52].

## Valutazione periodica

Ogni 12-16 settimane, valuta oggettivamente: progressi di forza assoluta, qualità tecnica, plateau, ed eventuale necessità di modificare selezione esercizi, split o strategia di periodizzazione [web:52].

## Scope

Skill dedicata al powerlifting competitivo. Per la logica biomeccanica di base usa `elite-sc-system`. Per governance settimanale e audit usa `programming-audit-council`. Per gestione RPE/velocità integrata usa `vbt-rfd-open-sets`. Per architettura tendinea e RFD usa `tendon-power-architecture`.
