class Arrmanage():
    def __init__(self):
        self.arr = []
        for i in range(20):
            x=[]
            for j in range(10):
                x.append(None)
            self.arr.append(x)
        self.temparr = self.arr
        xreg = 'X'

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
        
    def checkmove(self):
        f = True
        for i in range(1,len(self.arr)):
            x = False
            if f == False:
                x = True
            f = True
            for j in self.arr[i]:
                if j != None:
                    f = False
            if f == True and x == True:
                self.arr[i] = self.arr[i-1]
                self.arr[i-1] = [None,None,None,None,None,None,None,None,None,None]
                self.checkmove()
                
    def checkempty(self):
        for i in range(1,len(self.arr)):
            if None not in self.arr[i]:
                self.arr[i] = [None,None,None,None,None,None,None,None,None,None]
                self.checkmove()

f = Arrmanage()
