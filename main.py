#A minesweeper game

#Import the tkinter gui library
from tkinter import *
#for the random nodes
#-1 or 0
import random

class game():
    '''A MineSweeper game'''

    def __init__(self): # a constructor
        #make the board data type
        self.board={}
        #fill it up with random nodes
        #16 by 16 with 40 mines
        #use a range from 1 to 16^2 if it is less than 41 than it will be a bomb
        for i in range(0,16):
            for j in range(0,16):
                #get the randint
                newVal=random.randint(1,256)
                #bomb
                if newVal<41:
                    #a bomb
                    #new node
                    newNode=node(-1)
                    #add it to the board
                    self.board[(i,j)]=newNode
                #not bomb
                else:
                    newNode=node()
                    self.board[(i,j)]=newNode
                
        #update the node values so they reflect the correct number of
        for i in range(0,16): #row num
            for j in range(0,16) :# col num
                #this is only if it is a bomb
                if self.board[(i,j)].isBomb()!=True:
                    
                    
                    #find the up left corner
                    #go across and down
                    for k in range(i-1,i+2) :
                        for l in range(j-1,j+2) :
                            #is(k,l) on the board
                            if k>-1 and k<16 and l>-1 and l<16:
                                #if kl is a bomb then we inc ij
                                if self.board[(k,l)].isBomb()==True:
                                    #increase the number of bombs bordering
                                    self.board[(i,j)].increase()
                    
        #init the board
        self.window = Tk()
        self.window.title('MineSweeper')
        # Create a canvas within the window to draw on.
        self.canvas = Canvas(self.window, width = 16*30, height = 16*30, bg='white')
        self.canvas.pack()
        # Draw the grid on the canvas.
        for i in range(16):
            for j in range(16):
                self.canvas.create_rectangle(i*30, j*30, (i+1)*30, (j+1)*30)# fill as grey
        # Focus the mouse on the canvas.
        self.canvas.focus_set()

        #bind to the mousepad
        self.canvas.bind("<Button-1>", self.playGame)
        
        
    def playGame(self,event):
        #takes an event
        row = event.y//30
        col = event.x//30
        #checks to see if it's a bomb
        #is a bomb
        if self.board[(row,col)].isBomb():
            #end the game
            self.endGame(row,col)
            return

        #not a bomb
        self.updateBoard(row,col)
        return
    def updateBoard(self,y,x):
        #takes a coordinate in the form of a double and updates the board
        #draw the number on the board
        self.canvas.create_text(x*30+15, y*30+15, text=str(self.board[(y,x)].val).upper())
        return
    def endGame(self,y,x):
        #updates the board to show all cells
        #end the game
        self.canvas.create_text(x*30+15, y*30+15, text='O', fill='red')
        #make a new text block saying game over
        #rebind button so it wont work
        #make a restart option

        return

class node():
    #a node class
    #the node class will be of duples to nodes
    #if the val field <0 then it's a bomb
    #else, it represents the number of bombs it borders
    #the update field will start out as 0 then increase bith node.increase()
    def __init__(self,val=0):
        self.val=val
    def increase(self):
        self.val+=1
    def isBomb(self):
        #if it is a bomb true
        #else false
        if self.val==-1:
            return True
        else:
            return False
        
if __name__ == "__main__":
    game()
