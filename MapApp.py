import folium
import pandas

map = folium.Map(location = [22.58,88.41], zoom_start=8)
data = pandas.read_csv("Volcanoes.txt")
lat = data["LAT"]
lon = data["LON"]
loc = data["NAME"]+","+data["LOCATION"]
elev = data["ELEV"]

def displayColor(el):
    if el<1000:
        return 'lightgreen'
    elif 1000<=el and el<2000:
        return 'darkgreen'
    elif 2000<=el and el<3000:
        return 'orange'
    else:
        return 'red'


fgv = folium.FeatureGroup(name="Volcanoes")

for lt , lo,l,el in zip(lat,lon,loc,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,lo],popup=l,fill_color=displayColor(el),color='grey',fill_opacity=0.7,radius=6))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<3000000
else 'orange' if 3000000<= x['properties']['POP2005'] < 5000000
else 'red'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
