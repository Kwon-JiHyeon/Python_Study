import seaborn as sns

class EmbarkTownImputation:
    def __init__(self):
        # titanic 데이터셋 가져오기
        self.df = sns.load_dataset('titanic')
    
    def ffill_imputation(self):
        # embark_town 열의 NaN값을 바로 앞에 있는 값으로 변경 (ffill)
        self.df['embark_town'].fillna(method='ffill', inplace=True)
        
    def bfill_imputation(self):
        # embark_town 열의 NaN값을 바로 뒤에 있는 값으로 변경 (bfill)
        self.df['embark_town'].fillna(method='bfill', inplace=True)
        
    def print_imputed_data(self):
        # 변경된 embark_town 열 출력
        print(self.df['embark_town'][825:830])

# 클래스 인스턴스 생성
imputation = EmbarkTownImputation()

# ffill 방법을 사용하여 NaN값 대체
imputation.ffill_imputation()
print("ffill로 대체된 결과:")
imputation.print_imputed_data()
print()

# bfill 방법을 사용하여 NaN값 대체
imputation.bfill_imputation()
print("bfill로 대체된 결과:")
imputation.print_imputed_data()
