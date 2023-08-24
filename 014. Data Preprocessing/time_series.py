import pandas as pd

class StockDataPreprocessor:
    def __init__(self, csv_path):
        # read_csv() 함수로 CSV 파일을 가져와서 df로 변환
        self.df = pd.read_csv(csv_path)
    
    def convert_to_datetime(self):
        # 문자열 데이터를 판다스 Timestamp로 변환하여 새로운 열 추가
        self.df['new_Date'] = pd.to_datetime(self.df['Date'])
        
    def set_new_index(self):
        # 시계열 값으로 변환된 열을 새로운 행 인덱스로 지정. 기존 날짜 열은 삭제
        self.df.set_index('new_Date', inplace=True)
        self.df.drop('Date', axis=1, inplace=True)

# 클래스 인스턴스 생성
preprocessor = StockDataPreprocessor('stock-data.csv')

# 날짜 열을 Timestamp 형식으로 변환
preprocessor.convert_to_datetime()

# 시계열 값으로 변환된 열을 새로운 인덱스로 설정하고 기존 날짜 열 삭제
preprocessor.set_new_index()

# 변환된 결과 출력
print(preprocessor.df.head())
print('\n')
print(preprocessor.df.info())
