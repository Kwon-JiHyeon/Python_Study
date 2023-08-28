import pandas as pd

class DataMerger:
    def __init__(self, df1_path, df2_path):
        self.df1 = pd.read_excel(df1_path, engine='openpyxl')
        self.df2 = pd.read_excel(df2_path, engine='openpyxl')

    def merge_inner(self):
        return pd.merge(self.df1, self.df2)

    def merge_outer(self):
        return pd.merge(self.df1, self.df2, how='outer', on='id')

    def merge_left(self):
        return pd.merge(self.df1, self.df2, how='left', left_on='stock_name', right_on='name')

    def merge_right(self):
        return pd.merge(self.df1, self.df2, how='right', left_on='stock_name', right_on='name')

    def filter_price_below(self, price_limit):
        return self.df1[self.df1['price'] < price_limit]

    def merge_filtered(self, price_limit):
        filtered_df1 = self.filter_price_below(price_limit)
        return pd.merge(filtered_df1, self.df2)

# 클래스 인스턴스 생성
data_merger = DataMerger('./stock price.xlsx', './stock valuation.xlsx')

# 각각의 메서드 호출하여 결과 출력
merge_inner_result = data_merger.merge_inner()
print("Inner Merge:")
print(merge_inner_result)
print('\n')

merge_outer_result = data_merger.merge_outer()
print("Outer Merge:")
print(merge_outer_result)
print('\n')

merge_left_result = data_merger.merge_left()
print("Left Merge:")
print(merge_left_result)
print('\n')

merge_right_result = data_merger.merge_right()
print("Right Merge:")
print(merge_right_result)
print('\n')

filtered_result = data_merger.merge_filtered(50000)
print("Filtered and Merged:")
print(filtered_result)
