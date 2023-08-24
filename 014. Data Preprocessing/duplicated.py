import pandas as pd

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def find_duplicate_rows(self):
        print("Original DataFrame:")
        print(self.data)
        print("\n")
        
        duplicate_rows = self.data.duplicated()
        print("Duplicate rows in the DataFrame:")
        print(duplicate_rows)
        print("\n")

    def find_duplicate_column(self, column_name):
        column_duplicate = self.data[column_name].duplicated()
        print(f"Duplicate values in column '{column_name}':")
        print(column_duplicate)

# Create a DataFrame
data = {
    'c1': ['a', 'a', 'b', 'a', 'b'],
    'c2': [1, 1, 1, 2, 2],
    'c3': [1, 1, 2, 2, 2]
}

df = pd.DataFrame(data)

# Create an instance of the DataProcessor class and use its methods
data_processor = DataProcessor(df)
data_processor.find_duplicate_rows()
data_processor.find_duplicate_column('c2')
