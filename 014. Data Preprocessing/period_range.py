import pandas as pd

class PeriodGenerator:
    def __init__(self, start_date, periods, freq):
        self.start_date = start_date  # 날짜 범위의 시작
        self.periods = periods        # 생성할 Period 개수
        self.freq = freq              # 기간의 길이 (월, 시간 등)
    
    def generate_periods(self):
        # Period 배열 생성
        pr = pd.period_range(start=self.start_date,
                            periods=self.periods,
                            freq=self.freq)
        return pr

# 클래스 인스턴스 생성 및 원하는 파라미터 설정
period_generator = PeriodGenerator(start_date='2019-01-01',
                                   periods=3,
                                   freq='M')  # 1개월 길이

# Period 배열 생성
pr_m = period_generator.generate_periods()
print(pr_m)
print('\n')

# 다른 파라미터로 클래스 인스턴스 생성 및 Period 배열 생성
period_generator = PeriodGenerator(start_date='2019-01-01',
                                   periods=3,
                                   freq='H')  # 1시간 길이
pr_h = period_generator.generate_periods()
print(pr_h)
print('\n')

# 다른 파라미터로 클래스 인스턴스 생성 및 Period 배열 생성
period_generator = PeriodGenerator(start_date='2019-01-01',
                                   periods=3,
                                   freq='2H')  # 2시간 길이
pr_2h = period_generator.generate_periods()
print(pr_2h)
