import pandas as pd
import seaborn as sns

class TitanicDataAnalysis:
    def __init__(self):
        # titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 생성
        self.titanic = sns.load_dataset('titanic')
        self.df = self.titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
        self.grouped = self.df.groupby(['class', 'sex'])

    def calculate_grouped_mean(self):
        """
        그룹별로 평균을 계산하여 반환하는 메서드입니다.
        """
        # 그룹 객체에 연산 메서드 적용하여 평균 계산
        grouped_mean = self.grouped.mean()
        return grouped_mean

    def select_class(self, class_name):
        """
        특정 클래스를 선택하여 해당 클래스 데이터를 반환하는 메서드입니다.
        """
        # class 값이 class_name인 행을 선택하여 반환
        class_data = self.grouped.get_group((class_name, 'male'))  # 성별 정보도 함께 전달
        return class_data

    def select_class_and_sex(self, class_name, sex):
        """
        특정 클래스와 성별을 선택하여 해당 데이터를 반환하는 메서드입니다.
        """
        # class 값이 class_name이고, sex 값이 sex인 행을 선택하여 반환
        selected_data = self.grouped.get_group((class_name, sex))  # 성별 정보도 함께 전달
        return selected_data

    def select_sex(self, sex):
        """
        특정 성별을 선택하여 해당 데이터를 반환하는 메서드입니다.
        """
        # sex 값이 sex인 행을 선택하여 반환
        sex_data = self.grouped.xs(sex, level='sex')
        return sex_data

# 클래스 인스턴스 생성
data_analysis = TitanicDataAnalysis()

# calculate_grouped_mean 메서드를 사용하여 그룹별 평균을 계산하고 출력
grouped_mean = data_analysis.calculate_grouped_mean()
print("Grouped Mean:\n", grouped_mean)
print('\n')

# select_class 메서드를 사용하여 class 값이 'First'인 행을 선택하고 출력
first_class_data = data_analysis.select_class('First')
print("First Class Data:\n", first_class_data)
print('\n')

# select_class_and_sex 메서드를 사용하여 class 값이 'First'이고 sex 값이 'female'인 행을 선택하고 출력
first_female_data = data_analysis.select_class_and_sex('First', 'female')
print("First Class Female Data:\n", first_female_data)
print('\n')

# select_sex 메서드를 사용하여 sex 값이 'male'인 행을 선택하고 출력
male_data = data_analysis.select_sex('male')
print("Male Data:\n", male_data)
print('\n')
