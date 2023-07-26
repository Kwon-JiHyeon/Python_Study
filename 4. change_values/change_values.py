# 이중, 삼중 리스트가 있을때, 재귀함수 이용하여 특정 문자를 다른 문자로 바꾸기 

def change_values(lst, target, replacement):
    for i in range(len(lst)):
        if isinstance(lst[i], list):
            change_values(lst[i], target, replacement)
        elif lst[i] == target:
            lst[i] = replacement

L = [3, 2, [3, [[3, 4, [1, 4]], 4]]]
change_values(L, 4, 5)
print(L)
