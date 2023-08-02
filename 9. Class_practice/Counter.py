# 함수 호출시 숫자를 증가시키는 counter 클래스

class Counter:
    def __init__(self, value=0, step=1):
        self.value = value
        self.step = step

    def incr(self):
        self.value += self.step

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'{self.value}'

    def __call__(self):
        self.incr()
        return self.value

# 테스트 
c =  Counter()
c.incr()
c()
