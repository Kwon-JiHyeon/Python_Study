# 데코레이터 연습 1

def wrapper(func):
    def wrapped_func(*args):
        print('====before====')
        result = func(*args)
        print('====after====')
        return result
    return wrapped_func

@wrapper
def myfunc4(a, b):
    print('I am here')
    return a + b

# 테스트
result = myfunc4(10, 20)
print(result)
