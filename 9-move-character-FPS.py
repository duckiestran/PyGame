import pygame
import os  # to define the path to the images

WIDTH, HEIGHT = 900, 500  # set width and heigh of the game screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # initiate the game window
pygame.display.set_caption("My first pygame game")  # change the title
CHARACTER_WIDTH, CHARACTER_HEIGHT = 50, 50

WHITE = (255, 255, 255)  # set constant value for white color

FPS = 60  # set the frame rate

SUPERMAN_IMAGE = pygame.image.load(
    os.path.join('Assets', 'superman.png'))
SUPERMAN = pygame.transform.scale(SUPERMAN_IMAGE, (50, 50))  # resize the object

BATMAN_IMAGE = pygame.image.load(
    os.path.join('Assets', 'batman.png'))
BATMAN = pygame.transform.scale(BATMAN_IMAGE, (50, 50))  # resize the object


def draw_window(player_superman, player_batman):
    'function to update pygame window'
    WIN.fill(WHITE)  # set the background color for pygame window
    WIN.blit(SUPERMAN, (player_superman.x, player_superman.y))  # display the object with give coordinate
    WIN.blit(BATMAN, (player_batman.x, player_batman.y))  # display the object with give coordinate
    pygame.display.update()  # update displa


def main():

    # create pygame rectangle objects to control the characters
    player_superman = pygame.Rect(400, 50, 50, 50)  # instantiate a pygame Rect (X, Y, width, height)
    player_batman = pygame.Rect(400, 50, 50, 50)  # instantiate a pygame Rect (X, Y, width, height)

    clock = pygame.time.Clock()  # initiate the clock variable for controling framerate
    run = True
    while run:
        # clock.tick(FPS)  # control the framerate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        player_superman.y += 1  # change the y coordinate of superman Rect
        player_batman.x += 1  # change the x coordinate of batman Rect
        draw_window(player_superman, player_batman)
    pygame.quit()


if __name__ == "__main__":
    main()
