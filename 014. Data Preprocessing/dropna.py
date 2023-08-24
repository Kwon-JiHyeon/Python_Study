import seaborn as sns

class MissingDataHandler:
    def __init__(self, dataset):
        self.df = sns.load_dataset(dataset)
        
    def count_missing_values(self):
        missing_df = self.df.isnull()
        for col in missing_df.columns:
            missing_count = missing_df[col].value_counts()
            
            if True in missing_count.index:
                print(f"{col} 열: {missing_count[True]} 개의 누락값")
            else:
                print(f"{col} 열: 0 개의 누락값")
    
    def remove_columns_with_threshold(self, threshold):
        self.df = self.df.dropna(axis=1, thresh=threshold)
    
    def remove_rows_with_missing_values(self, column_name):
        self.df = self.df.dropna(subset=[column_name], how='any', axis=0)

# 클래스 인스턴스 생성
data_handler = MissingDataHandler('titanic')

# 누락값 개수 출력
print("누락값 개수:")
data_handler.count_missing_values()
print("\n")

# threshold 값 이상인 열 삭제
threshold = 500
data_handler.remove_columns_with_threshold(threshold)
print(f"누락값이 {threshold}개 이상인 열 삭제 후 열 이름: {data_handler.df.columns}")
print("\n")

# age 열에 누락된 데이터가 있는 행 삭제
column_to_check = 'age'
data_handler.remove_rows_with_missing_values(column_to_check)
print(f"{column_to_check} 열에 누락된 데이터가 있는 행 삭제 후 데이터 개수: {len(data_handler.df)}")
