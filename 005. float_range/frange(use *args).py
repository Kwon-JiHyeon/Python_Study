# range함수와 비슷하지만 실수 단위로 동작하는 frange함수(*args를 사용)

def frange(args1, *args):
    if len(args) == 0:
        start, stop, step = 0.0, float(args1), 1.0
    if len(args) == 1:
        start, stop, step = float(args1), float(args[0]), 1.0
    if len(args) == 2:
        start, stop, step = float(args1), float(args[0]), float(args[1])
    
    L = []
    v = start
    if step > 0:
        while v < stop:
            L.append(round(v,1)) 
            v += step
    elif step < 0:
        while v > stop:
            L.append(round(v,1))
            v += step
    return L

# 테스트
numbers1 = frange(1, 3, 0.2)
print(numbers1)
numbers2 = frange(3, 1, -0.2)
print(numbers1)
numbers3 = frange(1, 3)
print(numbers1)
numbers4 = frange(4)
print(numbers1)
