---
name: energy-systems-recovery
description: "Bioenergetics and recovery skill for power and collision-sport athletes. Covers the three energy systems (ATP-CP/glycolytic/aerobic), Repeated Sprint Ability (RSA) recovery rules and protocols by context, creatine loading, parasympathetic downregulation, sleep protocols, anti-inflammatory nutrition, and systemic recovery stacking for professional longevity. Use when programming energy-system work, RSA, or recovery/nutrition protocols around training load for power athletes, RB/football, and hybrid/HYROX athletes needing RSA or engine work."
compatibility: "Amp (.agents/skills, ~/.config/agents/skills) and Claude Code (~/.claude/skills)"
argument-hint: [conditioning, RSA, recovery protocol, sleep, inflammation, creatine, energy system]
---

# Energy Systems & Recovery

## Missione

Il recupero non è passivo: è una regolazione programmata del sistema nervoso. L'allenamento ad alta intensità pone l'atleta in uno stato cronico di attivazione simpatica; senza un deliberato shift parassimpatico, l'adattamento reale non avviene.

## I tre sistemi energetici (richiamo operativo)

- **ATP-CP (fosfageno)**: domina i primi 6-10 secondi di sforzo massimale. Uno sprint all-out di 6 secondi riduce le riserve muscolari di fosfocreatina fino al 55%.
- **Glicolitico anaerobico**: subentra da 10s a ~2min, produttore principale di lattato/idrogenioni.
- **Aerobico**: dominante oltre i 2 minuti, il vero motore per HYROX e lavoro capacità (vedi `hyrox-hybrid-system`).

## Specificità metabolica per il football/power athlete

Gli atleti di potenza rispondono male al conditioning generico (HIIT non specifico, corsa continua a fondo). Il sistema energetico dominante nel football è ATP-CP con contributo glicolitico, non ossidativo puro.

### Repeated Sprint Ability (RSA)

Il conditioning va costruito attorno a rapporti lavoro-recupero che rispecchiano la struttura reale del gioco: burst di 5-10 secondi seguiti da 25-35 secondi di recupero, in linea con il play clock di 30 secondi tipico del football. Questo è metabolicamente e neurologicamente diverso da un protocollo HIIT generico, ed è il motivo per cui atleti di potenza spesso "rispondono male" a HIIT non specifico: non è il sistema energetico giusto per il loro sport.

Con recuperi brevi tra sprint ripetuti, il contributo energetico del sistema ATP-CP diminuisce progressivamente e il fabbisogno energetico per mantenere la prestazione si sposta sul sistema glicolitico/aerobico: la qualità del 5°-6° sprint di una serie dipende dalla capacità di risintesi della fosfocreatina, non dalla potenza alattacida pura. Gli atleti con alta RSA mostrano una capacità superiore di tamponare l'accumulo di ioni idrogeno prodotti dalla via glicolitica, non solo una fosfocreatina più abbondante — questo è l'adattamento chiave da allenare con lavoro ripetuto submassimale.

**Regola aurea di recupero sprint**: 1-2 minuti di recupero per ogni 10 metri sprintati. Per un 40m sprint, questo significa 4-8 minuti di recupero completo tra ripetute se l'obiettivo è potenza pura (non RSA-specifico). Il recupero della fosfocreatina segue una curva esponenziale: circa il 50% è ripristinato a 30 secondi, il recupero funzionale quasi completo richiede fino a 2 minuti.

### Protocolli RSA per contesto

| Obiettivo | Distanza/durata | Recupero | Serie x Rip |
|---|---|---|---|
| Potenza pura (ATP-CP) | 10-20m sprint | 1-2min/10m (recupero completo) | 4-6x |
| RSA sport-specifica (RB/football) | 20-40m sprint | 15-30s (recupero incompleto) | 6-10x, 2-3 blocchi |
| Capacità glicolitica | 200-400m | 2-4min | 4-6x |
| Motore aerobico (HYROX) | Zona 2 continuo | — | 30-90min |

## Creatina: unico integratore con evidenza solida per potenza

Un protocollo di carico tipico è 20 g/die (4 x 5g) per 4-6 giorni, seguito da mantenimento; utile anche per atleti endurance/ibridi, non solo per potenza pura.

## Regolazione neurologica e recupero

### CARs (Controlled Articular Rotations)

Mobilizzazione articolare che ripristina i limiti naturali di movimento e "pulisce" il debris articolare, mantenendo accesso al range di movimento richiesto per l'elusività.

### Downregulation respiratoria

Protocolli di respirazione focalizzata per abbassare l'attivazione simpatica, ridurre la frequenza cardiaca e segnalare al corpo l'ingresso nel ciclo "rest and digest" di riparazione tissutale. Questi protocolli impattano direttamente la readiness dell'atleta per la sessione successiva e sono tra i principali driver della longevità di carriera.

## Recupero: gerarchia di priorità

1. **Sonno** — leva più potente e meno negoziabile; sotto le 7h per 3+ notti consecutive impone taglio del 10-15% del volume settimanale (vedi Weekly Continuity Check in `programming-audit-council`).
2. **Nutrizione post-sforzo** — carboidrati per risintesi glicogeno + proteine per sintesi proteica muscolare, entro la finestra metabolica post-sessione.
3. **Recupero attivo Zona 1-2** — smaltimento metabolico, non stimolo aggiuntivo.
4. **Gestione carico settimanale** — mai progredire per calendario se i marker di recupero non sono verdi (regola già codificata nel Council).

## Il protocollo di recupero elite (bio-maintenance)

| Frequenza | Intervento |
|---|---|
| Giornaliero | 1.5 galloni di acqua con protocollo di idratazione specifico |
| Giornaliero | 9-10 ore di sonno ("Bear Rule") — non negoziabile, reset primario del sistema nervoso |
| Giornaliero | Esposizione al freddo (crio/ice bath) seguita da sauna a infrarossi |
| Settimanale | Lavoro sui tessuti molli e massoterapia |
| Trimestrale | Blood mapping completo per monitorare infiammazione sistemica e micronutrienti |

### Nutrizione anti-infiammatoria

Approccio mandatorio nelle fonti: eliminazione di glutine, soia, latticini, con controlli ematici periodici per adattare le scelte nutrizionali a sensibilità e stato di salute intestinale in evoluzione.

### Strumenti di restauro cellulare

Camera iperbarica (HBOT) e crioterapia utilizzati per accelerare la guarigione di micro-lesioni a livello cellulare, riducendo il tempo di recupero tra sessioni ad alta intensità.

## Bioenergetica per profilo atleta

| Profilo | Sistema dominante | Priorità training |
|---|---|---|
| Potenza pura (sprint, salti, OL) | ATP-CP | Recuperi lunghi, qualità massima, no accumulo fatica |
| RB/football (RSA) | ATP-CP + glicolitico | Recuperi incompleti mirati, buffering lattato |
| Ibrido/HYROX | Aerobico + glicolitico | Zona 2 volume + soglie LT1/LT2 (vedi `hyrox-hybrid-system`) |

## Perché la gestione dell'infiammazione è strategica

L'infiammazione sistemica cronica è il principale nemico della longevità professionale: un atleta che non gestisce il proprio ambiente interno rischia il collasso della capacità prestativa nella parte finale della stagione, indipendentemente dalla qualità della programmazione in palestra.

## Integrazione con la programmazione

Il recupero non è un'aggiunta opzionale al piano settimanale: va programmato come una vera giornata di recovery con CARs, respirazione, mobilità e downregulation (vedi `programming-audit-council`), non semplicemente come "giorno senza allenamento".

## Scope

Skill dedicata a bioenergetica e recupero avanzato. Per la logica generale di bioenergetica di base usa `elite-sc-system`. Per governance della programmazione settimanale usa `programming-audit-council`. Per HYROX/ibridi, dove la gestione della fatica concorrente è centrale, usa `hyrox-hybrid-system`.

## Riferimenti

Protocolli di recupero elite (bio-maintenance, downregulation, CARs) da report interni sullo Space; dati su ATP-PCr, RSA, recupero fosfocreatina e creatina verificati da fonti esterne (PMC, 8weeksout, sci-bot.ru). Nessun dato è stato inventato.
