import pandas as pd

class TimestampGenerator:
    def __init__(self, start_date, periods, freq, timezone):
        self.start_date = start_date  # 날짜 범위의 시작
        self.periods = periods        # 생성할 Timestamp의 개수
        self.freq = freq              # 시간 간격 (월, 분기 등)
        self.timezone = timezone      # 시간대(timezone)
    
    def generate_timestamps(self):
        # Timestamp 배열 생성
        ts = pd.date_range(start=self.start_date,
                          periods=self.periods,
                          freq=self.freq,
                          tz=self.timezone)
        return ts

# 클래스 인스턴스 생성 및 원하는 파라미터 설정
timestamp_generator = TimestampGenerator(start_date='2019-01-01',
                                         periods=6,
                                         freq='MS',   # 월의 시작일
                                         timezone='Asia/Seoul')

# Timestamp 배열 생성
ts_ms = timestamp_generator.generate_timestamps()
print(ts_ms)
print('\n')

# 다른 파라미터로 클래스 인스턴스 생성 및 Timestamp 배열 생성
timestamp_generator = TimestampGenerator(start_date='2019-01-01',
                                         periods=6,
                                         freq='M',    # 월의 마지막 날
                                         timezone='Asia/Seoul')
ts_me = timestamp_generator.generate_timestamps()
print(ts_me)
print('\n')

# 다른 파라미터로 클래스 인스턴스 생성 및 Timestamp 배열 생성
timestamp_generator = TimestampGenerator(start_date='2019-01-01',
                                         periods=6,
                                         freq='3M',   # 3개월
                                         timezone='Asia/Seoul')
ts_3m = timestamp_generator.generate_timestamps()
print(ts_3m)
