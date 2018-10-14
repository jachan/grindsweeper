import random
import tkinter as tk

height = 16
length = 32
mines = 99
board = [[0 for y in range(length)] for x in range(height)]
spritePath = "/Users/johnchan/Github/grindsweeper/tilesprites/"

class Application(tk.Frame):
    def __init__(self, master=None):
        self.one = tk.PhotoImage(file = spritePath + "one.gif")
        self.two = tk.PhotoImage(file = spritePath + "two.gif")
        self.three = tk.PhotoImage(file = spritePath + "three.gif")
        self.four = tk.PhotoImage(file = spritePath + "four.gif")
        self.five = tk.PhotoImage(file = spritePath + "five.gif")
        self.six = tk.PhotoImage(file = spritePath + "six.gif")
        self.seven = tk.PhotoImage(file = spritePath + "seven.gif")
        self.eight = tk.PhotoImage(file = spritePath + "eight.gif")
        self.mine = tk.PhotoImage(file = spritePath + "mine.gif")
        self.blank = tk.PhotoImage(file = spritePath + "blank.gif")
        self.zero = tk.PhotoImage(file = spritePath + "zero.gif")
    
    def main(self):
        frame=tk.Frame(root)
        frame.grid(row=0,column=0)
        self.btn=  [[0 for y in range(length)] for x in range(height)]
        for x in range(height):
             for y in range(length):
                self.btn[x][y] = tk.Button(frame, borderwidth=0, padx=0, pady=0, highlightthickness=0, command= lambda x=x, y=y: self.reveal(x,y))
                self.btn[x][y].grid(column=y, row=x)
                self.btn[x][y]["image"] = self.blank
                self.btn[x][y].image = self.blank
        root.mainloop()

    def reveal(self,x,y):
        if board[x][y] is "M":
            self.btn[x][y].config(image = self.mine)
            self.btn[x][y].image = self.mine
        elif board[x][y] == "1":
            self.btn[x][y].config(image = self.one)
            self.btn[x][y].image = self.one
        elif board[x][y] == "2":
            self.btn[x][y].config(image = self.two)
            self.btn[x][y].image = self.two
        elif board[x][y] == "3":
            self.btn[x][y].config(image = self.three)
            self.btn[x][y].image = self.three
        elif board[x][y] == "4":
            self.btn[x][y].config(image = self.four)
            self.btn[x][y].image = self.four
        elif board[x][y] == "5":
            self.btn[x][y].config(image = self.five)
            self.btn[x][y].image = self.five
        elif board[x][y] == "6":
            self.btn[x][y].config(image = self.six)
            self.btn[x][y].image = self.six
        elif board[x][y] == "7":
            self.btn[x][y].config(image = self.seven)
            self.btn[x][y].image = self.seven
        elif board[x][y] == "8":
            self.btn[x][y].config(image = self.eight)
            self.btn[x][y].image = self.eight
        elif board[x][y] == "0":
            self.btn[x][y].config(image = self.zero)
            self.btn[x][y].image = self.zero
        else:
            print("unrecognized character at " + str(x) + " " + str(y))
def display():
    for x in range(height):
        for y in range(length):
            print(board[x][y],end="")
        print()

def init():
    global mines
    #places mines
    while mines > 0:
        x = random.randint(0,height-1)
        y = random.randint(0,length-1)
        if board[x][y] is not "M":
            board[x][y] = "M"
            mines = mines - 1
    for x in range(height):
        for y in range(length):
            if board[x][y] is not "M":
                board[x][y] = str(count(x,y))
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
display()
root = tk.Tk()
app = Application(master=root)
app.main()

#BUGS/TODO
##tk can't do right clicks on buttons -- flags won't work
##logic for win/loss
##initial burst of blank tiles
##tk looks bad on mac -- can't change default style for buttons
##cascading reveal for 0's
