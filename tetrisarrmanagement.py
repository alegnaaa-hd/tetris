import random
from Queue import Queue

class Arrmanage():
    def __init__(self):
        #int values
        self.x = 0
        self.y = 0
        self.queue = Queue()
        #create 2d array
        self.arr = []
        for i in range(20):
            l=[]
            for j in range(10):
                l.append(None)
            self.arr.append(l)
        #setup shapes
        xreg = 'R'
        shape1 = [
            [xreg,xreg,xreg,xreg],
            [None,None,None,None],
            [None,None,None,None],
            [None,None,None,None]

            ]
        shape2 = [
            [xreg,None,None,None],
            [xreg,xreg,xreg,None],
            [None,None,None,None],
            [None,None,None,None]
            ]
        shape3 = [
            [None,None,None,None],
            [None,None,None,None],
            [None,None,xreg,None],
            [xreg,xreg,xreg,None]
            ]
        shape4 = [
            [None,None,None,None],
            [None,None,None,None],
            [xreg,xreg,None,None],
            [xreg,xreg,None,None]
            ]
        shape5 = [
            [None,xreg,xreg,None],
            [xreg,xreg,None,None],
            [None,None,None,None],
            [None,None,None,None]
            ]
        shape6 = [
            [None,xreg,None,None],
            [xreg,xreg,xreg,None],
            [None,None,None,None],
            [None,None,None,None]
            ]
        shape7 = [
            [xreg,xreg,None,None],
            [None,xreg,xreg,None],
            [None,None,None,None],
            [None,None,None,None]
            ]
        self.shapes = [shape1,shape2,shape3,shape4,shape5,shape6,shape7]
        #make initial queue
        for i in range(3):
            self.getpiece()

    def kill(self):
        pass

    def addpiece(self):
        f=self.queue.dequeue()
        self.transpose(f)
        self.getpiece()
		
    def checkmove(self):
        f = True
        for i in range(1,len(self.arr)):
            #check if previous is not empty
            x = False
            if f == False:
                x = True
            f = True
            #checks if empty
            for j in self.arr[i]:
                if j != None:
                    f = False
            if f == True and x == True:
                #if both, move down
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
        #chooses random shape and adds it to queue
        p = random.randrange(0,7)
        shape = self.shapes[p]
        self.queue.inqueue(shape)
		
    def rotate(self,shape):
		#rotates a shape
        temp_shape = []
        for i in range(len(shape)):
            x=[]
            for j in range(len(shape[i])-1,-1,-1):
                x.append(shape[j][i])
            temp_shape.append(x)
        return temp_shape

    def transpose(self,shape):
		#puts shape at top
        for i in range(2):
            if 'X' in self.arr[i][3:6]:
				#kills if already at top
                self.kill()
            self.arr[i][3:6] = shape[i]
        self.x = 3
        self.y = 0
		
    def transpose_low(self,shape,x,y):
		#puts shape in board
        for i in range(x,x+4):
            if 'X' in self.arr[i][y:y+3]:
                for f in range(4):
                    if self.arr[i][y+f] == 'X' and shape[i-x][f] == 'R':
						#stops if impossible
                        return
            self.arr[i][y:y+3] = shape[i-x]
			
    def drop(self):
		#continually moves down until stops moving
        if self.movedown() != False:
            self.drop()
			
    def add_to_board(self):
		#adds shape to static values
        for i in range(20):
            for j in range(10):
                if self.arr[i][j] == 'R':
                    self.arr[i][j] = 'X'
        self.addpiece()
		
    def movedown(self):
		#checks that can move down
        for x in range(10):
            if self.arr[19][x] == 'R':
                self.add_to_board()
                return False
        f = False
        for i in range (19,0,-1):
            for j in range(10):
                if self.arr[i][j] == 'R':
                    if self.arr[i+1][j] == 'X':
                        self.add_to_board()
                        f = True
		#moves down
        if f == False:
            for i in range (19,0,-1):
                for j in range(10):
                    if self.arr[i][j] == 'R':
                        self.arr[i+1][j] = self.arr[i][j]
                        self.arr[i][j] = None
                        self.y-=1
    
    def moveleft(self):
		#checks that can move
        f = False
        for x in range(20):
            if self.arr[x][0] == 'R':
                return
        for i in range (19,-1,-1):
            for j in range(1,10):
                if self.arr[i][j] == 'R':
                    if self.arr[i][j-1] == 'X':
                        f=True
        if f == False:
			#moves
            for i in range (19,-1,-1):
                for j in range(1,10):
                    if self.arr[i][j] == 'R':
                        self.arr[i][j-1] = self.arr[i][j]
                        self.arr[i][j] = None
                        self.x-=1
    
    def moveright(self):
		#checks that can move
        f = False
        for x in range(20):
            if self.arr[x][9] == 'R':
                return
        for i in range (19,-1,-1):
            for j in range(8,-1,-1):
                if self.arr[i][j] == 'R':
                    if self.arr[i][j+1] == 'X':
                        f=True
        if f == False:
			#moves
            for i in range (19,-1,-1):
                for j in range(8,-1,-1):
                    if self.arr[i][j] == 'R':
                        self.arr[i][j+1] = self.arr[i][j]
                        self.arr[i][j] = None
                        self.x+=1
    
    def rotate_on_board(self):
		#grabs shape and rotates it
        f=[
            [self.arr[self.y][self.x],self.arr[self.y][self.x+1],self.arr[self.y][self.x+2],self.arr[self.y][self.x+3]],
            [self.arr[self.y+1][self.x],self.arr[self.y+1][self.x+1],self.arr[self.y+1][self.x+2],self.arr[self.y+1][self.x+3]],
            [self.arr[self.y+2][self.x],self.arr[self.y+2][self.x+1],self.arr[self.y+2][self.x+2],self.arr[self.y+2][self.x+3]],
            [self.arr[self.y+3][self.x],self.arr[self.y+3][self.x+1],self.arr[self.y+3][self.x+2],self.arr[self.y+3][self.x+3]]
        ]
        f=self.rotate(f)
		#places back on board
        self.transpose_low(f,self.x,self.y)
