import folium
import pandas


def color_on_elev(elevation):
    """

    :param elevation: float of volcano elevation
    :return: color: defined color based on elevation
    """
    if elevation < 1000:
        color = "green"
    elif 1000 <= elevation < 2000:
        color = "orange"
    elif 2000 <= elevation < 3000:
        color = "red"
    else:
        color = "purple"
    return color


# TODO: rework user input for location into functions
location = []
print("Enter the location coordinates for your map's starting point. If you "
      "want to skip, leave the prompt empty and you'll be defaulted to Budapest"
      " as the starting point.")

lat_text = "Enter Latitude of start location (0° to 90°): "
lon_text = "Enter Longitude  of start location (-180° to 180°): "
invalid_text = "Invalid coordinate."
lat = input(lat_text)
lon = input(lon_text)

location = [lat, lon]

invalid_coordinate = [True, True]

for index, coordinate in enumerate(location):
    while coordinate != "" and invalid_coordinate[index] is True:
        try:
            coordinate = float(coordinate)
            location[index] = coordinate
            if index == 0:
                if 90 >= location[0] >= 0:
                    invalid_coordinate[index] = False
                else:
                    coordinate = input(invalid_text + lat_text)
            elif index == 1:
                if 180 >= location[1] >= -180:
                    invalid_coordinate[index] = False
                else:
                    coordinate = input(invalid_text + " " + lon_text)
        except:
            if index == 0:
                value = lat_text
            elif index == 1:
                value = lon_text
            coordinate = input(
                f"Text is not accepted. {value}")
            continue
    else:
        if index == 0 and coordinate == "":
            lat = 47.497913
            location[index] = lat
            print(f"Latitude is set by default to {lat}.")
        elif index == 1 and coordinate == "":
            lon = 19.040236
            location[index] = lon
            print(f"Latitude is set by default to {lon}.")

map = folium.Map(location=[47.497913, 19.040236], zoom_start=7,
                 tiles='Stamen Terrain')

volcano_data = pandas.read_csv("volcano_markers.csv")
volcano_name = list(volcano_data["NAME"])
volcano_lat = list(volcano_data["LAT"])
volcano_lon = list(volcano_data["LON"])
volcano_elev = list(volcano_data["ELEV"])

html1 = """<h4>Volcano information:</h4>
Name: <a href="https://www.google.com/search?q=%s" target="_blank">%s</a><br>
Height: %s m
"""

fg1 = folium.FeatureGroup(name="Volcano Markers")
for n, e, lt, ln in zip(volcano_name, volcano_elev, volcano_lat, volcano_lon):
    iframe = folium.IFrame(html=html1 %(n, n, str(e)), width=200, height=100)
    fg1.add_child(folium.CircleMarker(location=[lt, ln], radius=6,
                 popup=folium.Popup(iframe), fill_color=color_on_elev(e),
                            color="black", fill=True, fill_opacity=0.6))

cities_data = pandas.read_csv("cities_hu.csv")
cities_name = cities_data["city"]
cities_lat = cities_data["lat"]
cities_lon = cities_data["lng"]
cities_pop = cities_data["population"]

html2 = """<h4>City information:</h4>
Name: <a href="https://www.google.com/search?q=%s" target="_blank">%s</a><br>
Population: %s
"""

fg2 = folium.FeatureGroup(name="City Markers")
for n, lt, ln, pop in zip(cities_name, cities_lat, cities_lon, cities_pop):
    iframe2 = folium.IFrame(html=html2 %(n, n, pop), width=200, height=100)
    if pop >= 10000:
        fg2.add_child(folium.Marker(location=[lt, ln], radius=6,
                                    popup=folium.Popup(iframe2),
                                    icon=folium.Icon(color="purple",
                                    icon_color="blue", icon="thumb-tack", prefix="fa" )))

map.add_child(fg1)
map.add_child(fg2)

map.save("map1.html")
