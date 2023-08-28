import seaborn as sns

class DataManipulator:
    def __init__(self):
        self.df = None
        
    def load_titanic_dataset(self):
        # titanic 데이터셋에서 age, fare 열을 선택하여 데이터프레임 생성
        titanic = sns.load_dataset('titanic')
        self.df = titanic.loc[:, ['age', 'fare']]
        self.df['ten'] = 10
        return self.df
    
    @staticmethod
    def add_two_obj(a, b):    # 두 객체의 합
        return a + b
    
    def add_columns_with_sum(self, dataframe, column1, column2):
        # 데이터프레임의 2개 열을 선택하여 적용하여 새 열 추가
        dataframe['add'] = dataframe.apply(lambda x: self.add_two_obj(x[column1], x[column2]), axis=1)
        return dataframe

# 클래스 인스턴스 생성
manipulator = DataManipulator()

# titanic 데이터셋 로드
manipulator.load_titanic_dataset()

# 두 열의 합을 계산하여 새 열 추가
result_df = manipulator.add_columns_with_sum(manipulator.df, 'age', 'ten')

# 결과 출력
print(result_df.head())
