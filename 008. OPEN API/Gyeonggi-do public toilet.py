# OPEN API 사용하여 경기도공중화장실현황 지도에 찍기

# 4~26행 데이터 가공
import json

file_names = '/content/경기도공중화장실현황(제공표준).json'

def get_data(file_names):
    with open(file_names, 'r', encoding="utf-8") as f:
        datas = json.load(f)
        return(datas)
      
data = get_data(file_names)

def find_dict(data, want_list):
    result = []
    for j in range(len(data)):
        sub_data = data[j]
        sub_result = {}
        for i in want_list:
            sub_result[i] = sub_data[i]
        result.append(sub_result)
    return result

want_list = ['PBCTLT_PLC_NM', 'REFINE_LOTNO_ADDR', 'REFINE_WGS84_LAT']
find_dict(data, want_list)

import folium

def map_add(maps, data):
    for item in data:
        name = item['PBCTLT_PLC_NM']
        if item['REFINE_WGS84_LAT']:
            latitude = item['REFINE_WGS84_LAT']
            longitude = item['REFINE_WGS84_LOGT']
            folium.CircleMarker([latitude, longitude], radius=4, popup=name, color='red', fill_color='red').add_to(maps)
    return maps

def FoliumMap(data, save_file='result.html'):
    maps = folium.Map(location=[37.560, 126.982], zoom_strat=7)
    map_add(maps, data).save(save_file)

FoliumMap(data)
