import pandas as pd

class StockDataProcessor:
    def __init__(self, filename):
        self.filename = filename
    
    def read_data(self):
        # CSV 파일 읽어와서 데이터프레임으로 변환
        df = pd.read_csv(self.filename)
        return df
    
    def add_new_date_column(self, df):
        # 문자열인 날짜 데이터를 판다스 Timestamp로 변환하여 새로운 열로 추가
        df['new_Date'] = pd.to_datetime(df['Date'])
        return df
    
    def extract_year_month_day(self, df):
        # dt 속성을 이용하여 날짜 데이터에서 년, 월, 일 정보를 추출하여 새로운 열로 추가
        df['Year'] = df['new_Date'].dt.year
        df['Month'] = df['new_Date'].dt.month
        df['Day'] = df['new_Date'].dt.day
        return df
    
    def convert_to_period(self, df):
        # Timestamp를 Period로 변환하여 년월일 표기 변경
        df['Date_yr'] = df['new_Date'].dt.to_period(freq='A')
        df['Date_m'] = df['new_Date'].dt.to_period(freq='M')
        return df
    
    def set_index_to_date_m(self, df):
        # 원하는 열을 새로운 행 인덱스로 지정
        df.set_index('Date_m', inplace=True)
        return df

# 클래스 인스턴스 생성
processor = StockDataProcessor('stock-data.csv')

# 데이터 읽기
df = processor.read_data()

# 새로운 열 추가
df = processor.add_new_date_column(df)

# 년월일 정보 추출
df = processor.extract_year_month_day(df)

# 년월일 표기 변경
df = processor.convert_to_period(df)

# 행 인덱스 변경
df = processor.set_index_to_date_m(df)

# 결과 출력
print(df.head())
