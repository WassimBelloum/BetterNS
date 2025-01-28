import folium
import random
import ast
import re

def random_color():
    """Genereer een willekeurige hex-kleur."""
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def map_stations(stations, train_plan):
    """
    Maakt een Folium-kaart met markers voor stations en tekent verbindingen
    (trajecten) tussen stations in willekeurige kleuren.
    """
    # Centraal op Nederland
    m = folium.Map(location=[52.0, 5.3], zoom_start=8, tiles="CartoDB Positron")

    # Voeg station-markers toe
    for station in stations:
        name = station.name
        x = station.x
        y = station.y

        folium.CircleMarker(
            location=[y, x],
            radius=3,
            color="blue",
            fill=True,
            fill_color="blue",
            fill_opacity=0.7,
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
                    weight=2,
                    opacity=0.5,
                    tooltip=f"connectie: {station_a}, {station_b}"
                ).add_to(m)

    # Sla de kaart op
    m.save('results/kaart_nederland.html')

# From output CSV to useble data plan for map_stations()
def load_endstate(df, algorythm, test_state):
    random_rows = df[df['Algorithm'] == algorythm]
    best_random_row = random_rows.loc[random_rows['Score'].idxmax()]
    best_random_plan_string = best_random_row['Endstate']
    quoted_plan_string = re.sub(
        r'\b([A-Za-z\-\s\/]+)\b',
        r'"\1"',
        best_random_plan_string
    )
    best_plan = ast.literal_eval(quoted_plan_string)
    for line in best_plan:
        for connection1 in line:
            start, end, time1 = connection1
            for key, value in test_state.connections.items():
                station_a = value.station_a
                station_b = value.station_b
                if start == station_a and end == station_b:
                    connection1 = value
    return best_plan