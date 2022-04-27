import folium
import pandas

# TODO: ask for user input on where the starting location of the map should be
# Budapest coordinates
map = folium.Map(location=[47.497913, 19.040236], zoom_start=7, tiles='Stamen Terrain')

volcano_data = pandas.read_csv("volcano_markers.csv")
volcano_name = list(volcano_data["NAME"])
volcano_lat = list(volcano_data["LAT"])
volcano_lon = list(volcano_data["LON"])
volcano_elev = list(volcano_data["ELEV"])

fg = folium.FeatureGroup(name="Web Map")

for n, e, lt, ln in zip(volcano_name, volcano_elev, volcano_lat, volcano_lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup=f"{n} - {e}m", icon=folium.Icon(color="orange")))

map.add_child(fg)

map.save("map1.html")