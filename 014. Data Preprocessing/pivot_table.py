import pandas as pd
import seaborn as sns

class TitanicPivotAnalysis:
    def __init__(self):
        # titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 생성
        self.titanic = sns.load_dataset('titanic')
        self.df = self.titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

    def print_dataframe_head(self):
        """
        데이터프레임의 첫 부분을 출력하는 메서드입니다.
        """
        print("DataFrame Head:\n", self.df.head())
        print('\n')

    def perform_pivot_table(self):
        """
        Pivot Table을 수행하는 메서드입니다.
        """
        # 행, 열, 값에 사용할 열을 지정하여 Pivot Table 수행
        # 평균 집계
        pdf1 = pd.pivot_table(self.df, index='class', columns='sex', values='age', aggfunc='mean')
        print("Pivot Table 1:\n", pdf1.head())
        print('\n')

        # 여러 집계 함수 지정 - 생존율, 생존자 수 집계
        pdf2 = pd.pivot_table(self.df, index='class', columns='sex', values='survived', aggfunc=['mean', 'sum'])
        print("Pivot Table 2:\n", pdf2.head())
        print('\n')

        # 여러 열과 집계 함수 지정 - 평균 나이, 최대 요금 집계
        pdf3 = pd.pivot_table(self.df, index=['class', 'sex'], columns='survived', values=['age', 'fare'], aggfunc=['mean', 'max'])
        print("Pivot Table 3:\n", pdf3.head())
        print('\n')

    def display_pivot_structure(self):
        """
        Pivot Table의 행, 열 구조를 출력하는 메서드입니다.
        """
        # Pivot Table의 행 인덱스와 열 인덱스 출력
        print("Pivot Table Index:\n", pdf3.index)
        print("Pivot Table Columns:\n", pdf3.columns)
        print('\n')

    def perform_xsection_selection(self):
        """
        xs 인덱서를 사용하여 데이터 선택을 수행하는 메서드입니다.
        """
        # xs 인덱서 사용하여 데이터 선택
        # 행 선택 (default: axis=0)
        print("First Class Data:\n", pdf3.xs('First'))
        print("First Class Female Data:\n", pdf3.xs(('First', 'female')))
        print("Male Data:\n", pdf3.xs('male', level='sex'))
        print("Second Class Male Data:\n", pdf3.xs(('Second', 'male'), level=[0, 'sex']))
        print('\n')

        # 열 선택 (axis=1 설정)
        print("Mean Age Data:\n", pdf3.xs('mean', axis=1))
        print("Mean Age Data for Male:\n", pdf3.xs(('mean', 'age'), axis=1))
        print("Survived=1 Data:\n", pdf3.xs(1, level='survived', axis=1))
        print("Max Fare Data for Survived=0:\n", pdf3.xs(('max', 'fare', 0), level=[0, 1, 2], axis=1))
        print('\n')

# 클래스 인스턴스 생성
pivot_analysis = TitanicPivotAnalysis()

# 메서드 호출을 통한 데이터 분석 수행
pivot_analysis.print_dataframe_head()
pivot_analysis.perform_pivot_table()
pivot_analysis.display_pivot_structure()
pivot_analysis.perform_xsection_selection()
