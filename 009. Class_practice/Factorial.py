# 팩도리얼 계산 1 - 단순반복문
class Factorial:
    def __call__(self, n):
        return self.factorial(n)

    def factorial(self, n):
        result = 1
        for i in range(1, n+1):
            result *= i
        return result
      

# 팩토리얼 계산 2 - math 라이브러리 사용
import math

class Factorial():
    def __call__(self, i):
        return math.factorial(i)


# 팩토리얼 계산 3 - cache를 사용하여 메모리 효율 높히기 
class Factorial:
    def __init__(self):
        self.cache = {}
    def __call__(self, n):
        if n not in self.cache:
            if n == 0:
                self.cache[n] = 1 
            else:
                self.cache[n] = n*self.__call__(n-1)
        return self.cache[n] 

# 테스트
fact = Factorial()
for i in range(10):
    print(f"{i}! = {fact(i)}")
