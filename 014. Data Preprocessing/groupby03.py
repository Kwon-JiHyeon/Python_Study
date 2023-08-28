import pandas as pd
import seaborn as sns

class TitanicDataAnalyzer:
    def __init__(self):
        self.titanic = sns.load_dataset('titanic')
        self.df = self.titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
        self.grouped = self.df.groupby(['class'])

    def analyze_age_mean(self):
        age_mean = self.grouped['age'].mean()
        print(age_mean)
        print('\n')

    def analyze_age_std(self):
        age_std = self.grouped['age'].std()
        print(age_std)
        print('\n')

    def analyze_z_scores(self):
        for key, group in self.grouped['age']:
            age_mean = group.mean()
            age_std = group.std()
            group_zscore = (group - age_mean) / age_std
            print('* origin :', key)
            print(group_zscore.head(3))
            print('\n')

    def calculate_z_score(self, x):
        return (x - x.mean()) / x.std()

    def analyze_transform(self):
        age_zscore = self.grouped['age'].transform(self.calculate_z_score)
        print(age_zscore.loc[[1, 9, 0]])
        print('\n')
        print(len(age_zscore))
        print('\n')
        print(age_zscore.loc[0:9])
        print('\n')
        print(type(age_zscore))

# 클래스 인스턴스 생성
analyzer = TitanicDataAnalyzer()

# analyze_age_mean 메서드를 사용하여 그룹별 age 열의 평균 출력
analyzer.analyze_age_mean()

# analyze_age_std 메서드를 사용하여 그룹별 age 열의 표준편차 출력
analyzer.analyze_age_std()

# analyze_z_scores 메서드를 사용하여 그룹별 z-score 계산 결과 출력
analyzer.analyze_z_scores()

# analyze_transform 메서드를 사용하여 age 열의 데이터를 z-score로 변환한 결과 출력
analyzer.analyze_transform()
