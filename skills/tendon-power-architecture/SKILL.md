---
name: tendon-power-architecture
description: "Tendon biomechanics and power development skill. Covers stiffness vs compliance trade-off, maximal isometrics protocol, supra-maximal eccentric loading, total body tension (G.L.A.G.S.), and foot mechanics for elite force transmission in power-speed athletes."
compatibility: "Amp (.agents/skills, ~/.config/agents/skills) and Claude Code (~/.claude/skills)"
argument-hint: [tendon stiffness, isometrics, eccentric overload, RFD]
---

# Tendon Power Architecture

## Missione

Il tendine è la trasmissione, il muscolo è il motore. Per un atleta di potenza (RB, sprinter, power athlete) la stiffness tendinea è la priorità strategica perché determina il Rate of Force Development.

## Le tre funzioni del tendine

1. **Energy storage and return**: durante il ciclo stiramento-accorciamento, tendini rigidi immagazzinano energia elastica e la restituiscono, abbassando il costo metabolico dello sprint.
2. **Power amplification**: il tendine permette all'unità muscolo-tendinea di superare l'output del solo muscolo, agendo da amplificatore di potenza nello sprint.
3. **Power absorption**: dissipa energia come calore durante stop improvvisi o impatti pesanti, proteggendo le fibre muscolari — un meccanismo di sicurezza essenziale nell'assorbire un contatto.

### Trade-off stiffness vs compliance

| Proprietà | Caratteristica | Chi ne beneficia |
|---|---|---|
| Stiffness | Alta resistenza alla deformazione | RFD massimo, basso costo metabolico dello sprint — RB, sprinter |
| Compliance | Alta elasticità, storage energetico | Economia su lunghe distanze — endurance athlete |

Un RB non va programmato per compliance: il suo bisogno esplosivo richiede stiffness.

## Maximal Isometrics — gold standard

I tendini sono metabolicamente più lenti del muscolo e richiedono strain meccanico sostenuto per innescare il turnover del collagene. La pliometria tradizionale è spesso insufficiente (stimolo troppo breve), mentre il lavoro di ipertrofia ad alto volume affatica il muscolo prima che il tendine sia sufficientemente stimolato.

**Protocollo**: 3 set x 5 ripetizioni, 3 secondi di hold massimale, applicato consistentemente per 10-12 settimane. Fisiologicamente aumenta la cross-sectional area del tendine e la qualità del collagene di Tipo I, permettendo di tollerare le forze eccentriche supra-massimali dei cambi di direzione a velocità di gara.

**Nota strategica**: isometria eccessiva può over-irrigidire il sistema e penalizzare la curva forza-tempo. Va bilanciata con lavoro balistico per mantenere la velocità.

## Eccentric overload per assorbimento della forza

Per preparare l'atleta alla fase di power absorption di un placcaggio, serve training che superi le capacità puramente concentriche. **Protocollo**: eccentrici supra-massimali al 120% del 1RM sui movimenti fondamentali, focalizzati sulla discesa controllata di un carico che l'atleta non potrebbe muovere in concentrica. Questo forza l'unità muscolo-tendinea a stabilizzare forze enormi — la base della prevenzione infortuni.

### Lift di riferimento
1. **Two-Box Cleans**: la fase di ricezione replica funzionalmente l'assorbimento di un contatto, insegnando a stabilizzare sotto carico improvviso.
2. **High Bar Squat**: sviluppa produzione di forza verticale e integrità strutturale della catena inferiore.
3. **RDL**: motore primario dell'hinge per l'accelerazione dalla posizione a 3 punti, target sulla catena posteriore essenziale nei primi tre passi.

## Total body tension — G.L.A.G.S. e meccanica del piede

La forza è un'abilità neurologica caratterizzata dalla capacità di generare tensione totale (irradiazione). Un movimento esplosivo partito da un core disattivato disperde energia in una base instabile.

Sequenza di attivazione per creare una piattaforma solida: Grip (stringere la barra attiva la cuffia dei rotatori e stabilizza la spalla per irradiazione neurologica) → Lats (ponte tra treno superiore e bacino) → Abs (pressione intra-addominale protegge la colonna e assicura trasferimento di forza) → Glutes (motore primario di spinta e stabilizzatore d'anca).

### Meccanica del piede
Il piede è l'unico punto di contatto con il terreno. La tecnica "short foot" (attivazione dell'arco, estensione dell'alluce) influenza l'intera catena cinetica e previene la rotazione tibiale interna, fattore critico nella prevenzione ACL durante i tagli laterali ad alto torque. Lavoro scalzo o in calzature minimal è utile per ripristinare la mappa propriocettiva del piede, spesso atrofizzata dall'uso costante di scarpe che agiscono come un "cast".

## Scope

Skill dedicata a stiffness tendinea e architettura della potenza. Per il quadro football/RB completo usa `football-rb-system`. Per parametri VBT usa `vbt-rfd-open-sets`. Per clinica e prevenzione usa `clinical-prehab-system`.
