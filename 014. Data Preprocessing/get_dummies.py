import pandas as pd
import numpy as np

class HorsepowerBinConversion:
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
        
    def bin_and_convert(self):
        # np.histogram 으로 3개의 bin으로 나누는 경계 값의 리스트 구하기
        count, bin_dividers = np.histogram(self.df['horsepower'], bins=3)
        
        # 3개의 bin에 이름 지정
        bin_names = ['저출력', '보통출력', '고출력']
        
        # pd.cut 으로 각 데이터를 3개의 bin에 할당
        self.df['hp_bin'] = pd.cut(x=self.df['horsepower'],
                                   bins=bin_dividers,
                                   labels=bin_names,
                                   include_lowest=True)
        
        # hp_bin 열의 범주형 데이터를 더미 변수로 변환
        horsepower_dummies = pd.get_dummies(self.df['hp_bin'])
        return horsepower_dummies.head(15)

# 클래스 인스턴스 생성
conversion = HorsepowerBinConversion('./auto-mpg.csv')

# 데이터 전처리
conversion.preprocess_data()

# 변환과 더미 변수 생성
horsepower_dummies = conversion.bin_and_convert()
print(horsepower_dummies)
