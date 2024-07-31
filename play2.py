# we have to combine this with the other play.py

import pygame, sys
import button
from pygame.locals import QUIT


def playy():
    from settings import setting
    # set variables 
    score = 0
    lines_cleared = 0
    level = 0
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('Data Structris')
    
    screen = pygame.display.set_mode((880, 1000))
    

    font_path = 'fonts.ttf'
    font_size = 32
    game_font = pygame.font.Font(font_path, font_size) 
    
    # ///////////////////// BANNER /////////////////////
    pygame.draw.rect(screen, "lightblue", pygame.Rect(30, 30, 810, 100))
    text_b = game_font.render("Data Structris", True, "black")
    screen.blit(text_b, (265, 60))
    
    # /////////////// RIGHT TOP - NEXT ///////////////
    pygame.draw.rect(screen, "white", pygame.Rect(640, 160, 200, 160))
    text_h = game_font.render("Next", True, "black")
    screen.blit(text_h, (700, 170))
    
    # ///////////// RIGHT MIDDLE - LINES CLEARED /////////////
    pygame.draw.rect(screen, "white", pygame.Rect(640, 350, 200, 150))
    text_lines = game_font.render("Lines", True, "black")
    screen.blit(text_lines, (685, 360))

    text_cleared = game_font.render("Cleared", True, "black")
    screen.blit(text_cleared, (660, 390))
    
    linesCleared_text = game_font.render(f'{lines_cleared}', True, "purple")
    screen.blit(linesCleared_text, (730, 435))
    
    # /////////////// right bottom - level and score ///////////////
    pygame.draw.rect(screen, "white", pygame.Rect(640, 530, 200, 330))
    text_l = game_font.render("Level", True, "black")
    screen.blit(text_l, (690, 540))
    
    #level_text displays the current value of the level variabe
    level_text = game_font.render(f'{level}', True, "purple")
    screen.blit(level_text, (730, 600))
    
    # ////////////////////// score //////////////////////
    text_s = game_font.render("Score", True, "black")
    screen.blit(text_s, (683, 680))
    
    #score_text displays the current value of the score variable
    score_text = game_font.render(f'{score}', True, "purple")
    screen.blit(level_text, (730, 750))
    
    # /////////////////// left top - hold ///////////////////
    pygame.draw.rect(screen, "white", pygame.Rect(30, 160, 200, 160))
    text = game_font.render("Hold", True, "black")
    textRect = text.get_rect()
    screen.blit(text, (85, 170))
    
    # //////////////////// middle ////////////////////
    pygame.draw.rect(screen, "black", pygame.Rect(260, 160, 350, 700))
    
    # //////////////////// settings button ////////////////////
    setting_img = pygame.image.load("images/button_settings.png").convert_alpha()

    setting_button = button.Button(14, 400, setting_img, 0.2)

    setting_button.draw(screen)

    
    # --------- grid ---------
    def drawGrid():
        blockSize = 35  #Set the size of the grid block
        for x in range(0, 330, blockSize):
            for y in range(0, 680, blockSize):
                rect = pygame.Rect(260 + x, 160 + y, blockSize, blockSize)
                pygame.draw.rect(screen, "grey", rect, 1)
    
    drawGrid()
    
    # ///////////////// MAIN GAME /////////////////
    while True:
    
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:

                game_paused = False
                x, y = pygame.mouse.get_pos()
                #print(f'{x}, {y}')
                if x>20 and x<240:
                    if y >405 and y< 468:
                        setting()
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
