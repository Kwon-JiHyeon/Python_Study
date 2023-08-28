import pandas as pd
import seaborn as sns

class TitanicDataAnalysis:
    def __init__(self):
        self.titanic = sns.load_dataset('titanic')
        self.df = self.titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
        self.grouped = self.df.groupby(['class']) 

    def summarize_grouped_data(self):
        # 각 그룹별 요약 통계정보를 집계하여 출력
        agg_grouped = self.grouped.apply(lambda x: x.describe())   
        return agg_grouped

    def calculate_z_score(self, column_name):
        # z-score를 계산하는 사용자 함수 정의
        def z_score(x):                          
            return (x - x.mean()) / x.std()

        zscore_series = self.grouped[column_name].apply(z_score)
        return zscore_series

    def filter_age_mean(self, threshold):
        # age 열의 데이터 평균이 threshold보다 작은 그룹만을 필터링하여 출력
        age_filter = self.grouped.apply(lambda x: x.age.mean() < threshold)  
        
        filtered_data = {}
        for group_key, condition in age_filter.items():
            if condition:
                age_filter_df = self.grouped.get_group(group_key)
                filtered_data[group_key] = age_filter_df
        
        return filtered_data

# 클래스 인스턴스 생성
data_analysis = TitanicDataAnalysis()

# summarize_grouped_data 메서드를 사용하여 그룹별 요약 통계정보를 출력
grouped_summary = data_analysis.summarize_grouped_data()
print("Grouped Data Summary:\n", grouped_summary)
print('\n')

# calculate_z_score 메서드를 사용하여 age 열의 z-score를 계산하고 출력
zscore_age = data_analysis.calculate_z_score('age')
print("Z-score for Age Column:\n", zscore_age.head())
print('\n')

# filter_age_mean 메서드를 사용하여 age 열의 데이터 평균이 30보다 작은 그룹을 필터링하고 출력
age_filter_data = data_analysis.filter_age_mean(30)
print("Filtered Age Mean < 30:\n")
for group_key, filtered_df in age_filter_data.items():
    print(f"Group: {group_key}")
    print(filtered_df.head())
    print('\n')
