from tkinter import *
import time

root  =Tk()

class Node():
    def __init__(self,x,y,data,grid):
        self.x = x
        self.y = y
        self.data = data 
        #parent structure - grid
        self.grid = grid
        # self.button = Button(root,text=str(data),command=self.btn_clicked,padx=20,pady=20,fg="white",bg="black")
        self.button = Button(root,text=data if data > 0 else '',command=self.btn_clicked,padx=20,pady=20)
        # position button on window
        self.button.grid(row = x, column = y)
    
    def btn_clicked(self):
        if self.data != 0:
             neighbours = self.get_neighnours()
             for neighbour in neighbours:
                #  print(neighbour.data)
                 if int(neighbour.data) == 0:
                     # make a move
                     # swap the data
                    self.data, neighbour.data = neighbour.data, self.data
                    self.update_button(self.data)
                    neighbour.update_button(neighbour.data)
                    if self.check_all():
                        print("You Win!")
                        time.sleep(2)
                        exit()
                    return
        
    def update_button(self,data):
        self.button.config(text = data if data > 0 else '')

    def get_neighnours(self):
        neighbours = []
        #left 
        if self.y - 1 >= 0 : 
            neighbours.append(self.grid[self.x][self.y-1])
        #right
        if self.y + 1 < 3:
            neighbours.append(self.grid[self.x][self.y+1])
        #up:
        if self.x-1 >= 0:
            neighbours.append(self.grid[self.x-1][self.y])
        # down
        if self.x + 1 < 3:
            neighbours.append(self.grid[self.x+1][self.y])
        
        return neighbours

    def check_all(self):
        count = 1
        for i in range(3):
            for j in range(3):
                if self.grid[i][j].data == count:
                    count += 1
                elif i == 2 and j == 2:
                    return True
                else:
                    return False
    
buttons = [[],[],[]]
count = 0

# set up all buttons
for i in range(3):
    for j in range(3):
        buttons[i].append(Node(i,j,count,buttons))
        count += 1

        
root.mainloop()
