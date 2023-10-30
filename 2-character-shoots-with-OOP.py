from cmath import inf
from json.encoder import INFINITY
from sys import platlibdir
from tracemalloc import stop
import pygame
import os

pygame.font.init()


WIDTH, HEIGHT = 900, 500  # set width and heigh of the game screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # initiate the game window
pygame.display.set_caption("My first pygame game")  # change the title

WHITE = (255, 255, 255)  # set constant value for white color
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

HEALTH_FONT = pygame.font.SysFont('times', 20)
WINNER_FONT = pygame.font.SysFont('times', 60)

FPS = 60  # set the frame rate

CHARACTER_WIDTH = 100
CHARACTER_HEIGHT = 100

VELOCITY = 5
BULLET_VELOCITY = 15
MAX_BULLET = 10

IRONMAN_HIT = pygame.USEREVENT + 1
CAPTAIN_HIT = pygame.USEREVENT + 2

IRONMAN_IMAGE = pygame.image.load(r'D:\iron-man.png')
IRONMAN = pygame.transform.scale(IRONMAN_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))  # resize the object

CAPTAIN_IMAGE = pygame.image.load(r'D:\captain-america.png')
CAPTAIN = pygame.transform.scale(CAPTAIN_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))  # resize the object

VERSUS_IMAGE = pygame.image.load(r'D:\vs.png')
VERSUS = pygame.transform.scale(VERSUS_IMAGE, (100, 100))


def draw_window(player_ironman, player_captain, ironman_bullet, captain_bullet, ironman_health, captain_health):
    'function to update pygame window'
    WIN.fill(WHITE)  # set the background color for pygame window
    WIN.blit(IRONMAN, (player_ironman.x, player_ironman.y))  
    WIN.blit(CAPTAIN, (player_captain.x, player_captain.y))  
    WIN.blit(VERSUS, pygame.Rect(405, 200, 100, 100))
    pygame.draw.rect(WIN, (0, 0, 0), pygame.Rect(450, 0, 10, 200))
    pygame.draw.rect(WIN, (0, 0, 0), pygame.Rect(450, 300, 10, 200))
    
    ironman_health_text = HEALTH_FONT.render("Health:" + str(ironman_health), 1, BLUE)
    WIN.blit(ironman_health_text, (WIDTH - 80, HEIGHT - 20))
    
    captain_health_text = HEALTH_FONT.render("Health:" + str(captain_health), 1, BLUE)
    WIN.blit(captain_health_text, (0, 0))
    
    for bullet in ironman_bullet:
        pygame.draw.rect(WIN, GREEN, bullet)
    
    for bullet in captain_bullet:
        pygame.draw.rect(WIN, RED, bullet)

    pygame.display.flip()
    pygame.display.update()  # update display
    
    
class Handle(draw_window):
    
    def __init__(self, player_ironman, player_captain):
        self.ironman = player_ironman
        self.captain = player_captain
        
    def ironman_movement_handle(self, key_pressed):
        
        if (key_pressed[pygame.K_LEFT]):
            self.ironman.x -= VELOCITY
        if (key_pressed[pygame.K_RIGHT]):
            self.ironman.x += VELOCITY
        if (key_pressed[pygame.K_UP]):
            self.ironman.y -= VELOCITY
        if (key_pressed[pygame.K_DOWN]):
            self.ironman.y += VELOCITY
        
        if self.ironman.x <= 430:
            self.ironman.x = 430
        if self.ironman.x >= 800:
            self.ironman.x = 800 
        if self.ironman.y <= 0:
            self.ironman.y = 0
        if self.ironman.y >= 375:
            self.ironman.y = 375  
            
            
    def captain_movement_handle(self, keys_pressed):
    
        if (keys_pressed[pygame.K_a]):  
            self.captain.x -= VELOCITY  
        if (keys_pressed[pygame.K_d]):  
            self.captain.x += VELOCITY  
        if (keys_pressed[pygame.K_w]):  
            self.captain.y -= VELOCITY  
        if (keys_pressed[pygame.K_s]):  
            self.captain.y += VELOCITY  
        
        # Keep player_captain on the screen    
        if self.captain.x <= 0:
            self.captain.x = 0
        if self.captain.x >= 350:
            self.captain.x = 350
        if self.captain.y <= 0:
            self.captain.y = 0
        if self.captain.y >= 380:
            self.captain.y = 380
            
    

            
            
Handle_movement = Handle()
