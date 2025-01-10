import csv

class Station():
    def __init__(self, naam: str, y: float, x: float, connecties: dict[str, float] | None = None) -> None:
        if connecties is None:
            connecties = {}
        self.naam = naam
        self.y = y
        self.x = x
        self.connecties = connecties

    def __str__(self):
        return f"({self.naam}, {self.y}, {self.x}, {self.connecties})"

    def __repr__(self):
        return self.__str__()

    def get_stations() -> list['Station']:

        stations = []

        with open('../data/StationsHolland.csv', 'r') as csv_file_stations_Holland:
            csv_reader = csv.reader(csv_file_stations_Holland)

            next(csv_reader)

            for row in csv_reader:
                naam = row[0]
                y = float(row[1])
                x = float(row[2])
            
                station = Station(naam, y, x)

                stations.append(station)
            
            # for station in stations: print(f'Station: {station.naam}, x: {station.x}, y: {station.y}')
        
        with open('../data/ConnectiesHolland.csv', 'r') as csv_file_connecties_Holland:
            csv_reader = csv.reader(csv_file_connecties_Holland)

            next(csv_reader)

            for row in csv_reader:
                station1 = row[0]
                station2 = row[1]
                afstand = float(row[2])

                for station in stations:
                    if station.naam == station1:
                        station.connecties[station2] = afstand
                    # elif station.naam == station2:
                    #     station.connecties[station1] = afstand

        return stations

## test

if __name__ == "__main__":
    
    stations = Station.get_stations()

    for station in stations:
        print(f'Station: {station.naam}, y: {station.y}, x: {station.x}, connecties: {station.connecties}')