import seaborn as sns

class MostFrequentImputer:
    def __init__(self, dataset_name):
        self.df = sns.load_dataset(dataset_name)
        
    def print_original_embark_town_column(self):
        print("embark_town 열의 829행의 NaN 데이터 출력:")
        print(self.df['embark_town'][825:830])
        print("\n")
        
    def impute_with_most_frequent(self):
        print("embark_town 열의 NaN값을 가장 많이 출현한 값으로 치환:")
        most_freq = self.df['embark_town'].value_counts(dropna=True).idxmax()
        print("가장 많이 출현한 값:", most_freq)
        self.df['embark_town'].fillna(most_freq, inplace=True)
        print("embark_town 열 829행의 NaN 데이터 출력 (NaN 값이 most_freq 값으로 대체):")
        print(self.df['embark_town'][825:830])
        print("\n")

# 클래스 인스턴스 생성
imputer = MostFrequentImputer('titanic')

# 누락된 값을 최빈값으로 대체하기 전 원본 데이터 출력
imputer.print_original_embark_town_column()

# 누락된 값을 최빈값으로 대체한 후 데이터 출력
imputer.impute_with_most_frequent()
