import pygame, sys
from pygame.locals import QUIT
from tetrisarrmanagement import Arrmanage
import os

pygame.init()
pygame.mixer.init() 
s='Projects/tetris/sound'
backgroundmusic = pygame.mixer.music.load(os.path.join(s,'backgroundmusic2.wav'))

DISPLAYSURF = pygame.display.set_mode((300, 300))
pygame.display.set_caption('Data Structris')

screen = pygame.display.set_mode((880, 1000))

#create the next box

# width, height, width, height

# colors are different to differ between boxes

# banner
pygame.draw.rect(screen, "white", pygame.Rect(30, 30, 810, 100))

font = pygame.font.Font("freesansbold.ttf", 36)
text_b = font.render("Data Structris", True, "black")
screen.blit(text_b, (310, 60))


# right top - next piece
pygame.draw.rect(screen, "white", pygame.Rect(640, 160, 200, 160))
font = pygame.font.Font("freesansbold.ttf", 32)
text_h = font.render("Next", True, "black")
screen.blit(text_h, (713, 160))

# right middle - lines cleared
pygame.draw.rect(screen, "white", pygame.Rect(640, 350, 200, 150))
font = pygame.font.Font("freesansbold.ttf", 28)
text_lc = font.render("Lines Cleared", True, "black")
screen.blit(text_lc, (645, 350))

# right bottom - level and score
pygame.draw.rect(screen, "white", pygame.Rect(640, 530, 200, 330))

font = pygame.font.Font("freesansbold.ttf", 32)
text_l = font.render("Level", True, "black")
screen.blit(text_l, (700, 540))

font = pygame.font.Font("freesansbold.ttf", 32)
text_s = font.render("Score", True, "black")
screen.blit(text_s, (700, 670))

# left top - hold
pygame.draw.rect(screen, "yellow", pygame.Rect(30, 160, 200, 160))
font = pygame.font.Font("freesansbold.ttf", 32)
text = font.render("Hold", True, "black")
textRect = text.get_rect()
screen.blit(text, (90, 160))



# middle
pygame.draw.rect(screen, "black", pygame.Rect(260, 160, 350, 700))

# grid
def drawGrid(arr):
    blockSize = 35 #Set the size of the grid block
    for x in range(0, 10):
        for y in range(0, 20):
            f = arr[y][x]
            if f == None:
                colour = 'grey'
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
            pygame.draw.rect(screen, colour, rect, 1)
            
pygame.mixer.music.play(-1)
arr = Arrmanage()
drawGrid(arr.arr)
speed = 30
i=0
while True:
    i+=1
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
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
                arr.soft_drop()
            elif f == pygame.K_UP:
                arr.rotate_on_board()
            elif f == pygame.K_SPACE:
                arr.drop()
            elif f == pygame.K_c:
                arr.arr_hold()
    if i == 500:
        arr.movedown()
        arr.checkempty()
        if arr.lines >= 10:
            arr.totallines += arr.lines
            arr.lines = 0
            arr.level+=1
            if speed > 5:
                speed-=1
        i=0
    drawGrid(arr.arr)
    pygame.display.update()
