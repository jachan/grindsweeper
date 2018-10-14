import random

rows = 16
cols = 32
mines = 99
board = [[0 for x in range(cols)] for y in range(rows)]
revealed = [[None for x in range(cols)] for y in range(rows)]

def display(arr):
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            print(arr[x][y],end="")
        print()

def init():
    global mines
    #places mines
    while mines > 0:
        a = random.randint(0,rows-1)
        b = random.randint(0,cols-1)
        if board[a][b] is not "M":
            board[a][b] = "M"
            mines = mines - 1
    for col in range(len(board)):
        for row in range(len(board[col])):
            if board[col][row] is not "M":
                board[col][row] = count(col,row)
def count(x,y):
#counts mines around x,y
    def counthelp(val1,val2):
        #checks for out of bounds
        if val1<0 or val2<0 or val1>len(board)-1 or val2 > len(board[val1])-1:
            return False
        else:
            return board[val1][val2] is "M"
    total = 0
    if counthelp(x-1,y-1):
        total = total + 1
    if counthelp(x-1,y):
        total = total + 1
    if counthelp(x-1,y+1):
        total = total + 1
    if counthelp(x,y-1):
        total = total + 1
    if counthelp(x,y+1):
        total = total + 1
    if counthelp(x+1,y-1):
        total = total + 1
    if counthelp(x+1,y):
        total = total + 1
    if counthelp(x+1,y+1):
        total = total + 1
    return total    
init()
display(board)

#BUGS
##x and y values how do they relate to row/col
