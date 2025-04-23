
# BikeProductionProject

Questo progetto è stato creato come Tesi per il Corso di Laurea in Informatica per le Aziende Digitali, l'obiettivo era sviluppare un codice python per simulare un processo produttivo nel settore secondario. Nello specifico il software è studiato per ottimizzare i processi produttivi di un’azienda che costruisce biciclette grazie alla simulazione e analisi della produzione in lotti. Ho deciso di utilizzare per il mio progetto questo tipo di azienda perché rappresenta un settore manifatturiero in cui si integrano processi industriali, logiche artigianali, automazione e controllo della qualità. 
Per interagire con il codice python, sono state realizzate 2 versioni: 

- App FullStack:
    - Front End - HTML, CSS e JavaScript Vanilla;
    - Back End - Python con libreria FastAPI.
- Interfaccia da Terminale. 


## Esegui la Full Stack App con Docker

Clona il progetto

```bash
  git clone https://github.com/tommy987-droid/BikeProductionProject
```

Vai alla cartella di progetto

```bash
  cd BikeProductionProject
```

Avvia i Container Docker

```bash
  docker compose up
```

Vai all'URL del Front End

```bash
  # Linux
  xdg-open http://localhost:80/
  
  # Windows
  start http://localhost:80/

  # macOS
  open http://localhost:80/
```

## Esegui APP Python da Terminale con Docker

Clona il progetto

```bash
  git clone --single-branch --branch CLI https://github.com/tommy987-droid/BikeProductionProject
```

Vai alla cartella di progetto

```bash
  cd BikeProductionProject
```

Avvia i Container Docker

```bash
  docker compose up
```

Avvia App

```bash
  docker exec -ti app-cli sh -c 'cd app && python makeBikeCli.py'
```

## Esegui APP Python da Terminale in Locale

Clona il progetto

```bash
  git clone --single-branch --branch CLI https://github.com/tommy987-droid/BikeProductionProject
```

Vai alla cartella di progetto

```bash
  cd BikeProductionProject
```

Installa librerie

```bash
  pip install -r requirementsCli.txt
```

Se vuoi usare un DB MySQL reale (è opzionale)

#### Modifica il file configDB.txt con le informazioni del tuo DB

Avvia App

```bash
  python makeBikeCli.py
```


## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## FAQ

#### Cosa serve per far girare l'App da Terminale in Locale?

Si può utilizzare con un db simulato semplicemente installando Python e seguendo le indicazioni precedenti "*Esegui APP Python da Terminale in Locale*", oppure se si vuole utilizzare un db MySQL reale oltre a installare Python bisogna modifica il file configDB.txt con le informazioni del DB e poi eseguire l'app seguendo le indicazioni precedenti "*Esegui APP Python da Terminale in Locale*".

#### Cosa serve per far girare con Docker l'App da Terminale o l'App FullStack?

Basta avere installato Docker e Docker Compose e poi:
- per l'App da Terminale seguire le indicazioni precedenti "*Esegui APP Python da Terminale con Docker*";
- per l'App FullStack seguire le indicazioni precedenti "*Esegui la Full Stack App con Docker*".


## Authors

- [@tommy987-droid](https://github.com/tommy987-droid)

