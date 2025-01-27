import folium
import random

def random_color():
    """Genereer een willekeurige hex-kleur."""
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def map_stations(stations, train_plan):
    """
    Maakt een Folium-kaart met markers voor stations en tekent verbindingen
    (trajecten) tussen stations in willekeurige kleuren.
    """
    # Centraal op Nederland
    m = folium.Map(location=[52.0, 5.3], zoom_start=8)

    # Voeg station-markers toe
    for station in stations:
        name = station.name
        x = station.x
        y = station.y

        folium.CircleMarker(
            location=[y, x],
            radius=4,
            color="yellow",
            fill=True,
            fill_color="blue",
            fill_opacity=0.9,
            tooltip=f"Station: {name}",
            popup=name
        ).add_to(m)

    # Teken de trajecten
    for traject in train_plan:
        line_color = random_color()
        
        for connection in traject:
            station_a = connection[0]
            station_b = connection[1]
            
            station_a_x = station_a_y = None
            station_b_x = station_b_y = None

            # Zoek de coördinaten van station A en B
            for station in stations:
                if station_a == station.name:
                    station_a_x = station.x
                    station_a_y = station.y
                if station_b == station.name:
                    station_b_x = station.x
                    station_b_y = station.y

            # Teken alleen de lijn als beide stations gevonden zijn
            if station_a_x is not None and station_b_x is not None:
                folium.PolyLine(
                    locations=[[station_a_y, station_a_x],
                               [station_b_y, station_b_x]],
                    color=line_color,
                    weight=3,
                    opacity=0.6,
                    tooltip=f"connectie: {station_a}, {station_b}"
                ).add_to(m)

    # Sla de kaart op
    m.save('kaart_nederland.html')
