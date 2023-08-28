import seaborn as sns

class DataFrameManipulator:
    def __init__(self):
        self.df = None
        
    def load_titanic_subset(self):
        # titanic 데이터셋의 부분을 선택하여 데이터프레임 생성
        titanic = sns.load_dataset('titanic')
        self.df = titanic.loc[0:4, 'survived':'age']
        return self.df
    
    def get_column_names(self):
        # 열 이름의 리스트 반환
        columns = list(self.df.columns.values)
        return columns
    
    def sort_columns_alphabetically(self):
        # 열 이름을 알파벳 순으로 정렬한 데이터프레임 반환
        columns_sorted = sorted(self.df.columns)
        df_sorted = self.df[columns_sorted]
        return df_sorted
    
    def reverse_columns_order(self):
        # 열 이름을 기존 순서의 정반대 역순으로 정렬한 데이터프레임 반환
        columns_reversed = list(reversed(self.df.columns))
        df_reversed = self.df[columns_reversed]
        return df_reversed
    
    def custom_order_columns(self, new_order):
        # 사용자가 정의한 순서로 열 이름을 재배치한 데이터프레임 반환
        df_customed = self.df[new_order]
        return df_customed

# 클래스 인스턴스 생성
manipulator = DataFrameManipulator()

# titanic 데이터셋 부분 로드
manipulator.load_titanic_subset()

# 열 이름 리스트 출력
columns = manipulator.get_column_names()
print(columns, '\n')

# 열 이름을 알파벳 순으로 정렬한 결과 출력
df_sorted = manipulator.sort_columns_alphabetically()
print(df_sorted, '\n')

# 열 이름을 역순으로 정렬한 결과 출력
df_reversed = manipulator.reverse_columns_order()
print(df_reversed, '\n')

# 사용자 정의 순서로 열 이름을 재배치한 결과 출력
columns_customed = ['pclass', 'sex', 'age', 'survived']
df_customed = manipulator.custom_order_columns(columns_customed)
print(df_customed)
