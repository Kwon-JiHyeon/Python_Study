import pandas as pd

class MPGConverter:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file, header=None)
        self.df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
                           'acceleration', 'model year', 'origin', 'name']

    def convert_to_kpl(self):
        # mpg(mile per gallon)를 kpl(kilometer per liter)로 변환 (mpg_to_kpl = 0.425)
        mpg_to_kpl = 1.60934 / 3.78541
        
        # mpg 열에 0.425를 곱한 결과를 새로운 열(kpl)에 추가
        self.df['kpl'] = self.df['mpg'] * mpg_to_kpl
        
        # kpl 열을 소수점 아래 둘째 자리에서 반올림 
        self.df['kpl'] = self.df['kpl'].round(2)

    def display_data(self):
        print("Original DataFrame:")
        print(self.df.head(3))
        print("\n")
        
        print("DataFrame after conversion to kpl:")
        print(self.df.head(3))

# Create an instance of the MPGConverter class
converter = MPGConverter('./auto-mpg.csv')

# Use the methods of the class
converter.display_data()
converter.convert_to_kpl()
converter.display_data()
