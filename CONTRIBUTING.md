# Contribuire a sc-coach-skills

## Proporre una nuova skill sport-specifica

Il pacchetto copre oggi powerlifting, weightlifting olimpico, football/RB, HYROX/ibridi e popolazione generale. Mancano volutamente: throwing sports (lancio del peso, giavellotto), youth/adolescent athletic development, endurance puro (maratona/triathlon non ibrido), sport di combattimento — per mancanza di fonti verificate al momento della stesura, non per scelta editoriale.

Per proporne una:
1. Apri una issue con il template "New skill request", indicando lo sport/dominio e le fonti che useresti.
2. Segui la struttura delle skill esistenti (`skills/<nome>/SKILL.md`): frontmatter con `name` uguale al nome cartella e `description` che dichiara quando attivarsi; corpo con missione, protocolli/tabelle concrete, e sezione "Scope" che rimanda alle altre skill del pacchetto con cui collabora.
3. Nessun dato reale di atleti — solo framework generici.

## Correggere una skill esistente

Apri una issue con il template "Correction" o direttamente una PR. Se la correzione tocca un riferimento incrociato ad altre skill (es. `` `nome-skill` `` nel testo), assicurati che il nome esista ancora in `skills/`.

## Prima di aprire una PR

```bash
bash scripts/validate-skills.sh
```

Deve passare senza errori: controlla che il frontmatter di ogni `SKILL.md` sia coerente (nome cartella = `name`, `description` presente) e segnala riferimenti a skill che non esistono più (utile dopo un rename o una fusione di skill). Lo stesso controllo gira in CI su ogni push/PR.
