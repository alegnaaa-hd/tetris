import random
import pygame
import os


class Arrmanage():
    def __init__(self):
        #sound
        pygame.mixer.init() 
        self.dropsound = pygame.mixer.Sound('dropsound.ogg')
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
        self.used = []
        #make initial queue
        self.getpiece()
        self.addpiece()

    def addpiece(self):
        if self.transpose(self.next) == 'DEAD':
            return 'DEAD'
        if 'RO' in self.arr[0]:
            self.x+=1
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
        if shape in self.used:
            self.getpiece()
            return
        self.next = shape
        self.used.append(shape)
        if len(self.used) == 7:
            self.used = []
		
    def rotate(self,shape):
		#rotates a shape
        shape = [[shape[j][i] for j in range(len(shape))] for i in range(len(shape[0])-1,-1,-1)]
        return shape

    def transpose(self,shape):
        #remove lines previous
        for i in range(20):
            for j in range(10):
                if self.arr[i][j] in self.colours:
                    self.arr[i][j] = None
		#puts shape at top
        for i in range(2):
            for x in self.notcolours:
                if x in self.arr[i+1][3:6]:
                    #kills if already at top
                    return 'DEAD'
            self.arr[i][3:6] = shape[i]
    
        self.x = 3
        self.y = 0
        if 'RO' in shape[0]:
            self.x+=1
        f=True
        for i in range(4,20):
            for j in self.arr[i]:
                if j in self.colours:
                    f = False
        if f==False:
            for i in range(20):
                for j in range(10):
                    if self.arr[i][j] in self.colours:
                        self.arr[i][j] = None
            self.used = self.used[0:len(self.used)-1]
            self.getpiece()
            self.addpiece()
	
    def arr_hold(self):
        f=None
        for x in self.arr:
            for l in x:
                if l in self.colours:
                    try:
                        f=[
                                [self.arr[self.y][self.x],self.arr[self.y][self.x+1],self.arr[self.y][self.x+2],self.arr[self.y][self.x+3]],
                                [self.arr[self.y+1][self.x],self.arr[self.y+1][self.x+1],self.arr[self.y+1][self.x+2],self.arr[self.y+1][self.x+3]],
                                [self.arr[self.y+2][self.x],self.arr[self.y+2][self.x+1],self.arr[self.y+2][self.x+2],self.arr[self.y+2][self.x+3]],
                                [self.arr[self.y+3][self.x],self.arr[self.y+3][self.x+1],self.arr[self.y+3][self.x+2],self.arr[self.y+3][self.x+3]]
                            ]
                    except:
                        try:
                            f=[
                                [self.arr[self.y][self.x],self.arr[self.y][self.x+1],self.arr[self.y][self.x+2]],
                                [self.arr[self.y+1][self.x],self.arr[self.y+1][self.x+1],self.arr[self.y+1][self.x+2]],
                                [self.arr[self.y+2][self.x],self.arr[self.y+2][self.x+1],self.arr[self.y+2][self.x+2]]
                            ]
                        except:
                            pass
        m = False
        if f:
            for w in f:
                if m == False:
                    for o in w:
                        if o in self.colours:
                            if o == 'RA':
                                f = [
                                    [o,o,o,o],
                                    [None,None,None,None],
                                    [None,None,None,None],
                                    [None,None,None,None]

                                    ]
                            elif o == 'RB':
                                f = [
                                    [o,None,None,None],
                                    [o,o,o,None],
                                    [None,None,None,None],
                                    [None,None,None,None]
                                    ]
                            elif o == 'RO':
                                f = [
                                    [None,None,o],
                                    [o,o,o],
                                    [None,None,None]
                                    ]
                            elif o == 'RY':
                                f = [
                                    [None,o,o,None],
                                    [None,o,o,None],
                                    [None,None,None,None],
                                    [None,None,None,None]
                                    
                                    ]
                            elif o == 'RG':
                                f = [
                                    [None,o,o,None],
                                    [o,o,None,None],
                                    [None,None,None,None],
                                    [None,None,None,None]
                                    ]
                            elif o == 'RP':
                                f = [
                                    [None,o,None,None],
                                    [o,o,o,None],
                                    [None,None,None,None],
                                    [None,None,None,None]
                                    ]
                            elif o == 'RR':
                                f = [
                                    [o,o,None,None],
                                    [None,o,o,None],
                                    [None,None,None,None],
                                    [None,None,None,None]
                                    ]
            if self.held_shape:
                self.transpose(self.held_shape)
            else:
                self.addpiece()
            self.held_shape = f
            
    def transpose_low(self,shape,x,y):
		#puts shape in board
        try:
            for i in range(len(shape)):
                for p in range(len(shape)):
                    if self.arr[y+p][i+x] in self.notcolours and shape[p][i] in self.colours:
                        return
                for l in range(len(shape)):
                    if self.arr[y+l][i+x] not in self.notcolours:
                        self.arr[y+l][x+i] = shape[l][i]
        except:
            return
	
    def soft_drop(self):
        return self.movedown()
    def drop(self):
		#continually moves down until stops moving
        f=True
        while f != False:
            f= self.soft_drop()
            if f == 'DEAD':
                return 'DEAD'
			
    def add_to_board(self):
		#adds shape to static values
        for i in range(20):
            for j in range(10):
                if self.arr[i][j] in self.colours:
                    f = self.arr[i][j]
                    f = f[1]
                    self.arr[i][j] = f
        pygame.mixer.Sound.play(self.dropsound)
        self.checkempty()
        if self.addpiece() == 'DEAD':
            return 'DEAD'
		
    def movedown(self):
		#checks that can move down
        for x in range(10):
            if self.arr[19][x] in self.colours:
                if self.add_to_board() == 'DEAD':
                    return 'DEAD'
                return False
        f = False
        for i in range (19,-1,-1):
            for j in range(10):
                if self.arr[i][j] in self.colours:
                    for x in self.notcolours:
                        if self.arr[i+1][j] == x:
                            if self.add_to_board() == 'DEAD':
                                return 'DEAD'
                            return False
		#moves down
        if f == False:
            for i in range (19,-1,-1):
                for j in range(10):
                    if self.arr[i][j] in self.colours:
                        self.arr[i+1][j] = self.arr[i][j]
                        self.arr[i][j] = None
            self.y+=1
    
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
        for x in self.arr:
            for l in x:
                if l in self.colours:
                    if 'RY' in x:
                        return
                    elif 'RA' in x:
                        try:
                            f=[
                                [self.arr[self.y][self.x],self.arr[self.y][self.x+1],self.arr[self.y][self.x+2],self.arr[self.y][self.x+3]],
                                [self.arr[self.y+1][self.x],self.arr[self.y+1][self.x+1],self.arr[self.y+1][self.x+2],self.arr[self.y+1][self.x+3]],
                                [self.arr[self.y+2][self.x],self.arr[self.y+2][self.x+1],self.arr[self.y+2][self.x+2],self.arr[self.y+2][self.x+3]],
                                [self.arr[self.y+3][self.x],self.arr[self.y+3][self.x+1],self.arr[self.y+3][self.x+2],self.arr[self.y+3][self.x+3]]
                            ]
                            if f[1][0] == 'RA':
                                f =[
                                    ['RA','RA','RA','RA'],
                                    [None,None,None,None],
                                    [None,None,None,None],
                                    [None,None,None,None]
                                ]
                            else:
                                f=[
                                    ['RA',None,None,None],
                                    ["RA",None,None,None],
                                    ["RA",None,None,None],
                                    ["RA",None,None,None]
                                ]
                            self.transpose_low(f,self.x,self.y)
                            return
                        except:
                            return
                    else:
                        try:
                            f=[
								[self.arr[self.y][self.x],self.arr[self.y][self.x+1],self.arr[self.y][self.x+2]],
                                [self.arr[self.y+1][self.x],self.arr[self.y+1][self.x+1],self.arr[self.y+1][self.x+2]],
                                [self.arr[self.y+2][self.x],self.arr[self.y+2][self.x+1],self.arr[self.y+2][self.x+2]]
                            ]
			    if 'RO' in f[0] or 'RO' in f[1]:
				self.x-=1
				f=[
				[self.arr[self.y][self.x],self.arr[self.y][self.x+1],self.arr[self.y][self.x+2]],
				[self.arr[self.y+1][self.x],self.arr[self.y+1][self.x+1],self.arr[self.y+1][self.x+2]],
                                [self.arr[self.y+2][self.x],self.arr[self.y+2][self.x+1],self.arr[self.y+2][self.x+2]]
                            ]
                            f=self.rotate(f)
                            #places back on board
                            self.transpose_low(f,self.x,self.y)
                            if 'RO' in f[0] or 'RO' in f[1]:
                                self.x+=1
                                pass
                        except:
                            return
