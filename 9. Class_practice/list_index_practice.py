class MyList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.data[index]
        elif isinstance(index, str):
            return self.data.index(index)

# 테스트
my_list = MyList(['red', 'blue', 'green', 'black'])

print(my_list[0])
print(my_list[2])
print(my_list['red'])
print(my_list['green'])
