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
def drawGrid():
    blockSize = 35 #Set the size of the grid block
    for x in range(0, 330, blockSize):
        for y in range(0, 680, blockSize):
            rect = pygame.Rect(260+x, 160+y, blockSize, blockSize)
            pygame.draw.rect(screen, "grey", rect, 1)
            
drawGrid()
pygame.mixer.music.play(-1)
arr = Arrmanage()
speed = 30
i=0
while True:
    i+=1
    print(i)
   
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            f = event.type
            if f == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif f == pygame.K_RIGHT:
                arr.moveright()
            elif f == pygame.K_LEFT:
                arr.moveleft()
            elif f == pygame.K_DOWN:
                arr.softdrop()
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
    

    pygame.display.update()

import pygame
import button
from pygame.locals import QUIT

pygame.init()

screen = pygame.display.set_mode((880, 1000))
pygame.display.set_caption ("Menu")

# game variables
game_paused = False
menu_state = "main"

# fonts
font = pygame.font.SysFont("timesnewroman", 50)

#define colours
TEXT_COL = (255, 255, 255)

# button images
resume_img = pygame.image.load("button_resume.png").convert_alpha()

# button instances
resume_button = button.Button(304, 125, resume_img, 1)

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#game loop
run = True
while run:

  screen.fill((52, 78, 91))

  #check if game is paused
  if game_paused == True:
    #check menu state
    if menu_state == "main":
      #draw pause screen buttons
      if resume_button.draw(screen):
        game_paused = False
        
  else:
    draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()

''' CODE FROM VIDEO: 

import pygame
import button

pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#game variables
game_paused = False
menu_state = "main"

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)

#load button images
resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
options_img = pygame.image.load("images/button_options.png").convert_alpha()
quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
video_img = pygame.image.load('images/button_video.png').convert_alpha()
audio_img = pygame.image.load('images/button_audio.png').convert_alpha()
keys_img = pygame.image.load('images/button_keys.png').convert_alpha()
back_img = pygame.image.load('images/button_back.png').convert_alpha()

#create button instances
resume_button = button.Button(304, 125, resume_img, 1)
options_button = button.Button(297, 250, options_img, 1)
quit_button = button.Button(336, 375, quit_img, 1)
video_button = button.Button(226, 75, video_img, 1)
audio_button = button.Button(225, 200, audio_img, 1)
keys_button = button.Button(246, 325, keys_img, 1)
back_button = button.Button(332, 450, back_img, 1)

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#game loop
run = True
while run:

  screen.fill((52, 78, 91))

  #check if game is paused
  if game_paused == True:
    #check menu state
    if menu_state == "main":
      #draw pause screen buttons
      if resume_button.draw(screen):
        game_paused = False
      if options_button.draw(screen):
        menu_state = "options"
      if quit_button.draw(screen):
        run = False
    #check if the options menu is open
    if menu_state == "options":
      #draw the different options buttons
      if video_button.draw(screen):
        print("Video Settings")
      if audio_button.draw(screen):
        print("Audio Settings")
      if keys_button.draw(screen):
        print("Change Key Bindings")
      if back_button.draw(screen):
        menu_state = "main"
  else:
    draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()

'''