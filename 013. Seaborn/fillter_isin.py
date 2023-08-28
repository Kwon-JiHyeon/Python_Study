import seaborn as sns
import pandas as pd

class TitanicSibspSelector:
    def __init__(self):
        self.titanic = sns.load_dataset('titanic')
        pd.set_option('display.max_columns', 10)
        
    def select_sibsp_counts(self, counts):
        # 함께 탑승한 형제 또는 배우자의 수가 주어진 counts에 해당하는 승객 선택
        mask = self.titanic['sibsp'].isin(counts)
        df_selected = self.titanic[mask]
        return df_selected

# 클래스 인스턴스 생성
sibsp_selector = TitanicSibspSelector()

# 함께 탑승한 형제 또는 배우자의 수가 3, 4, 5인 승객 선택
selected_sibsp_counts = [3, 4, 5]
selected_passengers = sibsp_selector.select_sibsp_counts(selected_sibsp_counts)

# 결과 출력
print("Selected Passengers with Sibsp Counts", selected_sibsp_counts)
print(selected_passengers.head())
