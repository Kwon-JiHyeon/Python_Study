import pandas as pd
import numpy as np

class DataPreprocessor:
    def __init__(self, filepath):
        self.df = pd.read_csv(filepath, header=None)
        self.df.columns = ['mpg','cylinders','displacement','horsepower','weight',
                          'acceleration','model year','origin','name']
        
    def check_data_types(self):
        print("각 열의 자료형 확인:")
        print(self.df.dtypes)
        print("\n")
        
    def check_unique_values(self, column_name):
        unique_values = self.df[column_name].unique()
        print(f"{column_name} 열의 고유값 확인:")
        print(unique_values)
        print("\n")
        
    def preprocess_horsepower(self):
        self.df['horsepower'].replace('?', np.nan, inplace=True)
        self.df.dropna(subset=['horsepower'], axis=0, inplace=True)
        self.df['horsepower'] = self.df['horsepower'].astype('float')
        print("horsepower 열 전처리 완료.")
        print("\n")
        
    def preprocess_origin(self):
        self.df['origin'].replace({1:'USA', 2:'EU', 3:'JAPAN'}, inplace=True)
        self.df['origin'] = self.df['origin'].astype('category')
        print("origin 열 전처리 완료.")
        print("\n")
        
    def preprocess_model_year(self):
        print("model year 열 변환 전:")
        print(self.df['model year'].sample(3))
        self.df['model year'] = self.df['model year'].astype('category')
        print("model year 열 변환 후:")
        print(self.df['model year'].sample(3))
        print("\n")

# 클래스 인스턴스 생성
preprocessor = DataPreprocessor('./auto-mpg.csv')

# 각 열의 자료형 확인
preprocessor.check_data_types()

# horsepower 열의 고유값 확인
preprocessor.check_unique_values('horsepower')

# horsepower 열 전처리
preprocessor.preprocess_horsepower()

# origin 열 전처리
preprocessor.preprocess_origin()

# model year 열 전처리
preprocessor.preprocess_model_year()
