import seaborn as sns

class TitanicSelector:
    def __init__(self):
        self.titanic = sns.load_dataset('titanic')
        
    def select_teenage_passengers(self):
        # 나이가 10대(10~19세)인 승객 선택
        mask1 = (self.titanic.age >= 10) & (self.titanic.age < 20)
        df_teenage = self.titanic.loc[mask1, :]
        return df_teenage
    
    def select_female_under_10(self):
        # 나이가 10세 미만(0~9세)이고 여성인 승객 선택
        mask2 = (self.titanic.age < 10) & (self.titanic.sex == 'female')
        df_female_under10 = self.titanic.loc[mask2, :]
        return df_female_under10
    
    def select_under_10_or_over_60(self):
        # 나이가 10세 미만(0~9세) 또는 60세 이상인 승객의 age, sex, alone 열 선택
        mask3 = (self.titanic.age < 10) | (self.titanic.age >= 60)
        df_under10_morethan60 = self.titanic.loc[mask3, ['age', 'sex', 'alone']]
        return df_under10_morethan60

# 클래스 인스턴스 생성
titanic_selector = TitanicSelector()

# 각 기준에 맞는 승객 선택
teenage_passengers = titanic_selector.select_teenage_passengers()
female_under_10 = titanic_selector.select_female_under_10()
under_10_or_over_60 = titanic_selector.select_under_10_or_over_60()

# 결과 출력
print("Teenage Passengers:")
print(teenage_passengers.head())

print("\nFemale Passengers Under 10:")
print(female_under_10.head())

print("\nPassengers Under 10 or Over 60:")
print(under_10_or_over_60.head())
