import pygame, sys
import button
from pygame.locals import QUIT
import os
from game_over import game_over
from copy import deepcopy


def playy(arr):

    from settings import setting
    # set variables 
    pygame.init()
    pygame.mixer.init()
    DISPLAYSURF = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('Data Structris')
    s='Projects/tetris/sound'
    backgroundmusic = pygame.mixer.music.load(os.path.join(s,'backgroundmusic2.wav'))
    if pygame.mixer.music.get_volume() > 99 and pygame.mixer.music.get_volume < 100:
        pygame.mixer.music.set_volume(0.5)
    screen = pygame.display.set_mode((880, 1000))
    
    def movedown(arr2):
		#checks that can move down
        for x in range(10):
            if arr2[19][x] in arr.colours:
                return arr2,arr2
        f = False
        for i in range (19,-1,-1):
            for j in range(10):
                if arr2[i][j] in arr.colours and arr2[i+1][j] in arr.notcolours:
                    return arr2,arr2
		#moves down
        if f == False:
            for i in range (18,-1,-1):
                for j in range(10):
                    if arr2[i][j] in arr.colours:
                        arr2[i+1][j] = arr2[i][j]
                        arr2[i][j] = None
            return True,arr2
    def drop():
		#continually moves down until stops moving
        m=[]
        for x in arr.arr:
            p = []
            for o in x:
                p.append(o)
            m.append(p)
        f=True
        while f == True:
            f,m= movedown(m)
        return f
    def findpos(arr):
        for m in arr.arr:
            for l in m:
                if l in arr.colours:
                    if 'RY' in m:
                        try:
                            f=[
                                [arr.arr[arr.y][arr.x],arr.arr[arr.y][arr.x+1]],
                                [arr.arr[arr.y+1][arr.x],arr.arr[arr.y+1][arr.x+1]]
                            ]
                        except:
                            return
                    elif 'RA' in m:
                        try:
                            f=[
                                [arr.arr[arr.y][arr.x],arr.arr[arr.y][arr.x+1],arr.arr[arr.y][arr.x+2],arr.arr[arr.y][arr.x+3]],
                                [arr.arr[arr.y+1][arr.x],arr.arr[arr.y+1][arr.x+1],arr.arr[arr.y+1][arr.x+2],arr.arr[arr.y+1][arr.x+3]],
                                [arr.arr[arr.y+2][arr.x],arr.arr[arr.y+2][arr.x+1],arr.arr[arr.y+2][arr.x+2],arr.arr[arr.y+2][arr.x+3]],
                                [arr.arr[arr.y+3][arr.x],arr.arr[arr.y+3][arr.x+1],arr.arr[arr.y+3][arr.x+2],arr.arr[arr.y+3][arr.x+3]]
                            ]
                        except:
                            return
                    else:
                        try:
                            f=[
                                [arr.arr[arr.y][arr.x],arr.arr[arr.y][arr.x+1],arr.arr[arr.y][arr.x+2]],
                                [arr.arr[arr.y+1][arr.x],arr.arr[arr.y+1][arr.x+1],arr.arr[arr.y+1][arr.x+2]],
                                [arr.arr[arr.y+2][arr.x],arr.arr[arr.y+2][arr.x+1],arr.arr[arr.y+2][arr.x+2]]
                            ]
                            #places back on board
                        except:
                            return
        q = drop()
        for x in range(len(q)):
            for y in range (len(q[x])):
                if q[x][y] in arr.colours:
                    rect = pygame.Rect(260+y*35, 160+x*35, 35, 35)
                    pygame.draw.rect(screen, 'grey74', rect)
                    pygame.draw.rect(screen, 'grey', rect, 1)
        

                    

    def draw1(arr):
        font_path = 'Projects/tetris/fonts.ttf'
        font_size = 32
        game_font = pygame.font.Font(font_path, font_size) 
        # ///////////////////// BANNER /////////////////////
        pygame.draw.rect(screen, "lightblue", pygame.Rect(30, 30, 810, 100))
        text_b = game_font.render("Data Structris", True, "black")
        screen.blit(text_b, (265, 60))
        
        # /////////////// RIGHT TOP - NEXT ///////////////
        pygame.draw.rect(screen, "white", pygame.Rect(640, 160, 200, 160))
        text_h = game_font.render("Next", True, "black")
        screen.blit(text_h, (680, 170))
        f=None
        for x in arr.next:
            for o in x:
                if o in arr.colours:
                    if o == 'RA':
                        f = pygame.image.load('Projects/tetris/pieces/aqua.png')
                    elif o == 'RB':
                        f = pygame.image.load('Projects/tetris/pieces/blue.png')
                    elif o == 'RO':
                        f = pygame.image.load('Projects/tetris/pieces/orange.png')
                    elif o == 'RY':
                        f = pygame.image.load('Projects/tetris/pieces/yellow.png')
                    elif o == 'RG':
                        f = pygame.image.load('Projects/tetris/pieces/green.png')
                    elif o == 'RP':
                        f = pygame.image.load('Projects/tetris/pieces/purple.png')
                    elif o == 'RR':
                        f = pygame.image.load('Projects/tetris/pieces/red.png')
        if f:
            screen.blit(f,(650,210))
        
        # ///////////// RIGHT MIDDLE - LINES CLEARED /////////////
        pygame.draw.rect(screen, "white", pygame.Rect(640, 350, 200, 150))
        text_lines = game_font.render("Lines", True, "black")
        screen.blit(text_lines, (685, 360))

        text_cleared = game_font.render("Cleared", True, "black")
        screen.blit(text_cleared, (660, 390))
        
        linesCleared_text = game_font.render(f'{arr.lines}', True, "purple")
        screen.blit(linesCleared_text, (730, 435))
        
        # /////////////// right bottom - level and score ///////////////
        pygame.draw.rect(screen, "white", pygame.Rect(640, 530, 200, 330))
        text_l = game_font.render("Level", True, "black")
        screen.blit(text_l, (690, 540))
        
        #level_text displays the current value of the level variabe
        level_text = game_font.render(f'{arr.level}', True, "purple")
        screen.blit(level_text, (730, 600))
        
        # ////////////////////// score //////////////////////
        text_s = game_font.render("Score", True, "black")
        screen.blit(text_s, (683, 680))
        
        #score_text displays the current value of the score variable
        slen = len(str(arr.score))
        slen = slen-3
        if slen<0:
            slen=0
        slen=slen*10
        score_text = game_font.render(f'{arr.score}', True, "purple")
        screen.blit(score_text, (730-slen, 750))
        
        # /////////////////// left top - hold ///////////////////
        pygame.draw.rect(screen, "white", pygame.Rect(30, 160, 200, 160))
        text = game_font.render("Hold", True, "black")
        textRect = text.get_rect()
        screen.blit(text, (85, 170))
        f=None
        for x in arr.held_shape:
            for o in x:
                if o in arr.colours:
                    if o == 'RA':
                        f = pygame.image.load('Projects/tetris/pieces/aqua.png')
                    elif o == 'RB':
                        f = pygame.image.load('Projects/tetris/pieces/blue.png')
                    elif o == 'RO':
                        f = pygame.image.load('Projects/tetris/pieces/orange.png')
                    elif o == 'RY':
                        f = pygame.image.load('Projects/tetris/pieces/yellow.png')
                    elif o == 'RG':
                        f = pygame.image.load('Projects/tetris/pieces/green.png')
                    elif o == 'RP':
                        f = pygame.image.load('Projects/tetris/pieces/purple.png')
                    elif o == 'RR':
                        f = pygame.image.load('Projects/tetris/pieces/red.png')
        if f:
            screen.blit(f,(50,210))
        
        # //////////////////// middle ////////////////////
        pygame.draw.rect(screen, "black", pygame.Rect(260, 160, 350, 700))
        
        # //////////////////// settings button ////////////////////
        setting_img = pygame.image.load("Projects/tetris/buttons/button_settings.png").convert_alpha()

        setting_button = button.Button(14, 400, setting_img, 0.2)

        setting_button.draw(screen)

    
    # --------- grid ---------
    def drawGrid(arr1):
        blockSize = 35 #Set the size of the grid block
        for x in range(0, 10):
            for y in range(0, 20):
                f = arr1[y][x]
                if f == None:
                    colour = 'grey'
                    rect = pygame.Rect(260+x*blockSize, 160+y*blockSize, blockSize, blockSize)
                    pygame.draw.rect(screen, 'black', rect)
                    pygame.draw.rect(screen, colour, rect, 1)
                else:
                    if len(f) == 2:
                        f = f[1]
                    if f == 'A':
                        colour = 'aqua'
                    elif f == 'B':
                        colour = 'blue'
                    elif f == 'O':
                        colour = 'orange'
                    elif f == 'Y':
                        colour = 'yellow'
                    elif f == 'G':
                        colour = 'green'
                    elif f == 'P':
                        colour = 'purple'
                    elif f == 'R':
                        colour = 'red'
                    rect = pygame.Rect(260+x*blockSize, 160+y*blockSize, blockSize, blockSize)
                    pygame.draw.rect(screen, colour, rect)
                    pygame.draw.rect(screen, 'grey', rect, 1)

    pygame.mixer.music.play(-1)
    drawGrid(arr.arr)
    
    speed = 30
    i=0
    while True:
        i+=1
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:    
                game_paused = False
                x, y = pygame.mouse.get_pos()
                if x>20 and x<240:
                    if y >405 and y< 468:
                        setting(arr)
            elif event.type == pygame.KEYDOWN:
                f = event.key
                if f == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif f == pygame.K_RIGHT:
                    arr.moveright()
                elif f == pygame.K_LEFT:
                    arr.moveleft()
                elif f == pygame.K_DOWN:
                    if arr.soft_drop() == 'DEAD':
                        game_over()
                elif f == pygame.K_UP:
                    arr.rotate_on_board()
                elif f == pygame.K_SPACE:
                    if arr.drop() == 'DEAD':
                        game_over()
                elif f == pygame.K_c:
                    arr.arr_hold()

        if i == 500-10*speed:
            if arr.movedown() == 'DEAD':
                game_over()
            if arr.lines >= 10:
                arr.totallines += arr.lines
                arr.lines = 0
                arr.level+=1
                if speed < 90:
                    speed+=1
            i=0
        draw1(arr)
        drawGrid(arr.arr)
        findpos(arr)
        pygame.display.update()
