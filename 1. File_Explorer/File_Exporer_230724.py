from pathlib import Path

def find_index_lines(folder_path):
    index_files = {}
    folder_path = Path(folder_path)  # folder_path 하위 폴더를 다 가져오기위해 import Path 사용
    for file_path in folder_path.glob('**/*.py'):  # glob 함수를 사용하여 폴더 내에서 *.py확장자를 사용하는 파일 검색
        if file_path.is_file():  # file_path가 실제 파일이면 True
            with open(file_path, 'r', encoding='utf-8') as f:
                lines_with_index = [line.strip() for line in f if
                                    'index' in line]  # 파일에서 한줄씩 읽어서 index가 포함된 줄을 찾아 리스트에 저장
                if lines_with_index:  # index가 포함된 줄이 하나라도 있으면 True
                    index_files[str(file_path)] = lines_with_index  # 딕셔너리에 파일경로를 key로, index가 포함된 줄을 value로 저장
    return index_files

def print_result(result):
    for file_path, lines in result.items():
        file_name = file_path.split('/pandas/', 1)[-1]  # /pandas/를 기준으로 1번만 나누어서 /pandas/ 맨 마지막 인덱스출력
        print(f'파일이름: {file_name}')
        print('-' * 80)
        for line in lines:
            print(f"- {line}")
        print()

folder_path = 'C:\\ProgramData\\Anaconda3\\lib\\site-packages\\pandas\\'

result = find_index_lines(folder_path)
print_result(result)
