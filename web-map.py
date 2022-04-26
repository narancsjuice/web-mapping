import folium

# TODO: ask for user input on where the starting location of the map should be
# Budapest coordinates
map = folium.Map(location=[47.497913, 19.040236], zoom_start=7, tiles='Stamen Terrain')

map.save("map1.html")