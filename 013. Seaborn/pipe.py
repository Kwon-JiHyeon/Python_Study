import seaborn as sns

class DataManipulator:
    def __init__(self):
        self.df = None
        
    def load_titanic_dataset(self):
        # titanic 데이터셋에서 age, fare 열을 선택하여 데이터프레임 생성
        titanic = sns.load_dataset('titanic')
        self.df = titanic.loc[:, ['age', 'fare']]
        return self.df
    
    @staticmethod
    def missing_value(x):
        return x.isnull()
    
    @staticmethod
    def missing_count(x):
        return DataManipulator.missing_value(x).sum()
    
    @staticmethod
    def total_number_missing(x):
        return DataManipulator.missing_count(x).sum()
    
    def apply_missing_value(self):
        # 데이터프레임에 missing_value 함수를 적용하여 데이터프레임 반환
        result_df = self.df.pipe(self.missing_value)
        return result_df
    
    def apply_missing_count(self):
        # 데이터프레임에 missing_count 함수를 적용하여 시리즈 반환
        result_series = self.df.pipe(self.missing_count)
        return result_series
    
    def apply_total_number_missing(self):
        # 데이터프레임에 total_number_missing 함수를 적용하여 값을 반환
        result_value = self.df.pipe(self.total_number_missing)
        return result_value

# 클래스 인스턴스 생성
manipulator = DataManipulator()

# titanic 데이터셋 로드
manipulator.load_titanic_dataset()

# 각 함수를 적용한 결과 출력
result_df = manipulator.apply_missing_value()
print(result_df.head())
print(type(result_df))
print('\n')

result_series = manipulator.apply_missing_count()
print(result_series)
print(type(result_series))
print('\n')

result_value = manipulator.apply_total_number_missing()
print(result_value)
print(type(result_value))
