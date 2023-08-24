import seaborn as sns

class MissingDataImputer:
    def __init__(self, dataset_name):
        self.df = sns.load_dataset(dataset_name)
        
    def print_original_age_column(self):
        print("age 열의 첫 10개 데이터 출력 (5 행에 NaN 값):")
        print(self.df['age'].head(10))
        print("\n")
        
    def impute_missing_with_mean(self):
        print("age 열의 NaN값을 다른 나이 데이터의 평균으로 변경:")
        mean_age = self.df['age'].mean(axis=0)
        self.df['age'].fillna(mean_age, inplace=True)
        print("age 열의 첫 10개 데이터 출력 (5 행에 NaN 값이 평균으로 대체):")
        print(self.df['age'].head(10))
        print("\n")

# 클래스 인스턴스 생성
imputer = MissingDataImputer('titanic')

# 누락된 값을 평균값으로 대체하기 전 원본 데이터 출력
imputer.print_original_age_column()

# 누락된 값을 평균값으로 대체한 후 데이터 출력
imputer.impute_missing_with_mean()
