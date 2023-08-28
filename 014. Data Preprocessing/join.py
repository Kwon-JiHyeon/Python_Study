import pandas as pd

class DataJoiner:
    def __init__(self, df1_path, df2_path):
        self.df1 = pd.read_excel(df1_path, index_col='id', engine='openpyxl')
        self.df2 = pd.read_excel(df2_path, index_col='id', engine='openpyxl')

    def join(self):
        return self.df1.join(self.df2)

    def inner_join(self):
        return self.df1.join(self.df2, how='inner')

# 클래스 인스턴스 생성
data_joiner = DataJoiner('./stock price.xlsx', './stock valuation.xlsx')

# join 메서드를 사용하여 데이터프레임 결합
joined_result = data_joiner.join()
print("Joined DataFrame:")
print(joined_result)
print('\n')

# inner_join 메서드를 사용하여 교집합 기준으로 데이터프레임 결합
inner_joined_result = data_joiner.inner_join()
print("Inner Joined DataFrame:")
print(inner_joined_result)
