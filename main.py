import pygame

pygame.init()

WIDTH = 1280
HEIGHT = 720
SCR = pygame.display.set_mode((WIDTH, HEIGHT))
COL = (69, 69, 69)
pygame.display.set_caption('Ohio Security')

FPS = 60


def draw_window():
    SCR.fill(COL)
    pygame.display.update()

def main():

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
   
        draw_window()
main()

if __name__ == "__main__":
    main()
