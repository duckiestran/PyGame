import pygame
import os


WIDTH, HEIGHT = 900, 500  # set width and heigh of the game screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # initiate the game window
pygame.display.set_caption("My first pygame game")  # change the title

WHITE = (255, 255, 255)  # set constant value for white color
WHITE = (255, 255, 255)  # set constant value for white color
BLUE = (0, 0, 255)  # set constant value for blue color

BORDER = pygame.Rect(0, HEIGHT / 2 - 5, WIDTH, 10)  # create border (X, Y, width, height)

FPS = 60  # set the frame rate

CHARACTER_WIDTH = 50
CHARACTER_HEIGHT = 50

VELOCITY = 5

SUPERMAN_IMAGE = pygame.image.load(
    os.path.join('Assets', 'SuperMan.png'))
SUPERMAN = pygame.transform.scale(SUPERMAN_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))  # resize the object

BATMAN_IMAGE = pygame.image.load(
    os.path.join('Assets', 'batman.png'))
BATMAN = pygame.transform.scale(BATMAN_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))  # resize the object


def draw_window(player_superman, player_batman):
    'function to update pygame window'
    WIN.fill(WHITE)  # set the background color for pygame window
    pygame.draw.rect(WIN, BLUE, BORDER)  # draw BORDER with blue color
    WIN.blit(SUPERMAN, (player_superman.x, player_superman.y))  # display the object with give coordinate
    WIN.blit(BATMAN, (player_batman.x, player_batman.y))  # display the object with give coordinate
    pygame.display.update()  # update display


def batman_movement_handle(keys_pressed, player_batman):
    ""
    if (keys_pressed[pygame.K_a]) and player_batman.x - VELOCITY > 0:  # check a key pressed
        player_batman.x -= VELOCITY  # move left
    if (keys_pressed[pygame.K_d]) and player_batman.x + VELOCITY + player_batman.width < WIDTH:  # check d key pressed
        player_batman.x += VELOCITY  # move right
    if (keys_pressed[pygame.K_w]) and player_batman.y - VELOCITY > 0:  # check w key pressed
        player_batman.y -= VELOCITY  # move up
    if (keys_pressed[pygame.K_s]) and player_batman.y + VELOCITY + player_batman.height < HEIGHT:  # check s key pressed
        player_batman.y += VELOCITY  # move down


def superman_movement_handle(keys_pressed, player_superman):
    ""
    if (keys_pressed[pygame.K_LEFT]):  # check a key pressed
        player_superman.x -= VELOCITY  # move left
    if (keys_pressed[pygame.K_RIGHT]):  # check d key pressed
        player_superman.x += VELOCITY  # move right
    if (keys_pressed[pygame.K_UP]):  # check w key pressed
        player_superman.y -= VELOCITY  # move up
    if (keys_pressed[pygame.K_DOWN]):  # check s key pressed
        player_superman.y += VELOCITY  # move down


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

        keys_pressed = pygame.key.get_pressed()
        batman_movement_handle(keys_pressed, player_batman)
        superman_movement_handle(keys_pressed, player_superman)
        draw_window(player_superman, player_batman)

    pygame.quit()


if __name__ == "__main__":
    main()
