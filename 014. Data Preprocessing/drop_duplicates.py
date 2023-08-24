# 중복데이터 제거

import pandas as pd

class DataProcessor:
    def __init__(self, data):
        self.data = data
      
    # 중복된 행 기준으로 삭제
    def remove_duplicate_rows(self):
        print("Original DataFrame:")
        print(self.data)
        print("\n")
        
        deduplicated_rows = self.data.drop_duplicates()
        print("DataFrame with duplicate rows removed:")
        print(deduplicated_rows)
        print("\n")

    # 열을 기준으로 중복된 행 삭제
    def remove_duplicate_rows_by_columns(self, column_names):
        deduplicated_rows = self.data.drop_duplicates(subset=column_names)
        print(f"DataFrame with duplicate rows removed based on columns {column_names}:")
        print(deduplicated_rows)

# Create a DataFrame with duplicate data
data_frame = pd.DataFrame({'c1': ['a', 'a', 'b', 'a', 'b'],
                           'c2': [1, 1, 1, 2, 2],
                           'c3': [1, 1, 2, 2, 2]})

# Create an instance of the DataProcessor class and use its methods
data_processor = DataProcessor(data_frame)
data_processor.remove_duplicate_rows()
data_processor.remove_duplicate_rows_by_columns(['c2', 'c3'])
