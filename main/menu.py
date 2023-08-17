import pygame
from pygame.locals import *
import sys
from moviepy.editor import *
import subprocess


FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
info = pygame.display.Info()  # Get the screen information
SCREENWIDTH = 1200  
SCREENHEIGHT = 800         

screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pygame.FULLSCREEN)  
pygame.display.set_caption('DUKEY BiRD')

clock = pygame.time.Clock()

background_image = pygame.image.load('gallery/sprites/text.png')
background_image = pygame.transform.scale(background_image, (SCREENWIDTH, SCREENHEIGHT))  

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def play_intro_video(video_path):
    intro_clip = VideoFileClip(video_path)
    intro_clip = intro_clip.resize((SCREENWIDTH, SCREENHEIGHT))  # Resize the video clip to fit the screen
    intro_clip.preview()
    intro_clip.close()
    pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))  # Restore the game window after the video

def main_menu():
    play_intro_video("gallery/sprites/intro.mp4")
    while True:
        screen.fill(BLACK)
        screen.blit(background_image, (0, 0))

        mx, my = pygame.mouse.get_pos()

        button_width = 200
        button_height = 99 
        button_margin = 10

        # Calculate the vertical position for the buttons
        total_button_height = (button_height * 4) + (button_margin * 3)
        button_start_y = (SCREENHEIGHT - total_button_height) // 2

        # Load button images
        easy_button_img = pygame.image.load('gallery/sprites/classic.png').convert_alpha()
        medium_button_img = pygame.image.load('gallery/sprites/Deserted.png').convert_alpha()
        hard_button_img = pygame.image.load('gallery/sprites/Forest.png').convert_alpha()
        ins_button_img = pygame.image.load('gallery/sprites/instructions.png').convert_alpha()
        quit_button_img = pygame.image.load('gallery/sprites/quit.png').convert_alpha()

        # Create button rectangles
        easy_button = easy_button_img.get_rect()
        medium_button = medium_button_img.get_rect()
        hard_button = hard_button_img.get_rect()
        ins_button = ins_button_img.get_rect()
        quit_button = quit_button_img.get_rect()

        # Set the button positions
        button_center_x = SCREENWIDTH // 2
        easy_button.center = (button_center_x, button_start_y)
        medium_button.center = (button_center_x, button_start_y + 1.2 * (button_height + button_margin))
        hard_button.center = (button_center_x, button_start_y + 2.4 * (button_height + button_margin))
        ins_button.center = (button_center_x, button_start_y + 3.6 * (button_height + button_margin))
        quit_button.center = (button_center_x, button_start_y + 4.8 * (button_height + button_margin))

        # Blit the button images onto the screen
        screen.blit(easy_button_img, easy_button)
        screen.blit(medium_button_img, medium_button)
        screen.blit(hard_button_img, hard_button)
        screen.blit(ins_button_img, ins_button)
        screen.blit(quit_button_img, quit_button)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if easy_button.collidepoint((mx, my)):
                        easy_mode()
                    elif medium_button.collidepoint((mx, my)):
                        medium_mode()
                    elif hard_button.collidepoint((mx, my)):
                        hard_mode()
                    elif ins_button.collidepoint((mx, my)):
                        ins_mode()
                    elif quit_button.collidepoint((mx, my)):
                        quit_game()

        pygame.display.update()
        clock.tick(FPS)


def easy_mode():
    # Code for easy mode
    subprocess.call(["python", "mode1.py", "--mode", "easy"])


def medium_mode():
    # Code for medium mode
    subprocess.call(["python", "mode2.py", "--mode", "medium"])

def hard_mode():
    # Code for hard mode
    subprocess.call(["python", "mode3.py", "--mode", "hard"])

def ins_mode():
    # Code for ins mode
    subprocess.call(["python", "ins.py", "--mode", "help"])


def quit_game():
    # Code for quitting the game
    print("Quit")
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main_menu()
