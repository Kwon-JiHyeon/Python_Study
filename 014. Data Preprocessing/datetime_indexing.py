import pandas as pd

class StockDataAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.df = None
    
    def read_data(self):
        # CSV 파일 읽어와서 데이터프레임으로 변환
        self.df = pd.read_csv(self.filename)
        return self.df
    
    def preprocess_data(self):
        # 문자열인 날짜 데이터를 판다스 Timestamp로 변환하여 새로운 열로 추가하고 인덱스로 지정
        self.df['new_Date'] = pd.to_datetime(self.df['Date'])
        self.df.set_index('new_Date', inplace=True)
        return self.df
    
    def select_data_by_year(self, year):
        # 년도별 데이터 선택
        selected_data = self.df[str(year)]
        return selected_data
    
    def select_data_by_year_month(self, year, month):
        # 특정 년월의 데이터 선택
        selected_data = self.df.loc[f'{year}-{month:02}']
        return selected_data
    
    def select_data_by_date_range(self, start_date, end_date):
        # 특정 날짜 범위의 데이터 선택
        selected_data = self.df[start_date:end_date]
        return selected_data
    
    def calculate_time_delta(self):
        # 시간 간격 계산 및 최근 180일 ~ 189일 사이의 데이터 선택
        today = pd.to_datetime('2018-12-25')  # 기준일 생성
        self.df['time_delta'] = today - self.df.index  # 날짜 차이 계산
        self.df.set_index('time_delta', inplace=True)  # 행 인덱스로 지정
        selected_data = self.df['180 days':'189 days']  # 최근 180일 ~ 189일 사이의 데이터 선택
        return selected_data

# 클래스 인스턴스 생성
analyzer = StockDataAnalyzer('stock-data.csv')

# 데이터 읽기
analyzer.read_data()

# 데이터 전처리
analyzer.preprocess_data()

# 년도별 데이터 선택
selected_data_by_year = analyzer.select_data_by_year(2018)

# 특정 년월의 데이터 선택
selected_data_by_year_month = analyzer.select_data_by_year_month(2018, 7)

# 특정 날짜 범위의 데이터 선택
selected_data_by_date_range = analyzer.select_data_by_date_range('2018-06-25', '2018-06-20')

# 시간 간격 계산 및 최근 180일 ~ 189일 사이의 데이터 선택
selected_data_time_delta = analyzer.calculate_time_delta()

# 결과 출력
print(selected_data_by_year)
print(selected_data_by_year_month)
print(selected_data_by_date_range)
print(selected_data_time_delta)
