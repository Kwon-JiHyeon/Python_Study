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
    def missing_value(series):    # 시리즈를 인수로 전달
        return series.isnull()    # 불린 시리즈를 반환
    
    def apply_function_to_columns(self, dataframe, function):
        # 데이터프레임의 각 열을 인수로 전달하여 결과 데이터프레임 반환
        result_df = dataframe.apply(function, axis=0)
        return result_df

# 클래스 인스턴스 생성
manipulator = DataManipulator()

# titanic 데이터셋 로드
manipulator.load_titanic_dataset()

# 사용자 함수 적용
result_df = manipulator.apply_function_to_columns(manipulator.df, manipulator.missing_value)

# 결과 출력
print(result_df.head())
print(type(result_df))
