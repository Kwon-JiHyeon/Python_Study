# 클래스 연습 사칙연산 계산기

class FourCal:
    def __init__(self, first, second):
        self.setdata(first, second)
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        return self.first + self.second
    def mul(self):
        return self.first * self.second
    def sub(self):
        return self.first - self.second
    def div(self):
        return self.first / self.second

# 테스트
fc = FourCal(10, 2)
print(fc.add())
print(fc.sub())
print(fc.mul())
print(fc.div())
