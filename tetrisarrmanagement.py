import random
from queue import Queue

class Arrmanage():
    def __init__(self):
        #setting up initial 2d array for board
        
        self.arr = []
        for i in range(20):
            x=[]
            for j in range(10):
                x.append(None)
            self.arr.append(x)
        self.temparr = self.arr

        #init shapes
        
        xreg = 'R'

        shape1 = [
            [None,None,None,None]
            [None,None,None,None]
            [None,None,None,None]
            [xreg,xreg,xreg,xreg]
            ]
        
        shape2 = [
            [None,None,None,None]
            [None,None,None,None]
            [xreg,None,None,None]
            [xreg,xreg,xreg,None]
            ]
        
        shape3 = [
            [None,None,None,None]
            [None,None,None,None]
            [None,None,xreg,None]
            [xreg,xreg,xreg,None]
            ]
        
        shape4 = [
            [None,None,None,None]
            [None,None,None,None]
            [xreg,xreg,None,None]
            [xreg,xreg,None,None]
            ]
        
        shape5 = [
            [None,None,None,None]
            [None,None,None,None]
            [None,xreg,xreg,None]
            [xreg,xreg,None,None]
            ]
        
        shape6 = [
            [None,None,None,None]
            [None,None,None,None]
            [None,xreg,None,None]
            [xreg,xreg,xreg,None]
            ]
        
        shape7 = [
            [None,None,None,None]
            [None,None,None,None]
            [xreg,xreg,None,None]
            [None,xreg,xreg,None]
            ]
        
        self.shapes = [shape1,shape2,shape3,shape4,shape5,shape6,shape7]

        #setting up next queue
        
        self.queue = Queue()
        for i in range(3):
            self.getpiece()
        
    def checkmove(self):
        f = True
        for i in range(1,len(self.arr)):

            #checking if previous not empty
            x = False
            if f == False:
                x = True

            #checking if line is empty
            f = True
            for j in self.arr[i]:
                if j != None:
                    f = False

            #if line empty and line above not, drop above line
            if f == True and x == True:
                self.arr[i] = self.arr[i-1]
                self.arr[i-1] = [None,None,None,None,None,None,None,None,None,None]
                self.checkmove()
                
    def checkempty(self):
        #clears line
        for i in range(1,len(self.arr)):
            if None not in self.arr[i]:
                self.arr[i] = [None,None,None,None,None,None,None,None,None,None]
                self.checkmove()
    def getpiece(self):
        #takes random piece and adds it to the queue
        p = random.randrange(0,7)
        shape = self.shapes[p]
        self.queue.inqueue(shape)
    
    def rotate(self,shape):
        #  ^
        temp_shape = []
        for i in range(4):
            x=[]
            for j in range(3,-1,-1):
                x.append(shape[j][i])
            temp_shape.append(x)
        return temp_shape

    def add_to_board(self):
        for i in range(20):
            for j in range(10):
                if self.arr[i][j] == 'R':
                    self.arr[i][j] = 'X'

    def transpose(self,shape):
        #places shape on top of board
        for i in range(4):
            if 'X' in self.arr[3:6]:
                self.kill()
            self.arr[i][3:6] = shape[i]

    def movedown(self):
        #checks if all points in shape can move down
        f = False
        for i in range (19,0,-1):
            for j in range(10):
                if self.arr[i][j] == 'R':
                    if self.arr[i+1][j] == 'X':
                        f=True
        #moves everything down
        if f == False:
            for i in range (19,0,-1):
                for j in range(10):
                    if self.arr[i][j] == 'R':
                        self.arr[i+1][j] = self.arr[i][j]
                        self.arr[i][j] = None

    def moveleft(self):
        for x in range(20):
            if self.arr[x][0] == 'R':
                return
        f = False
        for i in range (19,-1,-1):
            for j in range(1,10):
                if self.arr[i][j] == 'R':
                    if self.arr[i][j-1] == 'X':
                        f=True
        if f == False:
            for i in range (19,-1,-1):
                for j in range(1,10):
                    if self.arr[i][j] == 'R':
                        self.arr[i][j-1] = self.arr[i][j]
                        self.arr[i][j] = None
    def moveright(self):
        for x in range(20):
            if self.arr[x][9] == 'R':
                return
        f = False
        for i in range (19,-1,-1):
            for j in range(8,-1,-1):
                if self.arr[i][j] == 'R':
                    if self.arr[i][j+1] == 'X':
                        f=True
        if f == False:
            for i in range (19,-1,-1):
                for j in range(8,-1,-1):
                    if self.arr[i][j] == 'R':
                        self.arr[i][j+1] = self.arr[i][j]
                        self.arr[i][j] = None

f = Arrmanage()
