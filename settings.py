import pygame, sys
import button
from pygame.locals import QUIT
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from play import playy


def setting():
    from main import main_menu

    pygame.init()

    screen = pygame.display.set_mode((880, 1000))
    pygame.display.set_caption("Menu")

    # font
    #font = pygame.font.SysFont("timesnewroman", 36)
    font_path = 'fonts.ttf'
    font_size = 40
    game_font = pygame.font.Font(font_path, font_size) 
    settings_text = game_font.render("PAUSED - Settings", True, "white")
    screen.blit(settings_text, (225, 60))

    # button images
    resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
    back_img = pygame.image.load("images/button_back.png").convert_alpha()

    # button instances
    resume_button = button.Button(310, 450, resume_img, 0.25)
    back_button = button.Button(310, 550, back_img, 0.25)

    resume_button.draw(screen)
    back_button.draw(screen)

    # slider
    slider = Slider(screen,
                    200,
                    200,
                    500,
                    40,
                    min=0,
                    max=99,
                    step=1,
                    handleColour=(0, 0, 0),
                    colour=(255, 255, 255),
                    handleRadius=16)
    output = TextBox(
        screen,
        430,
        300,
        55,
        50,
        fontSize=30,
    )

    music_text = game_font.render("Music", True, "white")
    screen.blit(music_text, (385, 135))

    output.disable()  # disable textbox, make it a label

    slider.draw()
    output.draw()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(f'{x}, {y}')
                if x > 310 and x < 610:
                    # resume button hitbox
                    if y > 450 and y < 550:
                        playy()

                    # back button hitbox
                    if y > 555 and y < 645:
                        main_menu()

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

        output.setText(slider.getValue())
        pygame_widgets.update(event)
        pygame.display.update()


#def draw_text(text, font, text_col, x, y):
#img = font.render(text, True, text_col)
#screen.blit(img, (x, y))
