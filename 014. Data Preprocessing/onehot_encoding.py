import pandas as pd
import numpy as np
from sklearn import preprocessing

class HorsepowerBinEncoder:
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
        
    def bin_and_encode(self):
        # np.histogram 으로 3개의 bin으로 나누는 경계 값의 리스트 구하기
        count, bin_dividers = np.histogram(self.df['horsepower'], bins=3)
        
        # 3개의 bin에 이름 지정
        bin_names = ['저출력', '보통출력', '고출력']
        
        # pd.cut 으로 각 데이터를 3개의 bin에 할당
        self.df['hp_bin'] = pd.cut(x=self.df['horsepower'],
                                   bins=bin_dividers,
                                   labels=bin_names,
                                   include_lowest=True)
        
        # 전처리를 위한 encoder 객체 생성
        label_encoder = preprocessing.LabelEncoder()       
        onehot_encoder = preprocessing.OneHotEncoder()   
        
        # label encoder로 문자열 범주를 숫자형 범주로 변환
        onehot_labeled = label_encoder.fit_transform(self.df['hp_bin'].head(15)) 
        
        # 2차원 행렬로 형태 변경
        onehot_reshaped = onehot_labeled.reshape(len(onehot_labeled), 1) 
        
        # 희소행렬로 변환
        onehot_fitted = onehot_encoder.fit_transform(onehot_reshaped)
        return onehot_fitted

# 클래스 인스턴스 생성
encoder = HorsepowerBinEncoder('./auto-mpg.csv')

# 데이터 전처리
encoder.preprocess_data()

# 변환과 인코딩 수행
onehot_fitted = encoder.bin_and_encode()
print(onehot_fitted)
print(type(onehot_fitted))
