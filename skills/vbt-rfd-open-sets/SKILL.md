---
name: vbt-rfd-open-sets
description: "Velocity-based training skill for RFD, explosive strength, open sets methodology, readiness management, and velocity-loss based load prescription. Use for advanced load prescription, CNS monitoring, and power-oriented programming (Squillante VBT protocol, Bosco open sets)."
compatibility: "Amp (.agents/skills, ~/.config/agents/skills) and Claude Code (~/.claude/skills)"
argument-hint: [exercise, target velocity, velocity loss, power focus, readiness]
---

# VBT RFD Open Sets

## Missione

Usare la velocità come linguaggio della qualità neurale. Allenare la potenza senza almeno ragionare in termini di velocità significa procedere a sensazione, senza feedback oggettivo.

## VBT come biofeedback

La velocity-based training non è un lusso tecnologico: è il monitor più affidabile per capire readiness giornaliera, qualità dello stimolo, accumulo di fatica, e differenza tra lavoro utile e reps di scarto (junk reps).

### Intent to move
L'intento esplosivo è non negoziabile. Anche con carichi alti (tipici del powerlifting), l'intenzione neurale deve restare quella di muovere il carico il più velocemente possibile.

### Average velocity vs peak velocity
- Average velocity: lift "grinding", non balistici (squat, panca, stacco).
- Peak velocity: lift balistici (clean, snatch, jump, throw).

## Zone di velocity loss

| Velocity loss | Stato neuromuscolare | Obiettivo | Velocità target indicativa |
|---|---|---|---|
| 0-10% | Massima readiness | Peak power / RFD | ~1.3 m/s |
| 10-20% | Fatica minima | Forza esplosiva | ~1.0-1.2 m/s |
| 20-30% | Fatica moderata | Ipertrofia funzionale | ~1.0 m/s |
| 40%+ | Fatica estrema | Terminare la serie — alto rischio metabolico | N/A |

Per movimenti di potenza primaria (squat/clean variants) il target di peak power velocity di riferimento nelle fonti è 1.0-1.3 m/s.

## Open Sets (metodologia Bosco/Squillante)

Le ripetizioni non sono fisse per convenzione del coach: la serie continua finché la velocità dell'atleta resta nel range di qualità prestabilito. Nel momento in cui la velocità scende sotto la soglia target (es. -20%), la serie termina immediatamente.

Perché funziona: rispetta la readiness reale del giorno, elimina le junk reps, preserva il sistema nervoso centrale, mantiene pulito l'obiettivo adattativo della sessione.

## Logica di prescrizione

**Focus power/RFD**: bassa velocity loss (0-10%), volumi contenuti, intent massimo, recuperi pieni (120-180s). **Focus ipertrofia funzionale**: 20-30% velocity loss, più volume ma sempre con soglia di qualità. Da evitare: usare velocity loss alta quando l'obiettivo dichiarato è speed-power; fare reps fisse ignorando il decadimento di velocità reale; confondere fatica accumulata con qualità dello stimolo.

## Readiness management

Se la velocità baseline della sessione è chiaramente sotto la norma dell'atleta, riduci carico o volume, oppure cambia l'obiettivo della seduta. Un proxy utile complementare è il rolling average dei Countermovement Jump (CMJ): se l'altezza di salto è significativamente sotto la media dell'atleta, il carico va aggiustato per prevenire overtraining. Regola dura: non inseguire il numero sul bilanciere se la velocità o il CMJ segnalano che il sistema non è pronto.

## Transfer per contesto

**Football/RB**: la VBT protegge la finestra dei 200ms, migliora il first-step power, evita volume che rallenta il transfer, monitora lo stato neurale senza affidarsi a percezioni soggettive. **Hybrid/HYROX**: la VBT evita di sprecare il budget neurale dentro un programma concorrente forza-endurance, mantiene la strength reserve necessaria per le stazioni, controlla il costo neurologico della forza rispetto all'engine aerobico.

## Scope

Skill dedicata alla logica VBT. Per periodizzazione e audit settimanale usa `programming-audit-council`. Per football transfer specifico usa `football-rb-system`. Per clinica e ritorni da dolore usa `clinical-prehab-system`. Per architettura tendinea usa `tendon-power-architecture`.
