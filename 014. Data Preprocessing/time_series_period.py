import pandas as pd

class DateConverter:
    def __init__(self, date_list):
        self.dates = date_list  # 날짜 형식의 문자열로 구성된 리스트
    
    def convert_to_timestamp(self):
        # 문자열 데이터를 판다스 Timestamp로 변환
        self.ts_dates = pd.to_datetime(self.dates)
    
    def convert_to_period(self):
        # Timestamp를 Period로 변환 (다양한 주기별 변환 가능)
        self.pr_day = self.ts_dates.to_period(freq='D')
        self.pr_month = self.ts_dates.to_period(freq='M')
        self.pr_year = self.ts_dates.to_period(freq='A')

# 클래스 인스턴스 생성
date_converter = DateConverter(['2019-01-01', '2020-03-01', '2021-06-01'])

# 날짜를 Timestamp 형식으로 변환
date_converter.convert_to_timestamp()

# Timestamp를 다양한 주기의 Period로 변환
date_converter.convert_to_period()

# 변환된 결과 출력
print(date_converter.ts_dates)
print('\n')
print(date_converter.pr_day)
print(date_converter.pr_month)
print(date_converter.pr_year)
