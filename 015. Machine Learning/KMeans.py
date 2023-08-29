import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.cluster import KMeans

class KMeansClustering:
    def __init__(self):
        # Wholesale customers 데이터셋 가져오기 (출처: UCI ML Repository)
        uci_path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00292/Wholesale%20customers%20data.csv'
        self.df = pd.read_csv(uci_path, header=0)

    def explore_data(self):
        # 데이터 살펴보기
        print(self.df.head())
        print('\n')

        # 데이터 자료형 확인
        print(self.df.info())
        print('\n')

        # 데이터 통계 요약정보 확인
        print(self.df.describe())
        print('\n')

    def preprocess_data(self):
        # 분석에 사용할 속성을 선택
        X = self.df.iloc[:, :]

        # 설명 변수 데이터를 정규화
        X = preprocessing.StandardScaler().fit(X).transform(X)

        return X

    def perform_clustering(self, X):
        # k-means 군집 모형 생성
        kmeans = KMeans(init='k-means++', n_clusters=5, n_init=10)

        # 모형 학습
        kmeans.fit(X)

        # 예측 (군집)
        cluster_label = kmeans.labels_

        # 예측 결과를 데이터프레임에 추가
        self.df['Cluster'] = cluster_label

    def visualize_clusters(self):
        # 그래프로 표현 - 시각화
        self.df.plot(kind='scatter', x='Grocery', y='Frozen', c='Cluster', cmap='Set1',
                     colorbar=False, figsize=(10, 10))
        plt.show()
        plt.close()

        # 큰 값으로 구성된 클러스터(0, 4)를 제외하여 시각화
        mask = (self.df['Cluster'] == 0) | (self.df['Cluster'] == 4)
        ndf = self.df[~mask]

        ndf.plot(kind='scatter', x='Grocery', y='Frozen', c='Cluster', cmap='Set1',
                 colorbar=False, figsize=(10, 10))
        plt.show()
        plt.close()

# 클래스 인스턴스 생성
kmeans_clustering = KMeansClustering()

# 데이터 탐색
kmeans_clustering.explore_data()

# 데이터 전처리
X = kmeans_clustering.preprocess_data()

# 군집 수행
kmeans_clustering.perform_clustering(X)

# 군집 시각화
kmeans_clustering.visualize_clusters()
