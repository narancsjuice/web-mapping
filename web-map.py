import folium

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

map = folium.Map(location=[location[0], location[1]], zoom_start=7, tiles="Stamen Terrain")

map.save("map1.html")