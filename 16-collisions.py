import pygame
import os


WIDTH, HEIGHT = 900, 500  # set width and heigh of the game screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # initiate the game window
pygame.display.set_caption("My first pygame game")  # change the title

WHITE = (255, 255, 255)  # set constant value for white color
WHITE = (255, 255, 255)  # set constant value for white color
BLUE = (0, 0, 255)  # set constant value for blue color
BLACK = (0, 0, 0)

BORDER = pygame.Rect(0, HEIGHT / 2 - 5, WIDTH, 10)  # create border (X, Y, with, height)

FPS = 60  # set the frame rate

CHARACTER_WIDTH = 50
CHARACTER_HEIGHT = 50

VELOCITY = 5
BULLET_VELOCITY = 15  # bullet speed
MAX_BULLETS = 5  # number of bullet that a character can shoot at a time

# Must use different added values for different events
SUPERMAN_HIT = pygame.USEREVENT + 1  # declare a code-number of user events
BATMAN_HIT = pygame.USEREVENT + 2  # declare a code-number of user events

SUPERMAN_IMAGE = pygame.image.load(
    os.path.join('Assets', 'SuperMan.png'))
SUPERMAN = pygame.transform.scale(SUPERMAN_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))  # resize the object

BATMAN_IMAGE = pygame.image.load(
    os.path.join('Assets', 'batman.png'))
BATMAN = pygame.transform.scale(BATMAN_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))  # resize the object


def draw_window(player_superman, player_batman, batman_bullets, superman_bullets):
    'function to update pygame window'
    WIN.fill(WHITE)  # set the background color for pygame window
    pygame.draw.rect(WIN, BLUE, BORDER)  # draw BORDER with blue color
    WIN.blit(SUPERMAN, (player_superman.x, player_superman.y))  # display the object with give coordinate
    WIN.blit(BATMAN, (player_batman.x, player_batman.y))  # display the object with give coordinate

    for bullet in batman_bullets:
        pygame.draw.rect(WIN, BLACK, bullet)

    for bullet in superman_bullets:
        pygame.draw.rect(WIN, BLUE, bullet)
    pygame.display.update()  # update display


def batman_movement_handle(keys_pressed, player_batman):
    ""
    if (keys_pressed[pygame.K_a]) and player_batman.x - VELOCITY > 0:  # check a key pressed
        player_batman.x -= VELOCITY  # move left
    if (keys_pressed[pygame.K_d]) and player_batman.x + VELOCITY + player_batman.width < WIDTH:  # check d key pressed
        player_batman.x += VELOCITY  # move right
    if (keys_pressed[pygame.K_w]) and player_batman.y - VELOCITY > 0:  # check w key pressed
        player_batman.y -= VELOCITY  # move up
    if (keys_pressed[pygame.K_s]) and player_batman.y + VELOCITY + player_batman.height + BORDER.y < HEIGHT:  # check s key pressed
        player_batman.y += VELOCITY  # move down


def superman_movement_handle(keys_pressed, player_superman):
    ""
    if (keys_pressed[pygame.K_LEFT]) and player_superman.x - VELOCITY > 0:  # check a key pressed
        player_superman.x -= VELOCITY  # move left
    if (keys_pressed[pygame.K_RIGHT]) and player_superman.x + VELOCITY + player_superman.width < WIDTH:  # check d key pressed
        player_superman.x += VELOCITY  # move right
    if (keys_pressed[pygame.K_UP]) and player_superman.y - VELOCITY - BORDER.y > 0:  # check w key pressed
        player_superman.y -= VELOCITY  # move up
    if (keys_pressed[pygame.K_DOWN]) and player_superman.y + VELOCITY + player_superman.height < HEIGHT:  # check s key pressed
        player_superman.y += VELOCITY  # move down


def handle_bullets(batman_bullets, player_batman, superman_bullets, player_superman):
    ""
    for bullet in batman_bullets:
        bullet.y += BULLET_VELOCITY  # move the bullet
        if bullet.y > HEIGHT:
            batman_bullets.remove(bullet)  # remove bullet when it is out of screen
        elif player_superman.colliderect(bullet):  # colliderect - check two pygame.Rect objects collide or not
            batman_bullets.remove(bullet)  # remove bullet when it is out of screen
            pygame.event.post(pygame.event.Event(SUPERMAN_HIT))  # post event when supperman get hit

    for bullet in superman_bullets:
        bullet.y -= BULLET_VELOCITY  # move the bullet
        if bullet.y < 0:
            superman_bullets.remove(bullet)  # remove bullet when it is out of screen
        elif player_batman.colliderect(bullet):  # colliderect - check two pygame.Rect objects collide or not
            superman_bullets.remove(bullet)  # remove bullet when it is out of screen
            pygame.event.post(pygame.event.Event(BATMAN_HIT))  # post event when supperman get hit


def main():

    # create pygame rectangle objects to control the characters
    player_superman = pygame.Rect(200, 400, 50, 50)  # instantiate a pygame Rect (X, Y, width, height)
    player_batman = pygame.Rect(50, 50, 50, 50)  # instantiate a pygame Rect (X, Y, width, height)
    batman_bullets = []  # list of batman's bullets
    superman_bullets = []  # list of superman's bullet

    clock = pygame.time.Clock()  # initiate the clock variable for controling framerate
    run = True
    while run:
        clock.tick(FPS)  # control the framerate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:  # check user press a key event
                if event.key == pygame.K_LCTRL and len(batman_bullets) < MAX_BULLETS:  # check left ctrl click
                    # set the position of bullet when batman fire
                    bullet = pygame.Rect(player_batman.x + player_batman.width / 2, player_batman.y + player_batman.height, 10, 5)
                    batman_bullets.append(bullet)  # add bullet to the list for display and control the number of bullets
                if event.key == pygame.K_RCTRL and len(superman_bullets) < MAX_BULLETS:  # check left ctrl click
                    # set the position of bullet when batman fire
                    bullet = pygame.Rect(player_superman.x, player_superman.y, 10, 5)
                    superman_bullets.append(bullet)  # add bullet to the list for display and control the number of bullets

        keys_pressed = pygame.key.get_pressed()
        batman_movement_handle(keys_pressed, player_batman)
        superman_movement_handle(keys_pressed, player_superman)
        handle_bullets(batman_bullets, player_batman, superman_bullets, player_superman)
        draw_window(player_superman, player_batman, batman_bullets, superman_bullets)

    pygame.quit()


if __name__ == "__main__":
    main()
