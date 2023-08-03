# 닭과, 돼지의 총 마리수와 총 다리수만 아는 상태에서 닭, 돼지 각각 마리수를 구하는 함수 (완전탐색알고리즘사용)
def brute_force_algorithm(total_head, total_leg):
    for num_chicken in range(total_head + 1):
        num_pig = total_head - num_chicken
        total_legs = num_chicken * 2 + num_pig * 4
        if total_legs == total_leg:
            return num_chicken, num_pig

# 위의 brute_force_algorithm 함수를 사용하여 닭, 돼지의 총마리, 다리개수를 입력받아서 각각의 마리수를 구하는 함수
def barnyard():
    total_head = int(input("닭과 돼지의 총 마리수를 입력하세요: "))
    total_leg = int(input("다리의 총 개수를 입력하세요: "))

    result = brute_force_algorithm(total_head, total_leg)

    if result:
        num_chicken, num_pig = result
        print(f"닭의 수: {num_chicken}, 돼지의 수: {num_pig}")
    else:
        print('There is no solution')
