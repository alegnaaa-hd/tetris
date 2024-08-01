import pygame,sys
import button
from pygame.locals import QUIT
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from play import playy

def setting(arr):
    from main import main_menu

    pygame.init()
    
    screen = pygame.display.set_mode((880, 1000))
    pygame.display.set_caption("Menu")

    # font 
    font = pygame.font.SysFont("timesnewroman", 36)
    settings_text = font.render("PAUSED - Settings", True, "white")
    screen.blit(settings_text, (275, 60))

    # button images
    resume_img = pygame.image.load("buttons/button_resume.png").convert_alpha()
    back_img = pygame.image.load("buttons/button_back.png").convert_alpha()
    
    # button instances
    resume_button = button.Button(310, 450, resume_img, 0.25)
    back_button = button.Button(310, 550, back_img, 0.25)
    
    resume_button.draw(screen)
    back_button.draw(screen)
    
    # slider
    slider = Slider(screen, 200, 200, 500, 40, min=0, max=99, step=1, handleColour=(0, 0, 0), colour = (255, 255, 255), handleRadius=16)
    slider.value=int((pygame.mixer.music.get_volume())*100)
    output = TextBox(screen, 430, 300, 55, 50, fontSize=30, )
    
    music_text = font.render("Music", True, "white")
    screen.blit(music_text, (385, 135))
    
    output.disable() # disable textbox, make it a label
    
    slider.draw()
    output.draw()
    
    # game variables
    game_paused = False
    menu_state = "main"
    run = True
    while run:
        event = None
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_paused = False
                x, y = pygame.mouse.get_pos()
                if x > 310 and x < 610:
                    # resume button hitbox
                    if y > 450 and y < 550:
                        playy(arr)
                        
                    # back button hitbox
                    if y > 555 and y < 645:
                        main_menu(arr)
                    
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
    
        output.setText(slider.getValue())
        pygame.mixer.music.set_volume(slider.getValue()/100)
        arr.dropsound.set_volume(slider.getValue()/100)
        pygame_widgets.update(event)
        pygame.display.update()

#def draw_text(text, font, text_col, x, y):
#img = font.render(text, True, text_col)
#screen.blit(img, (x, y))
