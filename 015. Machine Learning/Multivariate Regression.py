import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class MultipleRegressionAnalysis:
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

    def split_dataset(self):
        # 데이터셋 구분
        X = self.ndf[['cylinders', 'horsepower', 'weight']]
        y = self.ndf['mpg']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)
        return X_train, X_test, y_train, y_test

    def multiple_regression(self):
        # 다중회귀분석
        X_train, X_test, y_train, y_test = self.split_dataset()

        # 모델 학습
        lr = LinearRegression()
        lr.fit(X_train, y_train)

        # 결정계수 계산
        r_square = lr.score(X_test, y_test)
        print("R-Square:", r_square)

        # 회귀식의 계수와 상수항 출력
        coefficients = lr.coef_
        intercept = lr.intercept_
        print("X 변수의 계수 a:", coefficients)
        print("상수항 b:", intercept)

        # 예측값과 실제값의 산점도 출력
        y_hat = lr.predict(X_test)

        plt.figure(figsize=(10, 5))
        ax1 = sns.kdeplot(y_test, label="y_test")
        ax2 = sns.kdeplot(y_hat, label="y_hat", ax=ax1)
        plt.legend()
        plt.show()

# 클래스 인스턴스 생성
multiple_regression_analysis = MultipleRegressionAnalysis()

# 다중회귀분석 수행
multiple_regression_analysis.multiple_regression()
