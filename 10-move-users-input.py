from sys import platlibdir
from tracemalloc import stop
import pygame
import os


WIDTH, HEIGHT = 900, 500  # set width and heigh of the game screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # initiate the game window
pygame.display.set_caption("My first pygame game")  # change the title

WHITE = (255, 255, 255)  # set constant value for white color

FPS = 60  # set the frame rate

CHARACTER_WIDTH = 100
CHARACTER_HEIGHT = 100

VELOCITY = 5

IRONMAN_IMAGE = pygame.image.load(r'D:\iron-man.png')
IRONMAN = pygame.transform.scale(IRONMAN_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))  # resize the object

CAPTAIN_IMAGE = pygame.image.load(r'D:\captain-america.png')
CAPTAIN = pygame.transform.scale(CAPTAIN_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))  # resize the object


def draw_window(player_ironman, player_captain):
    'function to update pygame window'
    WIN.fill(WHITE)  # set the background color for pygame window
    WIN.blit(IRONMAN, (player_ironman.x, player_ironman.y))  # display the object with give coordinate
    WIN.blit(CAPTAIN, (player_captain.x, player_captain.y))  # display the object with give coordinate
    pygame.display.update()  # update display


def ironman_movement_handle(keys_pressed, player_ironman):

    if (keys_pressed[pygame.K_a]):
        player_ironman.x -= VELOCITY
    if (keys_pressed[pygame.K_d]):
        player_ironman.x += VELOCITY
    if (keys_pressed[pygame.K_w]):
        player_ironman.y -= VELOCITY
    if (keys_pressed[pygame.K_s]):
        player_ironman.y += VELOCITY

    # Keep player_ironman on the screen
    if player_ironman.x <= 0:
        player_ironman.x = 0
    if player_ironman.x >= 800:
        player_ironman.x = 800
    if player_ironman.y <= 0:
        player_ironman.y = 0
    if player_ironman.y >= 375:
        player_ironman.y = 375


def captain_movement_handle(keys_pressed, player_captain):

    if (keys_pressed[pygame.K_LEFT]):
        player_captain.x -= VELOCITY
    if (keys_pressed[pygame.K_RIGHT]):
        player_captain.x += VELOCITY
    if (keys_pressed[pygame.K_UP]):
        player_captain.y -= VELOCITY
    if (keys_pressed[pygame.K_DOWN]):
        player_captain.y += VELOCITY

    # Keep player_captain on the screen
    if player_captain.x <= 0:
        player_captain.x = 0
    if player_captain.x >= 800:
        player_captain.x = 800
    if player_captain.y <= 0:
        player_captain.y = 0
    if player_captain.y >= 375:
        player_captain.y = 375



def main():

    # create pygame rectangle objects to control the characters
    player_ironman = pygame.Rect(700, 400, 100, 100)  # instantiate a pygame Rect (X, Y, width, height)
    player_captain = pygame.Rect(50, 50, 100, 100)  # instantiate a pygame Rect (X, Y, width, height)
    
    clock = pygame.time.Clock()  # initiate the clock variable for controling framerate
    run = True
    while run:
        clock.tick(FPS)  # control the framerate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()

        ironman_movement_handle(keys_pressed, player_ironman)
        captain_movement_handle(keys_pressed, player_captain)
        draw_window(player_ironman, player_captain)

    pygame.quit()


if __name__ == "__main__":
    main()
