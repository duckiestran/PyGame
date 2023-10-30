import pygame
import os


WIDTH, HEIGHT = 900, 500  # set width and heigh of the game screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # initiate the game window
pygame.display.set_caption("My first pygame game")  # change the title

WHITE = (255, 255, 255)  # set constant value for white color

FPS = 60  # set the frame rate

SUPERMAN_IMAGE = pygame.image.load(
    os.path.join('Assets', 'SuperMan.png'))
SUPERMAN = pygame.transform.scale(SUPERMAN_IMAGE, (150, 150))  # resize the object

BATMAN_IMAGE = pygame.image.load(
    os.path.join('Assets', 'batman.png'))
BATMAN = pygame.transform.scale(BATMAN_IMAGE, (150, 150))  # resize the object


def draw_window(player_superman, player_batman):
    'function to update pygame window'
    WIN.fill(WHITE)  # set the background color for pygame window
    WIN.blit(SUPERMAN, (player_superman.x, player_superman.y))  # display the object with give coordinate
    WIN.blit(BATMAN, (player_batman.x, player_batman.y))  # display the object with give coordinate
    pygame.display.update()  # update display


def main():

    # create pygame rectangle objects to control the characters
    player_superman = pygame.Rect(200, 50, 50, 50)  # instantiate a pygame Rect (X, Y, width, height)
    player_batman = pygame.Rect(50, 50, 50, 50)  # instantiate a pygame Rect (X, Y, width, height)

    clock = pygame.time.Clock()  # initiate the clock variable for controling framerate
    run = True
    while run:
        clock.tick(FPS)  # control the framerate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        player_superman.y += 1
        player_batman.x += 1
        draw_window(player_superman, player_batman)

    pygame.quit()


if __name__ == "__main__":
    main()
