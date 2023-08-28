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
    def add_10(n):   # 10을 더하는 함수
        return n + 10
    
    def apply_function_to_dataframe(self, dataframe, function):
        # 데이터프레임의 모든 원소에 함수 적용
        result_df = dataframe.applymap(function)
        return result_df

# 클래스 인스턴스 생성
manipulator = DataManipulator()

# titanic 데이터셋 로드
manipulator.load_titanic_dataset()

# 사용자 함수 적용
result_df = manipulator.apply_function_to_dataframe(manipulator.df, manipulator.add_10)

# 결과 출력
print(result_df.head())
