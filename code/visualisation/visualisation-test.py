import folium

# Maak de kaart en centreer op Nederland
m = folium.Map(location=[52.3, 5.3], zoom_start=8)

# Voeg een marker toe voor Amsterdam
folium.Marker(
    location=[52.3676, 4.9041],
    popup='Amsterdam'
).add_to(m)

# Voeg een marker toe voor Den Haag
folium.Marker(
    location=[52.0705, 4.3007],
    popup='Den Haag'
).add_to(m)

# Teken een lijn tussen Amsterdam en Den Haag
folium.PolyLine(
    locations=[
        [52.3676, 4.9041],  # Amsterdam
        [52.0705, 4.3007]   # Den Haag
    ],
    color='blue',
    weight=3
).add_to(m)

# Sla de kaart op als HTML-bestand
m.save('kaart_nederland.html')
