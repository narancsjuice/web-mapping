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


# TODO: ask for user input on where the starting location of the map should be
# Budapest coordinates
map = folium.Map(location=[47.497913, 19.040236], zoom_start=7, tiles='Stamen Terrain')

volcano_data = pandas.read_csv("volcano_markers.csv")
volcano_name = list(volcano_data["NAME"])
volcano_lat = list(volcano_data["LAT"])
volcano_lon = list(volcano_data["LON"])
volcano_elev = list(volcano_data["ELEV"])

html = """<h4>Volcano information:</h4>
Name: <a href="https://www.google.com/search?q=%s" target="_blank">%s</a><br>
Height: %s m
"""

fg = folium.FeatureGroup(name="Web Map")

for n, e, lt, ln in zip(volcano_name, volcano_elev, volcano_lat, volcano_lon):
    iframe = folium.IFrame(html=html %(n, n, str(e)), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6,
                 popup=folium.Popup(iframe),fill_color=color_on_elev(e),
                            color="black", fill=True, fill_opacity=0.6))

map.add_child(fg)

map.save("map1.html")