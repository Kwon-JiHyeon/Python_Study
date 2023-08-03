# brute_force_algorithm 함수에 다리가 8개인 곤충을 추가
def brute_force_algorithm2(total_head, total_leg):
    result = []
    for num_chicken in range(total_head + 1):
        for num_pig in range(total_head - num_chicken + 1): 
            num_insects = total_head - num_chicken - num_pig
            if total_leg == num_chicken*2 + num_pig*4 + num_insects*8:
                result.append((num_chicken, num_pig, num_insects))
    return (result)

# barnyard 함수에 곤충의 수 추가
def barnyard2():
    total_head = int(input("닭, 돼지, 곤충의 총 마리수를 입력하세요: "))
    total_leg = int(input("닭, 돼지, 곤충의 총 다리수를 입력하세요: "))

    result = brute_force_algorithm2(total_head, total_leg)

    if result:
        for i in result:
            print(f"닭의 수: {i[0]}, 돼지의 수: {i[1]}, 곤충의 수: {i[2]}")
    else:
        print('There is no solution')
