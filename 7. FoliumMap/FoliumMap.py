# 위도, 경도를 불러와서 지도위에 위치 찍기

import folium

def map_add(maps, data):
    for item in data:
        name = item
        latitude = data[item][0]
        longitude = data[item][1]
        folium.CircleMarker([latitude, longitude], radius=4, popup=name, color='red', fill_color='red').add_to(maps)
    return maps

def FoliumMap(data, save_file='result.html'):
    maps = folium.Map(location=[37.560, 126.982], zoom_strat=7)
    map_add(maps, data).save(save_file)

# result
<img src='FoliumMap.png'> </img>
