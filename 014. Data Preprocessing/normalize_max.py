import pandas as pd
import numpy as np

class HorsepowerScaler:
    def __init__(self, csv_path):
        # read_csv() 함수로 df 생성
        self.df = pd.read_csv(csv_path, header=None)
        
        # 열 이름을 지정
        self.df.columns = ['mpg','cylinders','displacement','horsepower','weight',
                           'acceleration','model year','origin','name'] 
    
    def preprocess_data(self):
        # horsepower 열의 누락 데이터('?') 삭제하고 실수형으로 변환
        self.df['horsepower'].replace('?', np.nan, inplace=True)
        self.df.dropna(subset=['horsepower'], axis=0, inplace=True)
        self.df['horsepower'] = self.df['horsepower'].astype('float')
        
    def scale_horsepower(self):
        # horsepower 열의 최대값의 절대값으로 모든 데이터를 나눠서 저장
        max_horsepower = abs(self.df['horsepower'].max())
        self.df['horsepower'] = self.df['horsepower'] / max_horsepower

# 클래스 인스턴스 생성
scaler = HorsepowerScaler('./auto-mpg.csv')

# 데이터 전처리
scaler.preprocess_data()

# 데이터 스케일링
scaler.scale_horsepower()

# 스케일링된 결과 출력
print(scaler.df['horsepower'].head())
print('\n')
print(scaler.df['horsepower'].describe())
