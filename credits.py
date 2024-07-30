import pygame
import button
from pygame.locals import QUIT

def credits():
  from main import main_menu
  pygame.init()
  screen = pygame.display.set_mode((880, 1000))

  Bigfont = pygame.font.SysFont("timesnewroman", 36)
  font = pygame.font.SysFont("timesnewroman", 25)
  
   # main credits banner 
  credits_text = Bigfont.render("Credits", True, "white")
  screen.blit(credits_text, (365, 40))

  # data structures final project
  dsaa_text = font.render("Data Structures And Algorithms (DSAA/DATA)", True, "white")
  screen.blit(dsaa_text, (160, 100))

  # final project
  dsaa_text = font.render("Final Project", True, "white")
  screen.blit(dsaa_text, (350, 140))
  
  # cty car 24.2 @ Dickinson College
  cty_text = font.render("CTY CAR 24.2 @ Dickinson College", True, "white")
  screen.blit(cty_text, (220, 180))
  
  # angela wang, kaylin han, nick scott, rachael wang

  names_text = font.render("CREATORS: Angela Wang, Kaylin Han, ", True, "white")
  screen.blit(names_text, (200, 220))

  names2_text = font.render("Nick Scott, and Rachael Wang", True, "white")
  screen.blit(names2_text, (245, 260))

  # insert music credits
  music_text = font.render("insert music credits", True, "white")
  screen.blit(music_text, (335, 300))
  
  # link to the code maybe
  codeLink_text = font.render("insert code link(?)", True, "white")
  screen.blit(codeLink_text, (335, 340))
  
  # project description (?)
  description_text = font.render("insert description here", True, "white")
  screen.blit(description_text, (325, 380))
  
  # back button
  back_img = pygame.image.load("images/button_back.png").convert_alpha()
  back_button = button.Button(290, 420, back_img, 0.25)
  back_button.draw(screen)

  while True:

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(f'{x}, {y}')
            if x > 290 and x < 580:
              if y > 420 and y < 515:
                main_menu()
                
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
