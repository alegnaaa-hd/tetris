import pygame, sys
import button
from pygame.locals import QUIT
from settings import setting
from pygame_widgets.slider import Slider
from play import playy
from credits import credits
#setting()
#credits()
def main_menu():
  pygame.init()

  screen = pygame.display.set_mode((880, 1000))
  pygame.display.set_caption("Data Structris")

  #main data structris label
  pygame.draw.rect(screen, "lightblue", pygame.Rect(30, 30, 810, 100))

  font = pygame.font.SysFont("timesnewroman", 36)
  text_b = font.render("Welcome to Data Structris!", True, "black")
  screen.blit(text_b, (230, 60))

  #play button on menu screen
  play_img = pygame.image.load("images/button_play.png").convert_alpha()

  play_button = button.Button(290, 250, play_img, 0.25)

  play_button.draw(screen)

  #credits button on menu screen
  credits_img = pygame.image.load("images/button_credits.png").convert_alpha()

  credits_button = button.Button(290, 350, credits_img, 0.25)

  credits_button.draw(screen)

  #settings button on menu screen

  settings_img = pygame.image.load("images/button_settings.png").convert_alpha()

  settings_button = button.Button(290, 450, settings_img, 0.25)

  settings_button.draw(screen)

  run = True
  while run:
      for event in pygame.event.get():

          if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(f'{x}, {y}')
            if x>297 and x<578:
              if y > 256 and y < 337:
                playy()
              if y > 290 and y < 440:
                credits()
              if y > 450 and y < 550:
                setting()
          elif event.type == QUIT:
              pygame.quit()
              sys.exit()

      pygame.display.update()
    
main_menu()
