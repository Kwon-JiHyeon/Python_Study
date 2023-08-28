import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class CarMpgAnalysis:
    def __init__(self):
        # 데이터 불러오기
        self.df = pd.read_csv('./auto-mpg.csv', header=None)
        self.df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
                           'acceleration', 'model year', 'origin', 'name']
        
        # horsepower 열의 누락데이터 처리
        self.df['horsepower'].replace('?', np.nan, inplace=True)
        self.df.dropna(subset=['horsepower'], axis=0, inplace=True)
        self.df['horsepower'] = self.df['horsepower'].astype('float')
        
        # 분석에 사용할 열 선택
        self.ndf = self.df[['mpg', 'cylinders', 'horsepower', 'weight']]
        
        # IPython 디스플레이 설정 변경
        pd.set_option('display.max_columns', 10)

    def explore_data(self):
        # 데이터 정보 확인
        print(self.df.info())
        print('\n')

        # 데이터 통계 요약정보 확인
        print(self.df.describe())
        print('\n')

    def plot_scatter(self):
        # 산점도 그래프 그리기
        self.ndf.plot(kind='scatter', x='weight', y='mpg', c='coral', s=10, figsize=(10, 5))
        plt.show()

    def plot_regplot(self):
        # 회귀선을 포함한 산점도 그래프 그리기
        fig = plt.figure(figsize=(10, 5))
        ax1 = fig.add_subplot(1, 2, 1)
        ax2 = fig.add_subplot(1, 2, 2)
        sns.regplot(x='weight', y='mpg', data=self.ndf, ax=ax1)
        sns.regplot(x='weight', y='mpg', data=self.ndf, ax=ax2, fit_reg=False)
        plt.show()

    def plot_jointplot(self):
        # 조인트 그래프 그리기
        sns.jointplot(x='weight', y='mpg', data=self.ndf)
        sns.jointplot(x='weight', y='mpg', kind='reg', data=self.ndf)
        plt.show()

    def split_dataset(self):
        # 데이터셋 구분
        X = self.ndf[['weight']]
        y = self.ndf['mpg']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)
        return X_train, X_test, y_train, y_test

    def simple_linear_regression(self):
        # 단순회귀분석
        X_train, X_test, y_train, y_test = self.split_dataset()

        lr = LinearRegression()
        lr.fit(X_train, y_train)
        r_square = lr.score(X_test, y_test)
        print("R-Square:", r_square)
        print("기울기 a:", lr.coef_)
        print("y절편 b:", lr.intercept_)

        y_hat = lr.predict(X)

        plt.figure(figsize=(10, 5))
        ax1 = sns.kdeplot(y, label="y")
        ax2 = sns.kdeplot(y_hat, label="y_hat", ax=ax1)
        plt.legend()
        plt.show()

# 클래스 인스턴스 생성
car_analysis = CarMpgAnalysis()

# 데이터 탐색
car_analysis.explore_data()

# 산점도 그래프
car_analysis.plot_scatter()

# 회귀선을 포함한 산점도 그래프
car_analysis.plot_regplot()

# 조인트 그래프
car_analysis.plot_jointplot()

# 단순회귀분석
car_analysis.simple_linear_regression()
