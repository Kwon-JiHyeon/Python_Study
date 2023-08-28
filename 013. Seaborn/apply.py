import seaborn as sns

class DataManipulator:
    def __init__(self):
        self.df = None
        
    def load_titanic_dataset(self):
        # titanic 데이터셋에서 age, fare 열을 선택하여 데이터프레임 생성
        titanic = sns.load_dataset('titanic')
        self.df = titanic.loc[:, ['age', 'fare']]
        self.df['ten'] = 10
        return self.df
    
    @staticmethod
    def add_10(n):   # 10을 더하는 함수
        return n + 10
    
    @staticmethod
    def add_two_obj(a, b):    # 두 객체의 합
        return a + b
    
    def apply_function_to_series(self, series, function, *args, **kwargs):
        # 시리즈 객체에 함수 적용
        result_series = series.apply(function, *args, **kwargs)
        return result_series

# 클래스 인스턴스 생성
manipulator = DataManipulator()

# titanic 데이터셋 로드
manipulator.load_titanic_dataset()

# 사용자 함수 적용
result_sr1 = manipulator.apply_function_to_series(manipulator.df['age'], manipulator.add_10)
result_sr2 = manipulator.apply_function_to_series(manipulator.df['age'], manipulator.add_two_obj, b=10)
result_sr3 = manipulator.apply_function_to_series(manipulator.df['age'], lambda x: manipulator.add_10(x))

# 결과 출력
print(result_sr1.head())
print(result_sr2.head())
print(result_sr3.head())
