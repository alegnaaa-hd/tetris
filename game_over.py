import pygame, sys
import button
from pygame.locals import QUIT

def game_over():
  from main import main_menu

  pygame.init()
  screen = pygame.display.set_mode((880, 1000))


  font_path = 'fonts.ttf'
  font_size = 60
  BigFont = pygame.font.Font(font_path, font_size)
  SmallFont = pygame.font.Font(font_path, 30)
  
  game_over_text = BigFont.render("GAME OVER", True, "white")
  screen.blit(game_over_text, (237, 60))

  game_over_text = SmallFont.render("git gud", True, "white")
  screen.blit(game_over_text, (360, 170))

  # back button
  back_img = pygame.image.load("images/button_back.png").convert_alpha()
  back_button = button.Button(290, 250, back_img, 0.25)
  back_button.draw(screen)

  while True:

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(f'{x}, {y}')
            # back button
            if x > 290 and x < 585:
              if y > 250 and y < 345:
                main_menu()

        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
