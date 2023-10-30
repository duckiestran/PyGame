import pygame


WIDTH, HEIGHT = 900, 500  # set width and heigh of the game screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # initiate the game window
pygame.display.set_caption("My first pygame game")  # change the title

WHITE = (255, 255, 255)  # set constant value for white color

FPS = 60  # set the frame rate


def main():

    clock = pygame.time.Clock()  # initiate the clock variable for controling framerate
    i = 1
    run = True
    while run:
        clock.tick(FPS)  # control the framerate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        WIN.fill(WHITE)  # set the background color for pygame window
        pygame.display.update()  # update display
        print(i)
        i += 1

    pygame.quit()


if __name__ == "__main__":
    main()
