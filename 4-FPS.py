import pygame


WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My first pygame game")

WHITE = (255, 255, 255)


def main():

    i = 1
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        WIN.fill(WHITE)
        pygame.display.update()
        print(i)
        i += 1

    pygame.quit()


if __name__ == "__main__":
    main()
