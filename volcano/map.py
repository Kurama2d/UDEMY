import folium
import pandas

data = pandas.read_csv('volcanoes_world.txt')
lat = list(data['Latitude'])
lon = list(data['Longitude'])
high = list(data['Elev'])

def color_check():
    return 'green'

map1 = folium.Map(location=[59.9, 30.3], tiles="Stamen Terrain")
fg = folium.FeatureGroup(name='My map')

for lt,ln, hg in zip(lat,lon, high):
    if hg > 3000.0:
        fg.add_child(folium.Marker(location=[lt,ln], popup=str(hg) + 'm', icon=folium.Icon(color='pink')))

map1.add_child(fg)


map1.save('Map1.html')


