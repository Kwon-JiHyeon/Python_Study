import pandas as pd
import seaborn as sns

class TitanicDataAnalyzer:
    def __init__(self):
        self.titanic = sns.load_dataset('titanic')
        self.df = self.titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
        self.grouped = self.df.groupby(['class'])

    def analyze_std_all(self):
        std_all = self.grouped.std()
        print(std_all)
        print('\n')
        print(type(std_all))
        print('\n')

    def analyze_std_fare(self):
        std_fare = self.grouped['fare'].std()
        print(std_fare)
        print('\n')
        print(type(std_fare))
        print('\n')

    def analyze_agg_minmax(self):
        def min_max(x):
            return x.max() - x.min()

        agg_minmax = self.grouped.agg(min_max)
        print(agg_minmax.head())
        print('\n')

    def analyze_agg_all(self):
        agg_all = self.grouped.agg(['min', 'max'])
        print(agg_all.head())
        print('\n')

    def analyze_agg_sep(self):
        agg_sep = self.grouped.agg({'fare': ['min', 'max'], 'age': 'mean'})
        print(agg_sep.head())

# 클래스 인스턴스 생성
analyzer = TitanicDataAnalyzer()

# analyze_std_all 메서드를 사용하여 모든 열의 표준편차 출력
analyzer.analyze_std_all()

# analyze_std_fare 메서드를 사용하여 fare 열의 표준편차 출력
analyzer.analyze_std_fare()

# analyze_agg_minmax 메서드를 사용하여 최대값과 최소값의 차이 집계 결과 출력
analyzer.analyze_agg_minmax()

# analyze_agg_all 메서드를 사용하여 모든 열에 여러 함수 적용 결과 출력
analyzer.analyze_agg_all()

# analyze_agg_sep 메서드를 사용하여 각 열에 다른 함수 적용 결과 출력
analyzer.analyze_agg_sep()
