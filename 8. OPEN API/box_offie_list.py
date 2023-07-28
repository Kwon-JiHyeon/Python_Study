# OPEN API로 인기영화순위 불러오기

import requests

url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=c3a0fa760324363ef7cde2afa0d73297&targetDt=20230722'
resp = requests.get(url)
data = resp.json()

def find_dict(data, want_list):
    result = []
    for j in range(len(data)):
        sub_data = data[j]
        sub_result = {}
        for i in want_list:
            sub_result[i] = sub_data[i]
        result.append(sub_result)
    return result

# test
data1 = data['boxOfficeResult']['dailyBoxOfficeList']
want_list = ['rank', 'movieNm', 'openDt', 'salesAmt']
find_dict(data1, want_list)
