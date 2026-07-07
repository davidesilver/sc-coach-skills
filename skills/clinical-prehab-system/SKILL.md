---
name: clinical-prehab-system
description: "Clinical prehab and return-to-performance skill. Covers Sanford soreness rules, Copenhagen adduction protocol, soleus/MTSS management, tibialis and foot intrinsic work, collision shielding, and criterion-based return-to-run for football and power-speed athletes."
compatibility: "Amp (.agents/skills, ~/.config/agents/skills) and Claude Code (~/.claude/skills)"
argument-hint: [pain area, MTSS, adductors, tendon, return-to-run]
---

# Clinical Prehab System

## Missione

Ridurre il rischio infortuni e gestire il ritorno al carico con criteri oggettivi, non con ottimismo. Il tessuto non negozia con la narrativa del coach o dell'atleta.

## Sanford Soreness Rules

1. Dolore al warm-up che persiste → stop, 2 giorni off, torna allo step precedente.
2. Dolore al warm-up che scompare → resta allo step attuale, non avanzare finché non è senza dolore.
3. Dolore che scompare ma ritorna in sessione → stop, 2 giorni off, torna allo step precedente.
4. Dolore il giorno dopo → 1 giorno off, non avanzare il programma.

Queste regole governano il carico in modo oggettivo, indipendentemente dall'umore o dalla motivazione dell'atleta.

## MTSS e il fattore soleo

### Reframe clinico
La Medial Tibial Stress Syndrome (MTSS) va trattata come stress osseo a basso rischio (bone stress injury), non come banale "shin splints". Diagnosi clinica: tenderness lungo il bordo posteromediale della tibia per più di 5cm, fulcrum test positivo, dolore durante hop test. Tenderness focale sotto i 5cm suggerisce invece una frattura da stress tibiale, che richiede un profilo di carico completamente diverso.

### Il ruolo del soleo
Il soleo assorbe un carico tibiale significativamente maggiore del gastrocnemio durante la corsa ed è il principale scudo meccanico contro lo stress tibiale ripetuto. Un soleo debole o affaticato lascia che le forze di taglio raggiungano il periostio.

### Progressione criterion-based (fasi)
- **Fase I (acuta, 7-14gg)**: se dolore in ADL, boot/splint 2-4 settimane. NWB strengthening (quadricipiti/glutei), lavoro intrinseco del piede, conditioning aerobico low-impact.
- **Fase II (subacuta, sett. 2-6)**: carico progressivo dal 50%, heel raise progression (bilaterale → eccentrico → monopodalico).
- **Fase III (sett. 2-8)**: return-to-run organizzato, pliometria monopodalica.
- **Fase IV**: Heavy Resisted Sprint Training (sled 60-80% BW) per ottimizzare produzione di forza orizzontale e accelerazione 0-10m.

### Benchmark obbligatori pre-avanzamento
- 25 single-leg heel raises bilaterali senza dolore.
- 15 single-leg hops senza dolore.
- 30 minuti di cammino continuo senza riacutizzazione.
- Squat 60% BW, 6 ripetizioni con hold di 6 secondi ciascuna.

## Copenhagen Adduction Protocol

Protocollo non negoziabile per sport con tagli laterali, jump cut, frenate e torsioni. Dati di riferimento nelle fonti: +35.7% di forza eccentrica dell'adduttore, -41% di rischio infortunio all'inguine.

### Volume progressivo (8 settimane)
1. Settimane 1-2: 2x6 rip/lato, 2-3x/settimana — focus tecnico.
2. Settimane 3-5: 3x10 rip/lato — focus tolleranza al carico.
3. Settimane 6-8: 3x15 rip/lato — accumulo di volume.
4. Mantenimento: 250 ripetizioni/gamba totali per preservare l'adattamento.

Regola di programmazione: integrare il Copenhagen senza duplicare lavoro aduttorio ridondante nello stesso microciclo. Se compare dolore inguinale, obbligatorio gap di 48h prima del prossimo stimolo aduttorio.

## Tibialis, piede e controllo distale

Il lavoro sul tibiale anteriore è necessario per il controllo decelerativo, la salute della caviglia e la tolleranza nelle frenate. Il piede è il primo anello di contatto: senza attivazione del piede (short foot / foot intrinsics), peggiora la gestione del centro di massa e aumenta la torsione tibiale indesiderata, con effetti negativi sulla qualità del taglio.

## Collision shielding (protezione della colonna)

Per sport di contatto: rinforzo cervicale (chin tucks, isometrici multiplanari) per ridurre l'accelerazione tipo whiplash della testa durante impatti; mobilizzazione toracica per ripristinare estensione e rotazione, evitando che la colonna lombare compensi durante rotazioni e stiff-arm.

## Return-to-run / return-to-field

Il ritorno non è mai time-based, è sempre criterion-based. Check obbligatori: dolore sotto controllo secondo Sanford, benchmark locali superati, pattern di corsa accettabile, tolleranza alle progressioni senza flare-up. Modificatori di gait da considerare in fase di ripresa: gestione della cadenza, scelta della superficie (erba a basso impatto prima del sintetico), controllo del tronco, riduzione delle esposizioni caotiche troppo precoci.

## Scope

Skill dedicata al lato clinico/prehab. Per programmazione settimanale usa `programming-audit-council`. Per football/RB transfer usa `football-rb-system`. Per open sets e velocità usa `vbt-rfd-open-sets`. Per architettura tendinea approfondita usa `tendon-power-architecture`.
