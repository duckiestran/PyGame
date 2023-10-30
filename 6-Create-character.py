import pygame
import os


WIDTH, HEIGHT = 900, 500  # set width and heigh of the game screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # initiate the game window
pygame.display.set_caption("My first pygame game")  # change the title

WHITE = (255, 255, 255)  # set constant value for white color

FPS = 60  # set the frame rate

IRONMAN_IMAGE = pygame.image.load(r'D:\iron-man.png')
IRONMAN = pygame.transform.scale(IRONMAN_IMAGE, (100, 100))

CAPTAIN_IMAGE = pygame.image.load(r'D:\captain-america.png')
CAPTAIN = pygame.transform.scale(CAPTAIN_IMAGE, (100, 100))



def draw_window():
    'function to update pygame window'
    WIN.fill(WHITE)  # set the background color for pygame window
    WIN.blit(IRONMAN, (250, 150))  # display the object with give coordinate
    WIN.blit(CAPTAIN, (600, 150))
    pygame.display.update()  # update display


def main():

    clock = pygame.time.Clock()  # initiate the clock variable for controling framerate
    run = True
    while run:
        clock.tick(FPS)  # control the framerate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
