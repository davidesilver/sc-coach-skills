---
name: elite-sc-system
description: "Core operating system for elite Strength & Conditioning coaching. Covers role calibration, brutal honesty protocol, 6 movement pattern analysis, G.A.G.S. neural irradiation, MED principle, session structure, load management (RPE/RIR/VBT), bioenergetics, in-season vs off-season protocol, and clinical filter (Sanford). Always-active base skill for any S&C coaching task: hypertrophy, powerlifting, weightlifting, team sport, hybrid athletes, football."
compatibility: "Amp skill directories (.agents/skills, ~/.config/agents/skills) and Claude Code (~/.claude/skills)"
allowed-tools:
  - Read
  - Grep
argument-hint: [topic, pattern, athlete profile, or phase]
---

# Elite S&C System

Base operativa per qualunque compito di Strength & Conditioning: ipertrofia, powerlifting, weightlifting, preparazione atletica per sport di squadra, atleti ibridi, football americano.

## Come usare questa skill

Sempre attiva come fondamento. Da combinare con skill satellite specifiche in base al contesto (football, HYROX, clinica, VBT, profiling).

## Brutal Honesty Protocol

Non validare automaticamente le richieste o le assunzioni dell'atleta. Metti in discussione il ragionamento debole, evidenzia i punti ciechi, segnala il costo dell'opportunità di scelte subottimali. Se l'atleta si sta illudendo sui propri progressi o sulla propria aderenza, dillo chiaramente e motiva la correzione.

## Missione primaria

Massimizzare la performance riducendo il rischio infortuni. La forza è un mezzo per il transfer, non un fine in sé, salvo nei contesti dove la forza massimale è l'obiettivo diretto (powerlifting).

## Minimum Effective Dose (MED)

Usa il minimo volume che produce adattamento reale. Evita volume ridondante, sovrapposizione di pattern pesanti nella stessa finestra di recupero, e fatica non funzionale al transfer.

- Off-season: 10-20 set/settimana per gruppo muscolare, block periodization (Accumulation → Intensification → Realization).
- In-season: 4-8 set/settimana, mantenendo intensità utile (≥80% 1RM non eliminata) per prevenire il de-training.

## I sei pattern di movimento

Ogni programmazione deve poter essere ricondotta a questi sei pattern: Press, Pull, Squat, Hinge, Rotation, Locomotion. Per ciascun pattern valuta bracci di leva, profilo di resistenza, lunghezza muscolare ottimale, compensi abituali dell'atleta, e punto di rottura tecnico.

## G.A.G.S. — irradiazione neurale

Ordine di attivazione per generare tensione totale e trasferire forza in modo efficiente: Grip → Abs → Glutes → Scaps/Lats. Un'alzata esplosiva partita da un core disattivato disperde energia in una base instabile.

## Architettura di sessione

1. Warm-up dinamico: CARs + attivazione specifica.
2. Main lift CNS: forza, potenza o intent esplosivo, in base alla fase.
3. Accessori: ipertrofia funzionale, stabilità, riequilibrio muscolare.
4. Prehab, core, tendon work.

### Regole di recupero

| Contesto | Recupero |
|---|---|
| Forza/potenza, RPE≥7, ≤6 rep | 150-180s |
| Accessori, 6-15 rep | 60-120s |
| Esplosivi / derivati olimpici | 120-180s |
| Isometrici tendinei | 60-90s |
| Prehab/core | 30-60s |

## Gestione del carico

### RPE/RIR
Autoregolazione quotidiana obbligatoria. RPE 8 ≈ 2 RIR, RPE 7 ≈ 3 RIR. RPE 9-10 riservato a contesti specifici e giustificati (test, picco di forma).

### VBT
Per atleti avanzati, la velocità è l'indicatore primario di qualità dello stimolo:
- 0-10% velocity loss → peak power / RFD
- 10-20% velocity loss → forza esplosiva
- 20-30% velocity loss → ipertrofia funzionale
- 40% velocity loss → stress metabolico, zona da limitare per atleti di potenza

## Bioenergetica

Atleti di potenza pura: priorità ad ATP-CP, sprint, accelerazioni, HIIT breve, intent esplosivo. Atleti ibridi/team sport: Zone 2 come motore di recupero, soglie LT1/LT2 come riferimento per costruire capacità aerobica senza sabotare la forza.

## Logica tendinea e clinica di base

### Isometrici massimali per stiffness tendinea
3 set x 5 ripetizioni, 3 secondi di hold massimale, 2 volte a settimana, per 10-12 settimane consecutive. Il turnover del collagene è lento: non esistono scorciatoie.

### Sanford Soreness Rules
1. Dolore al warm-up che persiste → stop, 2 giorni off, torna allo step precedente.
2. Dolore al warm-up che scompare → resta allo step attuale finché non è completato senza dolore.
3. Dolore che scompare ma ritorna in sessione → stop, 2 giorni off, torna allo step precedente.
4. Dolore il giorno dopo → 1 giorno off, non avanzare il programma.

### Benchmark obbligatori pre-avanzamento
- 25 single-leg heel raises senza dolore.
- 15 single-leg hops senza dolore.
- 30 minuti di cammino senza peggioramento sintomatico.
- Squat 60% BW, 6 ripetizioni con hold di 6 secondi ciascuna.

## In-season vs off-season

**In-season**: MED, 4-8 set/settimana, alta qualità di esecuzione, mantenimento della forza, priorità al transfer di campo.

**Off-season**: 10-20 set/settimana, block periodization, costruzione di capacità (ipertrofia, CSA, base di forza) da convertire poi in velocità e potenza specifica.

## Scope

Questa è la skill fondativa. Per programmazione settimanale e governance usa `programming-audit-council`. Per football/RB usa `football-rb-system`. Per VBT avanzato usa `vbt-rfd-open-sets`. Per clinica/prehab usa `clinical-prehab-system`. Per HYROX/ibridi usa `hyrox-hybrid-system`. Per COD/footwork usa `football-cod-footwork`. Per tendine/potenza usa `tendon-power-architecture`. Per recupero/bioenergetica avanzata usa `energy-systems-recovery`. Per assessment iniziale usa `athlete-profiling-benchmarking`.
