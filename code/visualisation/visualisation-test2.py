import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib
matplotlib.use('TkAgg')




# Kaart + assen configureren
fig = plt.figure(figsize=(6, 6))
ax = plt.axes(projection=ccrs.PlateCarree())

# Kaartfeatures toevoegen
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.LAND, facecolor='lightgray')
ax.add_feature(cfeature.OCEAN, facecolor='lightblue')

# Zoom op Nederland
ax.set_extent([3, 8, 50.5, 53.7], ccrs.PlateCarree())

# Amsterdam
amsterdam_coords = (4.9041, 52.3676)
plt.plot(amsterdam_coords[0], amsterdam_coords[1], 
         marker='o', color='red', markersize=5)
plt.text(amsterdam_coords[0] + 0.1, amsterdam_coords[1], 
         'Amsterdam', fontsize=9)

# Den Haag
denhaag_coords = (4.3007, 52.0705)
plt.plot(denhaag_coords[0], denhaag_coords[1], 
         marker='o', color='blue', markersize=5)
plt.text(denhaag_coords[0] + 0.1, denhaag_coords[1], 
         'Den Haag', fontsize=9)

# Lijn tussen Amsterdam en Den Haag
plt.plot([amsterdam_coords[0], denhaag_coords[0]],
         [amsterdam_coords[1], denhaag_coords[1]],
         color='green', linewidth=2)

plt.title('Kaart van Nederland met Amsterdam en Den Haag')
plt.show()  # Toont het direct in je Python-omgeving/IDE

# Opslaan als PNG
# plt.savefig("kaart_nederland.png")
