---
name: biomechanics-movement-screen
description: Use when assessing an athlete's movement quality, screening for asymmetries, or deciding whether to clear/restrict an exercise based on baseline movement patterns. Grounded in FMS evidence and the 6-pattern framework (Press/Pull/Squat/Hinge/Rotation/Locomotion).
---

# Biomechanics & Movement Screen

## Quando attivare questa skill
Insieme a `elite-sc-system`, all'intake di un nuovo atleta, dopo un infortunio, o prima di aumentare aggressivamente il carico su un pattern specifico.

## Cosa dice davvero l'evidenza sul FMS
Il Functional Movement Screen è affidabile e clinicamente utile, ma NON è uno strumento standalone di previsione infortuni [web:34]. Questo è un punto critico: il FMS da solo non basta a prevedere chi si infortunerà.

Il valore del FMS aumenta quando combinato con Y-Balance test, storia di infortuni pregressi, dolore attuale e fattori di stile di vita [web:34]. Il dolore durante il movimento e le limitazioni maggiori (punteggio 1 o asimmetrie) sono costantemente collegati a rischio più alto, con alcuni studi che riportano fino a 2.7 volte maggiore probabilità di infortunio in certi gruppi [web:34].

Nel contesto sport di squadra, il punteggio composito FMS e le asimmetrie sono risultati particolarmente utili per stimare il rischio infortunio in rugby, football americano e hockey su ghiaccio [web:37] — rilevante direttamente per la popolazione RB/football di questo Space.

## Protocollo operativo (non solo FMS puro)
1. **Movement quality prima** — screening dei 6 pattern fondamentali (Press, Pull, Squat, Hinge, Rotation, Locomotion) con carico corporeo o carico minimo.
2. **Aggiungere contesto** — storia infortuni, dolore corrente, qualità del sonno, carico di vita esterno all'allenamento [web:34].
3. **Decisione informata** — non usare mai un singolo punteggio come veto assoluto; usarlo come uno dei segnali insieme ad asimmetria e dolore.

## I 6 pattern: cosa cercare in ciascuno

| Pattern | Cosa valutare | Red flag |
|---|---|---|
| Squat | Profondità, controllo ginocchio-anca, mobilità caviglia | Ginocchia valghe, perdita di lordosi lombare |
| Hinge | Dissociazione anca-colonna, hamstring loading | Flessione lombare precoce, "buttress" |
| Press | Stabilità scapolare, ROM spalla | Compenso lombare, scapola alata |
| Pull | Retrazione scapolare, controllo eccentrico | Shrug compensatorio, ROM incompleto |
| Rotation | Dissociazione toraco-pelvica | Rotazione globale rigida, dolore lombare |
| Locomotion | Simmetria del passo, cadenza, ammortizzazione | Asimmetria evidente, atterraggio rumoroso |

## Asimmetria come segnale prioritario
Un'asimmetria significativa tra lato dominante e non dominante in qualsiasi pattern è un predittore di rischio più affidabile del punteggio assoluto — questo vale soprattutto per atleti di sport con dominanza laterale marcata (RB, cambi di direzione) [web:34][web:37].

## Fattori aggiuntivi da incrociare (oltre il movimento puro)
Il BMI in fascia sovrappeso/obesità è risultato collegato a maggiore suscettibilità a infortuni di categoria alta, plausibilmente per il range di movimento limitato; la forma del piede (piede piatto) invece non ha mostrato un legame diretto con il rischio infortunio alto in uno studio su studenti sportivi [web:40] — utile per contestualizzare, non per creare automatismi diagnostici eccessivi.

## Come integrare con il resto del sistema
- Se lo screening rivela dolore riproducibile → applica subito il Sanford Filter di `clinical-prehab-system`, stop 2 giorni prima di procedere.
- Se rivela asimmetria senza dolore → non è un veto, ma un flag da monitorare nel Weekly Continuity Check e da bilanciare nella scelta degli accessori (unilaterali prioritari sul lato debole).
- Lo screening iniziale alimenta direttamente `athlete-profiling-benchmarking` come primo dato oggettivo del profilo atleta.

## Riferimenti
Evidenza sul valore predittivo del FMS verificata su fonti esterne allo Space (functionalmovement.com, Indiana State University Scholars, sportpedagogy.org.ua) [web:34][web:37][web:40].
