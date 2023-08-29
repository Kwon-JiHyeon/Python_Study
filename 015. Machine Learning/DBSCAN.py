import pandas as pd
import folium
from sklearn import preprocessing
from sklearn.cluster import DBSCAN

class SchoolClusterAnalysis:
    def __init__(self):
        # 서울시내 중학교 진학률 데이터셋
        file_path = './2016_middle_shcool_graduates_report.xlsx'
        self.df = pd.read_excel(file_path, engine='openpyxl', header=0)

        # IPython Console 디스플레이 옵션 설정
        pd.set_option('display.width', None)
        pd.set_option('display.max_rows', 100)
        pd.set_option('display.max_columns', 10)
        pd.set_option('display.max_colwidth', 20)
        pd.set_option('display.unicode.east_asian_width', True)

    def explore_data(self):
        # 열 이름 배열 출력
        print(self.df.columns.values)
        print('\n')

        # 데이터 살펴보기
        print(self.df.head())
        print('\n')

        # 데이터 자료형 확인
        print(self.df.info())
        print('\n')

        # 데이터 통계 요약정보 확인
        print(self.df.describe())
        print('\n')

    def visualize_school_locations(self):
        # 지도에 위치 표시
        mschool_map = folium.Map(location=[37.55, 126.98], tiles='Stamen Terrain', zoom_start=12)

        # 중학교 위치정보를 CircleMarker로 표시
        for name, lat, lng in zip(self.df.학교명, self.df.위도, self.df.경도):
            folium.CircleMarker([lat, lng],
                                radius=5,
                                color='brown',
                                fill=True,
                                fill_color='coral',
                                fill_opacity=0.7,
                                popup=name
            ).add_to(mschool_map)

        # 지도를 html 파일로 저장
        mschool_map.save('./seoul_mschool_location.html')

    def preprocess_data(self):
        # 원핫인코딩(더미 변수)
        label_encoder = preprocessing.LabelEncoder()

        onehot_location = label_encoder.fit_transform(self.df['지역'])
        onehot_code = label_encoder.fit_transform(self.df['코드'])
        onehot_type = label_encoder.fit_transform(self.df['유형'])
        onehot_day = label_encoder.fit_transform(self.df['주야'])

        self.df['location'] = onehot_location
        self.df['code'] = onehot_code
        self.df['type'] = onehot_type
        self.df['day'] = onehot_day

    def perform_clustering(self, columns_list):
        X = self.df.iloc[:, columns_list]
        X = preprocessing.StandardScaler().fit(X).transform(X)

        dbm = DBSCAN(eps=0.2, min_samples=5)
        dbm.fit(X)
        self.df['Cluster'] = dbm.labels_

        grouped_cols = [0, 1, 3] + columns_list
        grouped = self.df.groupby('Cluster')
        for key, group in grouped:
            print('* key :', key)
            print('* number :', len(group))
            print(group.iloc[:, grouped_cols].head())
            print('\n')

        cluster_map = folium.Map(location=[37.55, 126.98], tiles='Stamen Terrain', zoom_start=12)

        colors = {-1: 'gray', 0: 'coral', 1: 'blue', 2: 'green', 3: 'red', 4: 'purple',
                  5: 'orange', 6: 'brown', 7: 'brick', 8: 'yellow', 9: 'magenta', 10: 'cyan', 11: 'tan'}

        for name, lat, lng, clus in zip(self.df.학교명, self.df.위도, self.df.경도, self.df.Cluster):
            folium.CircleMarker([lat, lng],
                                radius=5,
                                color=colors[clus],
                                fill=True,
                                fill_color=colors[clus],
                                fill_opacity=0.7,
                                popup=name
            ).add_to(cluster_map)

        cluster_map.save('./seoul_mschool_cluster.html')

# 클래스 인스턴스 생성
school_cluster_analysis = SchoolClusterAnalysis()

# 데이터 탐색
school_cluster_analysis.explore_data()

# 지도 시각화
school_cluster_analysis.visualize_school_locations()

# 데이터 전처리
school_cluster_analysis.preprocess_data()

# 클러스터링 수행 및 시각화
# 첫 번째 경우
columns_list1 = [9, 10, 13]
school_cluster_analysis.perform_clustering(columns_list1)

# 두 번째 경우
columns_list2 = [9, 10, 13, 22]
school_cluster_analysis.perform_clustering(columns_list2)

# 세 번째 경우
columns_list3 = [9, 10]
school_cluster_analysis.perform_clustering(columns_list3)
