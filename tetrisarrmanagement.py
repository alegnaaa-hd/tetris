import random
import pygame
import os


class Arrmanage():
    def __init__(self):
        #sound
        pygame.mixer.init() 
        s='Projects/tetris/sound'
        self.dropsound = pygame.mixer.Sound(os.path.join(s, 'dropsound.ogg'))
        #int values
        self.score = 0
        self.level = 1
        self.totallines = 0
        self.lines = 0
        self.x = 0
        self.y = 0
        self.held_shape = []
        self.next = []
        #create 2d array
        self.arr = []
        for i in range(20):
            l=[]
            for j in range(10):
                l.append(None)
            self.arr.append(l)
        #setup shapes
        xreg = 'RA'
        shape1 = [
            [xreg,xreg,xreg,xreg],
            [None,None,None,None],
            [None,None,None,None],
            [None,None,None,None]

            ]
        xreg = 'RB'
        shape2 = [
            [xreg,None,None,None],
            [xreg,xreg,xreg,None],
            [None,None,None,None],
            [None,None,None,None]
            ]
        xreg = 'RO'
        shape3 = [
            [None,None,None,xreg],
            [None,xreg,xreg,xreg],
            [None,None,None,None],
            [None,None,None,None]
            ]
        xreg = 'RY'
        shape4 = [
            [None,xreg,xreg,None],
            [None,xreg,xreg,None],
            [None,None,None,None],
            [None,None,None,None]
            
            ]
        xreg = 'RG'
        shape5 = [
            [None,xreg,xreg,None],
            [xreg,xreg,None,None],
            [None,None,None,None],
            [None,None,None,None]
            ]
        xreg = 'RP'
        shape6 = [
            [None,xreg,None,None],
            [xreg,xreg,xreg,None],
            [None,None,None,None],
            [None,None,None,None]
            ]
        xreg = 'RR'
        shape7 = [
            [xreg,xreg,None,None],
            [None,xreg,xreg,None],
            [None,None,None,None],
            [None,None,None,None]
            ]
        self.colours = ['RA','RB','RO','RY','RG','RP','RR']
        self.notcolours = ['A','B','O','Y','G','P','R']
        self.shapes = [shape1,shape2,shape3,shape4,shape5,shape6,shape7]
        #make initial queue
        self.getpiece()
        self.addpiece()
    def kill(self):
        pass

    def addpiece(self):
        self.transpose(self.next)
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
        c=0
        for i in range(1,len(self.arr)):
            if None not in self.arr[i]:
                print("LINE IS EMPTY")
                c+=1
                self.arr[i] = [None,None,None,None,None,None,None,None,None,None]
                try:
                    if None not in self.arr[i+1]:
                        c+=1
                        self.arr[i+1] = [None,None,None,None,None,None,None,None,None,None]
                        try:
                            if None not in self.arr[i+2]:
                                c+=1
                                self.arr[i+2] = [None,None,None,None,None,None,None,None,None,None]
                                try:
                                    if None not in self.arr[i+3]:
                                        c+=1
                                        self.arr[i+3] = [None,None,None,None,None,None,None,None,None,None]
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
                self.lines+=c
                if c==1:
                    self.score += 40*self.level
                if c==2:
                    self.score += 100*self.level
                if c==3:
                    self.score += 300*self.level
                if c==4:
                    self.score += 1200*self.level
                self.checkmove()
        
                
    def getpiece(self):
        #chooses random shape and adds it to queue
        p = random.randrange(0,7)
        shape = self.shapes[p]
        self.next = shape
		
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
            for x in self.notcolours:
                if x in self.arr[i+1][3:6]:
                    #kills if already at top
                    self.kill()
            self.arr[i][3:6] = shape[i]
        self.x = 3
        self.y = 0
	
    def arr_hold(self):
        f=[
            [self.arr[self.y][self.x],self.arr[self.y][self.x+1],self.arr[self.y][self.x+2],self.arr[self.y][self.x+3]],
            [self.arr[self.y+1][self.x],self.arr[self.y+1][self.x+1],self.arr[self.y+1][self.x+2],self.arr[self.y+1][self.x+3]],
            [self.arr[self.y+2][self.x],self.arr[self.y+2][self.x+1],self.arr[self.y+2][self.x+2],self.arr[self.y+2][self.x+3]],
            [self.arr[self.y+3][self.x],self.arr[self.y+3][self.x+1],self.arr[self.y+3][self.x+2],self.arr[self.y+3][self.x+3]]
        ]
        if self.held_shape:
            self.transpose(self.held_shape)
        else:
            self.addpiece()
            
    def transpose_low(self,shape,x,y):
		#puts shape in board
        for i in range(x,x+4):
            for x in self.notcolours:
                if x in self.arr[i][y:y+3]:
                    for f in range(4):
                        if self.arr[i][y+f] == x and shape[i-x][f] in self.colours:
                            #stops if impossible
                            return
            for l in range(4):
                for x in self.notcolours:
                    if self.arr[i][y+l] == x:
                        pass
                    else:
                        self.arr[i][y+l] = shape[i-x][l]
	
    def soft_drop(self):
        return self.movedown()
    def drop(self):
		#continually moves down until stops moving
        f=True
        while f != False:
            f= self.soft_drop()
			
    def add_to_board(self):
		#adds shape to static values
        for i in range(20):
            for j in range(10):
                if self.arr[i][j] in self.colours:
                    f = self.arr[i][j]
                    f = f[1]
                    self.arr[i][j] = f
        pygame.mixer.Sound.play(self.dropsound)
        self.addpiece()
        self.checkempty()
		
    def movedown(self):
		#checks that can move down
        for x in range(10):
            if self.arr[19][x] in self.colours:
                self.add_to_board()
                return False
        f = False
        for i in range (19,-1,-1):
            for j in range(10):
                if self.arr[i][j] in self.colours:
                    for x in self.notcolours:
                        if self.arr[i+1][j] == x:
                            self.add_to_board()
                            return False
		#moves down
        if f == False:
            for i in range (19,-1,-1):
                for j in range(10):
                    if self.arr[i][j] in self.colours:
                        self.arr[i+1][j] = self.arr[i][j]
                        self.arr[i][j] = None
                        self.y-=1
    
    def moveleft(self):
		#checks that can move
        f = False
        for x in range(20):
            if self.arr[x][0] in self.colours:
                return
        for i in range (19,-1,-1):
            for j in range(1,10):
                if self.arr[i][j] in self.colours:
                    for x in self.notcolours:
                        if self.arr[i][j-1] == x:
                            f=True
        if f == False:
			#moves
            for i in range (19,-1,-1):
                for j in range(1,10):
                    if self.arr[i][j] in self.colours:
                        self.arr[i][j-1] = self.arr[i][j]
                        self.arr[i][j] = None
                        self.x-=1
    
    def moveright(self):
		#checks that can move
        f = False
        for x in range(20):
            if self.arr[x][9] in self.colours:
                return
        for i in range (19,-1,-1):
            for j in range(8,-1,-1):
                if self.arr[i][j] in self.colours:
                    for x in self.notcolours:
                        if self.arr[i][j+1] == x:
                            f=True
        if f == False:
			#moves
            for i in range (19,-1,-1):
                for j in range(8,-1,-1):
                    if self.arr[i][j] in self.colours:
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
