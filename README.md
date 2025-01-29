# BetterNS

![Beste Plan](path/to/image.jpg)

In de RailNL case moet er een dienstregeling worden gemaakt voor de intercity treinen in Nederland. De bedoeling van deze case is om een dienstregeling te maken voor Nederland waarbij er rekening moet worden gehouden met een aantal constraints. In heel Nederland mogen er niet meer dan 20 trajecten zijn en een traject mag niet een langere reistijd hebben dan 180 minuten. Het doel is om de score K zo hoog mogelijk te krijgen. De formule van de K is als volgt:

$$K = p * 10000 – (T * 100 + Min)​$$

Hierbij is p de fractie bereden verbindingen (tussen 0 en 1). T is het aantal trajecten en Min is de som van de reistijden van alle trajecten in minuten.

## algoritmes

Er zijn vier verschillende algoritmes geïmplementeerd om de dienstregeling te optimaliseren.

### Random

uitleg random

### Greedy

uitleg greedy

### Hillclimber

uitleg hillclimber

### Breadth First

uitleg breadth first

## Aan de slag

### Vereisten

Deze code is geschreven in Python 3.12.3. In requirements.txt staan alle benodigde libraries die nodig zijn om de code te runnen.

Om deze libraries te installeren gebruik je de volgende command:

```bash
pip install -r requirements.txt
```

### Algemeen Gebruik

Om de code te kunnen runnen gebruik je de volgende algemene command:

```bash
python3 main.py <algorithm> <runs> 
```

Het invoeren van aantal runs is optioneel, standaard is het aantal runs 1.
Dus om bijvoorbeeld het random algoritme te runnen met 100 iteraties gebruik je de volgende command:

```bash
python3 main.py random 100 
```

Met uitzondering van het breadth first algoritme. Deze moet met aanhalings tekens worden getypt in de terminal. Dus om het breadth first algoritme te runnen met 10 iteraties gebruik je de volgende command:

```bash
python3 main.py "breadth first" 10
```

Hier is de link naar de output.csv file:
[output.csv](https://drive.google.com/file/d/1t7gX7bm0S-SrIda9_g1jyAehxsswfuCS/view?usp=drive_link)

Deze moet worden opgeslagen in de results map. Zie de structuur van de mappen hieronder.

## Experimenten runnen

Om de experimenten te runnen gebruik je de volgende command:

```bash
commandos voor experimenten runnen
```

## Structuur

Onze mappen structuur ziet er als volgt uit:

```bash
. 
└── Better NS/ 
    ├── code/ 
    │   ├── algorythm/ 
    │   │   ├── breadth_first.py 
    │   │   ├── greedy.py 
    │   │   ├── hillclimber.py 
    │   │   └── randomise.py 
    │   ├── classes/ 
    │   │   ├── connections.py 
    │   │   ├── state.py 
    │   │   └── stations.py 
    │   ├── visualisation/ 
    │   │   ├── graphs.py 
    │   │   ├── plot.py 
    │   │   └── visualisation.py 
    │   └── save_load_data.py 
    ├── data/ 
    │   ├── ConnectiesHolland.csv 
    │   ├── ConnectiesNationaal.csv 
    │   ├── StationsHolland.csv 
    │   └── StationNationaal.csv 
    ├── results/ 
    │   ├── presentation/ 
    │   │   ├── images/ 
    │   │   └── presentation_betterns.pptx 
    │   ├── hillclimber_scores_output.csv 
    │   ├── Map_Netherlands.html 
    │   └── output.csv 
    ├── .gitignore 
    ├── main.py 
    ├── README.md 
    └── requirements.txt 
```

## Auteurs

BetterNS is gemaakt door:

- Nour Jamal
- Rick van Engelenburg
- Wassim Belloum
