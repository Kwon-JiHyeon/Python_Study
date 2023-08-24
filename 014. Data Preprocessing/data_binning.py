import pandas as pd
import numpy as np
\
class HorsepowerBinning:
    def __init__(self, file_path):
        # 데이터 불러오기 및 열 이름 설정
        self.df = pd.read_csv(file_path, header=None)
        self.df.columns = ['mpg','cylinders','displacement','horsepower','weight',
                           'acceleration','model year','origin','name']
        
    def preprocess_data(self):
        # 누락된 데이터 삭제 및 horsepower 열 실수형으로 변환
        self.df['horsepower'].replace('?', np.nan, inplace=True)
        self.df.dropna(subset=['horsepower'], axis=0, inplace=True)
        self.df['horsepower'] = self.df['horsepower'].astype('float')
        
    def create_bins(self):
        # np.histogram 함수로 3개의 bin 경계값 계산
        count, bin_dividers = np.histogram(self.df['horsepower'], bins=3)
        
        # 각 bin에 이름 할당
        bin_names = ['저출력', '보통출력', '고출력']
        
        # pd.cut 함수로 데이터를 bin에 할당하여 새 열 생성
        self.df['hp_bin'] = pd.cut(x=self.df['horsepower'],
                                   bins=bin_dividers,
                                   labels=bin_names,
                                   include_lowest=True)
        
    def print_binned_data(self):
        # horsepower 열과 hp_bin 열의 첫 15행 출력
        print(self.df[['horsepower', 'hp_bin']].head(15))

# 클래스 인스턴스 생성
binning = HorsepowerBinning('./auto-mpg.csv')

# 데이터 전처리 및 bin 생성
binning.preprocess_data()
binning.create_bins()

# bin 생성 결과 출력
binning.print_binned_data()
