# range함수와 비슷하지만 실수 단위로 동작하는 frange함수

def frange(start, stop=None, step=1.0):
    if stop is None:
        start, stop = 0.0, start

    direction = 1 if start < stop else -1
    result = []

    current = start
    while direction * current < direction * stop:
        result.append(current)
        current += step

    return result

def print_frange(numbers):
    formatted_numbers = ['{:.1f}'.format(num) for num in numbers]
    print('[', ', '.join(formatted_numbers), ']')

# 테스트
numbers1 = frange(1, 3, 0.2)
print_frange(numbers1)

numbers2 = frange(3, 1, -0.2)
print_frange(numbers2)

numbers3 = frange(1, 3)
print_frange(numbers3)

numbers4 = frange(4)
print_frange(numbers4)
