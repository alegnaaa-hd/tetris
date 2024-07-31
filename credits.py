import pygame,sys
import button
from pygame.locals import QUIT
import webbrowser


def credits(arr):
  from main import main_menu
  pygame.init()
  screen = pygame.display.set_mode((880, 1000))

  #Bigfont = pygame.font.SysFont("timesnewroman", 36)
  #font = pygame.font.SysFont("timesnewroman", 25)

  font_path = 'Projects/tetris/fonts.ttf'

  Big_game_font = pygame.font.Font(font_path, 40) 
  game_font = pygame.font.Font(font_path, 20)
  small_font = pygame.font.Font(font_path, 17)
  
   # main credits banner 
  credits_text = Big_game_font.render("Credits", True, "white")
  screen.blit(credits_text, (365, 40))

  # data structures final project
  dsaa_text = game_font.render("Data Structures And Algorithms (DSAA/DATA)", True, "white")
  screen.blit(dsaa_text, (160, 100))

  # final project
  dsaa_text = game_font.render("Final Project", True, "white")
  screen.blit(dsaa_text, (350, 140))
  
  # cty car 24.2 @ Dickinson College
  cty_text = game_font.render("CTY CAR 24.2 @ Dickinson College", True, "white")
  screen.blit(cty_text, (220, 180))
  
  # angela wang, kaylin han, nick scott, rachael wang

  names_text = game_font.render("CREATORS: Angela Wang, Kaylin Han, ", True, "white")
  screen.blit(names_text, (200, 220))

  names2_text = game_font.render("Nick Scott, and Rachael Wang", True, "white")
  screen.blit(names2_text, (245, 260))

  # music credits
  music_text = game_font.render("Background Music:", True, "white")
  screen.blit(music_text, (310, 300))

  musicLink_text = small_font.render("https://freesound.org/people/ironreaper1832/sounds/710963/", True, "white")
  screen.blit(musicLink_text, (70, 340))
  
  # link to the code 
  codeLink_text = game_font.render("Code Link: https://github.com/alegnaaa-hd/tetris", True, "white")
  screen.blit(codeLink_text, (145, 380))
  
  # project description (?)
  description_text = game_font.render("Data Structris is our team's recreation of the popular", True, "white")
  screen.blit(description_text, (45, 440))

  description2_text = game_font.render("arcade game: Tetris. With all of the classic game features ", True, "white")
  screen.blit(description2_text, (25, 480))

  description3_text = game_font.render("like rotating, holding, and placing colored shapes, our ", True, "white")
  screen.blit(description3_text, (45, 520))

  description4_text = game_font.render(" game is fun, frustration, and entertainment all in one!", True, "white")
  screen.blit(description4_text, (35, 560))
  
  # back button
  back_img = pygame.image.load("Projects/tetris/buttons/button_back.png").convert_alpha()
  back_button = button.Button(290, 620, back_img, 0.25)
  back_button.draw(screen)

  while True:

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(f'{x}, {y}')
            # link to music
            if x > 66 and x < 800:
              if y > 345 and y < 360:
                webbrowser.open(r"https://freesound.org/people/ironreaper1832/sounds/710963/")
            
            # link to github
            if x > 300 and x < 840:
              if y > 385 and y < 400:
                webbrowser.open(r"https://github.com/alegnaaa-hd/tetris")
    
            # back button
            if x > 290 and x < 580:
              if y > 620 and y < 715:
                main_menu(arr)
                
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
