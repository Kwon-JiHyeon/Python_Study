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
    def min_max(x):    # 최대값 - 최소값
        return x.max() - x.min()
    
    def calculate_min_max_for_columns(self, dataframe):
        # 데이터프레임의 각 열을 인수로 전달하여 결과 시리즈 반환
        result_series = dataframe.apply(self.min_max)   # 기본값 axis=0
        return result_series

# 클래스 인스턴스 생성
manipulator = DataManipulator()

# titanic 데이터셋 로드
manipulator.load_titanic_dataset()

# 사용자 함수 적용
result_series = manipulator.calculate_min_max_for_columns(manipulator.df)

# 결과 출력
print(result_series)
print(type(result_series))
