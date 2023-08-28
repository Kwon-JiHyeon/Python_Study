import pandas as pd

class DataFrameConcatenator:
    def __init__(self):
        self.df1 = pd.DataFrame({'a': ['a0', 'a1', 'a2', 'a3'],
                                 'b': ['b0', 'b1', 'b2', 'b3'],
                                 'c': ['c0', 'c1', 'c2', 'c3']},
                                 index=[0, 1, 2, 3])

        self.df2 = pd.DataFrame({'a': ['a2', 'a3', 'a4', 'a5'],
                                 'b': ['b2', 'b3', 'b4', 'b5'],
                                 'c': ['c2', 'c3', 'c4', 'c5'],
                                 'd': ['d2', 'd3', 'd4', 'd5']},
                                 index=[2, 3, 4, 5])

        self.sr1 = pd.Series(['e0', 'e1', 'e2', 'e3'], name='e')
        self.sr2 = pd.Series(['f0', 'f1', 'f2'], name='f', index=[3, 4, 5])
        self.sr3 = pd.Series(['g0', 'g1', 'g2', 'g3'], name='g')

    def concatenate_frames_vertical(self):
        result = pd.concat([self.df1, self.df2])
        return result

    def concatenate_frames_vertical_ignore_index(self):
        result = pd.concat([self.df1, self.df2], ignore_index=True)
        return result

    def concatenate_frames_horizontal(self):
        result = pd.concat([self.df1, self.df2], axis=1)
        return result

    def concatenate_frames_horizontal_inner_join(self):
        result = pd.concat([self.df1, self.df2], axis=1, join='inner')
        return result

    def concatenate_series_with_dataframe(self):
        result = pd.concat([self.df1, self.sr1], axis=1)
        return result

    def concatenate_series_with_dataframe_sorted(self):
        result = pd.concat([self.df2, self.sr2], axis=1, sort=True)
        return result

    def concatenate_series(self):
        result = pd.concat([self.sr1, self.sr3], axis=1)
        return result

    def concatenate_series_vertical(self):
        result = pd.concat([self.sr1, self.sr3], axis=0)
        return result

# 클래스 인스턴스 생성
concatenator = DataFrameConcatenator()

# 메서드 사용 예시
result_vertical = concatenator.concatenate_frames_vertical()
print("Vertical Concatenation:")
print(result_vertical, '\n')

result_horizontal = concatenator.concatenate_frames_horizontal()
print("Horizontal Concatenation:")
print(result_horizontal, '\n')
