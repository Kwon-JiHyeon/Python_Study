import pandas as pd
import seaborn as sns

class TitanicDataFilter:
    def __init__(self):
        self.titanic = sns.load_dataset('titanic')
        self.df = self.titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
        self.grouped = self.df.groupby(['class']) 

    def filter_grouped_data(self):
        # 데이터 개수가 200개 이상인 그룹만을 필터링하여 데이터프레임 반환
        grouped_filter = self.grouped.filter(lambda x: len(x) >= 200)  
        return grouped_filter

    def filter_age_mean(self):
        # age 열의 평균이 30보다 작은 그룹만을 필터링하여 데이터프레임 반환
        age_filter = self.grouped.filter(lambda x: x.age.mean() < 30)  
        return age_filter

# 클래스 인스턴스 생성
data_filter = TitanicDataFilter()

# filter_grouped_data 메서드를 사용하여 데이터 개수가 200개 이상인 그룹을 필터링하고 출력
grouped_filter_data = data_filter.filter_grouped_data()
print("Filtered Data (Data Count >= 200):\n", grouped_filter_data.head())
print('\n')

# filter_age_mean 메서드를 사용하여 age 열의 평균이 30보다 작은 그룹을 필터링하고 출력
age_filter_data = data_filter.filter_age_mean()
print("Filtered Data (Age Mean < 30):\n", age_filter_data.tail())
