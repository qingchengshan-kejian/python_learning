weird_board = [['_'] * 3] * 3
print(weird_board)
# 列表内的3个引用指向同一个对象！！！！
weird_board[1][2] = 'O'
print(weird_board)

# 追加同一个对象row到board内
row=['_'] * 3
board = []
for i in range(3):
    board.append(row)

# 每次循环都新建一个列表row追加到board里
board = []
for i in range(3):
    row=['_'] * 3
    board.append(row)

