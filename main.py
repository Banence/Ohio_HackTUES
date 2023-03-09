import pygame
import os
pygame.init()

WIDTH = 1280
HEIGHT = 720
SCR = pygame.display.set_mode((WIDTH, HEIGHT))
COL = (69, 69, 69)
pygame.display.set_caption('Ohio Security')
TAB_image = pygame.image.load(os.path.join('Images', 'TabletWHandsColor.png'))
TAB_WIDTH, TAB_HEIGHT = 1200, 605 
TAB = pygame.transform.scale(TAB_image, (TAB_WIDTH, TAB_HEIGHT))
FPS = 60


def draw_window(tab):
    SCR.fill(COL)
    SCR.blit(TAB, (tab.x, tab.y))
    pygame.display.update()

def main():
    tab = pygame.Rect(WIDTH//2 - TAB_WIDTH//2, HEIGHT - TAB_HEIGHT, TAB_WIDTH, TAB_HEIGHT)
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
   
        draw_window(tab)
main()

if __name__ == "__main__":
    main()
