'''
2차원 배열 행렬 변환 함수
1 2 3
4 5 6
7 8 9
순서대로 적힌 data.txt 파일이 있다.

위 파일을 [[1, 4, 7], [2, 5, 8], [3, 6, 9]] 출력형태로 바꾸기
'''

def trans_matrix(file_path):
    with open(file_path, 'r') as f:
        matrix = [list(map(int, line.strip().split())) for line in f] # [[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]
        return [list(row) for row in zip(*matrix)]

# 테스트
file_path = 'data.txt'
trans_matrix(file_path)
