import pandas as pd

class DateSplitter:
    def __init__(self, file_path):
        self.df = pd.read_excel(file_path, engine='openpyxl')
        
    def split_date_columns(self):
        # 연, 월, 일 데이터 분리하여 새로운 열 추가
        self.df['연월일'] = self.df['연월일'].astype('str')
        dates = self.df['연월일'].str.split('-')
        self.df['연'] = dates.str.get(0)
        self.df['월'] = dates.str.get(1)
        self.df['일'] = dates.str.get(2)
        return self.df

# 클래스 인스턴스 생성
splitter = DateSplitter('./주가데이터.xlsx')

# 날짜 데이터 분리 및 새로운 열 추가
result_df = splitter.split_date_columns()

# 결과 출력
print(result_df.head())
