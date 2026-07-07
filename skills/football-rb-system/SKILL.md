---
name: football-rb-system
description: "Football and running back specific performance system. Covers first-step dominance, the 200ms window, tendon stiffness, deceleration/COD mechanics, contact balance, ball security, field transfer priorities, and structural resilience for collision-sport athletes."
compatibility: "Amp (.agents/skills, ~/.config/agents/skills) and Claude Code (~/.claude/skills)"
allowed-tools:
  - Read
  - Grep
argument-hint: [RB task, field transfer, acceleration, contact balance, ball security]
---

# Football RB System

## Missione

Costruire un atleta da football che trasferisca la forza al campo entro la finestra utile del gesto, non un fenomeno da weight room che arriva tardi sul movimento reale.

## La finestra dei 200ms

Nel football d'élite la maggior parte delle azioni decisive (sprint, contatti, cambi di direzione) avviene sotto i 200 millisecondi. Il training deve dare priorità al Rate of Force Development (RFD) rispetto alla forza massimale lenta: una forza che richiede 600ms per esprimersi è meno utile di una forza inferiore ma disponibile nella finestra reale del gioco.

## Stiffness tendinea come priorità

Per RB e power athlete la stiffness tendinea determina l'RFD: alta rigidità significa che la forza muscolare viene trasmessa immediatamente al terreno invece di essere assorbita da un tendine elastico. Questo si traduce in accelerazione esplosiva, minor costo metabolico dello sprint, e cambi di direzione più violenti.

### Trade-off potenza vs endurance
Stiffness alta = miglior RFD e minor costo metabolico dello sprint. Compliance alta = miglior storage/return di energia, preferita dagli endurance athlete ma controproducente per le esigenze esplosive di un RB. Un RB non va programmato come un endurance athlete: eccesso di compliance e conditioning generico degradano stiffness e first-step dominance.

## Priorità del running back

1. First-step dominance (0-10m).
2. Produzione di forza orizzontale.
3. Competenza nella decelerazione.
4. Meccanica del penultimate step.
5. Contact balance.
6. Ball security sotto redirection e contatto.
7. Resilienza strutturale a collisioni ripetute.

## Il penultimate step

Il penultimate step (il penultimo appoggio prima del plant) è il vero motore della decelerazione: gestisce Ground Reaction Force fino a 2.7x il peso corporeo. Se l'atleta non assorbe in questo appoggio, il plant diventa un gesto di sopravvivenza invece che un vero strumento di redirection. Markers tecnici: abbassamento controllato del centro di massa nei passi precedenti al plant, trunk lean coerente con il vettore di uscita, positive tibia angle (inclinazione dello stinco verso la direzione di uscita), nessun collasso in valgismo del ginocchio.

## Contact balance

Capacità di assorbire il contatto senza perdere allineamento, velocità utile o controllo del centro di massa. Il modello di riferimento nelle fonti utilizza una tecnica hand-down: la mano libera funge da pivot di stabilizzazione a terra, creando un terzo punto di appoggio che ridistribuisce la forza di reazione al suolo e protegge le articolazioni durante il contatto. Prerequisiti: bassa altezza del COM, rigidità attiva, piedi vivi durante l'impatto (active feet), forza eccentrica e isometrica del treno inferiore.

## Ball security — protocollo dei 4 punti

Posizione "High and Tight" con quattro punti di contatto simultanei:

| Punto | Ruolo |
|---|---|
| Mano | Copre la punta del pallone, previene strappi frontali |
| Avambraccio | Brace laterale rigido contro le costole |
| Bicipite | Blocca la parte alta del pallone, previene estrazione verticale |
| Petto | Ancoraggio finale, usa la massa corporea per stabilizzare |

Ogni drill di agility e footwork va eseguito mantenendo questa posizione: una presa lasca sposta il centro di massa fuori dalla midline e peggiora la qualità dei cambi di direzione.

## Meccanica push-pull e Dynamic Trunk Control (DTC)

Nel contatto, un braccio funge da lock (High and Tight) mentre l'altro agisce da arma (stiff-arm), creando una force-couple. Il DTC è ciò che impedisce che la forza generata dallo stiff-arm faccia collassare il centro di massa dell'atleta stesso: alto DTC significa che la forza si distribuisce sulla catena cinetica inferiore invece di piegare il busto.

## Field transfer — nessuna settimana solo palestra

Ogni settimana utile per un RB deve includere: power day, field speed/acceleration, esposizione a drill di COD o decelerazione, upper body con transfer, lavoro di resilienza tissutale. Gerarchia di transfer: tecnica di campo → espressione esplosiva → forza transferabile → prehab strutturale.

## Lavoro strutturale mandatorio

- Isometrici massimali per stiffness tendinea (vedi `elite-sc-system`).
- Lavoro sul soleo (vedi `clinical-prehab-system`).
- Copenhagen adduction protocol.
- Foot intrinsics / short foot activation.
- Collision shielding: rinforzo cervicale (chin tucks, isometrici multiplanari) e mobilizzazione T-spine per proteggere la colonna lombare durante stiff-arm e collisioni.
- Sprint e resisted sprint training integrati nel ciclo.

## Programmazione

**In-season**: MED, esposizione heavy non eliminata, intent esplosivo mantenuto, volume sotto controllo. **Off-season**: accumulation di capacità (stiffness, forza, CSA), progressione verso high-velocity transfer.

## Scope

Skill dedicata a football players e RB. Per la governance settimanale usa `programming-audit-council`. Per i parametri VBT specifici usa `vbt-rfd-open-sets`. Per COD/footwork dettagliato usa `football-cod-footwork`. Per dolore, return-to-run e MTSS usa `clinical-prehab-system`. Per architettura tendinea approfondita usa `tendon-power-architecture`.
