# BetterNS

In de RailNL case moet er een dienstregeling worden gemaakt voor de intercity treinen in Nederland. De bedoeling van deze case is om een dienstregeling te maken voor Nederland waarbij er rekening moet worden gehouden met een aantal constraints. In heel Nederland mogen er niet meer dan 20 trajecten zijn en een traject mag niet een langere reistijd hebben dan 180 minuten.

## Aan de slag

### Vereisten

Deze code is geschreven in Python 3.12.3. In requirements.txt staan alle benodigde libraries die nodig zijn om de code te runnen.

```bash
pip install -r requirements.txt
```

### Gebruik

Om de code te kunnen gebruiken gebruik je de volgende commands:

```bash
python3 main.py <algoritme> --iterations <aantal iteraties> 
```

Standaard is het aantal iteraties 1.
Dus om bijvoorbeeld het breadth_first algoritme te runnen met 100 iteraties gebruik je de volgende command:

```bash
python3 main.py breadth_first --iterations 100
```

Hier is de link naar de output.csv file:
[output.csv](https://drive.google.com/file/d/1t7gX7bm0S-SrIda9_g1jyAehxsswfuCS/view?usp=drive_link)

### Structuur

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
    │   └── visualisation/ 
    │       ├── graphs.py 
    │       └── visualisation.py 
    ├── data/ 
    │   ├── ConnectiesHolland.csv 
    │   ├── ConnectiesNationaal.csv 
    │   ├── output.csv 
    │   ├── save_load_data.py 
    │   ├── StationsHolland.csv 
    │   └── StationNationaal.csv 
    ├── results/ 
    │   └── kaart_nederland.html 
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
