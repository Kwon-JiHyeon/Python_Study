import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

class NonlinearRegressionAnalysis:
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
        X = self.ndf[['weight']]
        y = self.ndf['mpg']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)
        return X_train, X_test, y_train, y_test

    def nonlinear_regression(self):
        # 비선형회귀분석
        X_train, X_test, y_train, y_test = self.split_dataset()

        # 다항식 변환
        poly = PolynomialFeatures(degree=2)
        X_train_poly = poly.fit_transform(X_train)
        X_test_poly = poly.fit_transform(X_test)

        pr = LinearRegression()
        pr.fit(X_train_poly, y_train)
        r_square = pr.score(X_test_poly, y_test)
        print("R-Square:", r_square)

        y_hat_test = pr.predict(X_test_poly)

        fig = plt.figure(figsize=(10, 5))
        ax = fig.add_subplot(1, 1, 1)
        ax.plot(X_train, y_train, 'o', label='Train Data')
        ax.plot(X_test, y_hat_test, 'r+', label='Predicted Value')
        ax.legend(loc='best')
        plt.xlabel('weight')
        plt.ylabel('mpg')
        plt.show()

        X_ploy = poly.fit_transform(X)
        y_hat = pr.predict(X_ploy)

        plt.figure(figsize=(10, 5))
        ax1 = sns.kdeplot(y, label="y")
        ax2 = sns.kdeplot(y_hat, label="y_hat", ax=ax1)
        plt.legend()
        plt.show()

# 클래스 인스턴스 생성
nonlinear_analysis = NonlinearRegressionAnalysis()

# 비선형회귀분석 수행
nonlinear_analysis.nonlinear_regression()
