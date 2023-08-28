import pandas as pd
import seaborn as sns

class TitanicDataAnalyzer:
    def __init__(self):
        self.titanic = sns.load_dataset('titanic')
        self.df = self.titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

    def analyze(self):
        print('승객 수:', len(self.df))
        print(self.df.head())
        print('\n')

    def analyze_grouped(self, column):
        grouped = self.df.groupby([column])
        print(grouped)
        print('\n')
        
        for key, group in grouped:
            print('* key:', key)
            print('* number:', len(group))
            print(group.head())
            print('\n')

    def analyze_average(self):
        grouped = self.df.groupby(['class'])
        average = grouped.mean()
        print(average)
        print('\n')

    def analyze_group_selection(self, column, value):
        grouped = self.df.groupby([column])
        selected_group = grouped.get_group(value)
        print(selected_group.head())
        print('\n')

    def analyze_two_grouped(self, column1, column2):
        grouped_two = self.df.groupby([column1, column2])
        for key, group in grouped_two:
            print('* key:', key)
            print('* number:', len(group))
            print(group.head())
            print('\n')

    def analyze_average_two_grouped(self):
        grouped_two = self.df.groupby(['class', 'sex'])
        average_two = grouped_two.mean()
        print(average_two)
        print('\n')
        print(type(average_two))

    def analyze_group_selection_two(self, value1, value2):
        grouped_two = self.df.groupby(['class', 'sex'])
        selected_group_two = grouped_two.get_group((value1, value2))
        print(selected_group_two.head())

# 클래스 인스턴스 생성
analyzer = TitanicDataAnalyzer()

# analyze 메서드를 사용하여 데이터셋 분석 결과 출력
analyzer.analyze()

# analyze_grouped 메서드를 사용하여 class 열을 기준으로 분할된 그룹 정보 출력
analyzer.analyze_grouped('class')

# analyze_average 메서드를 사용하여 class 열을 기준으로 분할된 그룹의 평균값 출력
analyzer.analyze_average()

# analyze_group_selection 메서드를 사용하여 특정 그룹 선택 결과 출력
analyzer.analyze_group_selection('class', 'Third')

# analyze_two_grouped 메서드를 사용하여 class 열과 sex 열을 기준으로 분할된 그룹 정보 출력
analyzer.analyze_two_grouped('class', 'sex')

# analyze_average_two_grouped 메서드를 사용하여 class 열과 sex 열을 기준으로 분할된 그룹의 평균값 출력
analyzer.analyze_average_two_grouped()

# analyze_group_selection_two 메서드를 사용하여 특정 그룹 선택 결과 출력
analyzer.analyze_group_selection_two('Third', 'female')
