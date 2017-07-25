import folium
import pandas
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1500.0:
        return 'green'
    elif 1500.0 <= elevation < 3000.0:
        return 'blue'
    else:
        return 'red'

feature_group1 = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    feature_group1.add_child(folium.CircleMarker(location=[lt, ln], radius=7, popup=str(el)+"m", fill_color=color_producer(el)))
feature_group2 = folium.FeatureGroup(name="Population")


map1 = folium.Map(location=[38, -100], zoom_start = 3, tiles="Mapbox Bright")

feature_group2.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig'), style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000<=x['properties']['POP2005'] < 50000000 else 'red'}))

map1.add_child(feature_group1)
map1.add_child(feature_group2)

map1.add_child(folium.LayerControl())

map1.save("Map1.html")
