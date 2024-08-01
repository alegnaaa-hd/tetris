import pygame, sys
import button
from pygame.locals import QUIT
from tetrisarrmanagement import Arrmanage

def game_over(score,highscore):
  from main import main_menu
  if (highscore) < score:
      resline = 'NEW HIGH SCORE!'
      file = open('highscore.txt','w')
      file.write(str(score))
      file.close()
  elif (highscore) == score:
      resline = 'HIGH SCORE MATCHED!'
  else:
      resline = 'HIGH SCORE: ' + str(highscore)
  scoreline = 'Your score is: '+str(score)
  pygame.init()
  screen = pygame.display.set_mode((880, 1000))


  font_path = 'fonts.ttf'
  font_size = 60
  BigFont = pygame.font.Font(font_path, font_size)
  SmallFont = pygame.font.Font(font_path, 30)
  
  game_over_text = BigFont.render("GAME OVER", True, "white")
  screen.blit(game_over_text, (237, 60))

  game_over_text = SmallFont.render(scoreline, True, "white")
  screen.blit(game_over_text, (260, 170))

  game_over_text = SmallFont.render(resline, True, "white")
  screen.blit(game_over_text, (260, 210))

  # back button
  back_img = pygame.image.load("buttons/button_back.png").convert_alpha()
  back_button = button.Button(290, 280, back_img, 0.25)
  back_button.draw(screen)

  while True:

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # back button
            if x > 290 and x < 585:
              if y > 280 and y < 375:
                arr = Arrmanage()
                main_menu(arr)

        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
