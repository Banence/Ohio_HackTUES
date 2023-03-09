import pygame
import os

pygame.init()

WIDTH = 1920
HEIGHT = 1080
SCR = pygame.display.set_mode((WIDTH, HEIGHT))
COL = (52, 78, 91)
pygame.display.set_caption('Ohio Security')
TAB_image = pygame.image.load(os.path.join('Images', 'TabletWHandsColor.png'))
TAB_WIDTH, TAB_HEIGHT = 1540, 950 
TAB = pygame.transform.scale(TAB_image, (TAB_WIDTH, TAB_HEIGHT))
FPS = 60

INTRO_FONT = pygame.font.SysFont('Rouhtem.ttf', 40)
INTRO_TEXT = INTRO_FONT.render("ESCAPE - MENU", True, (255, 255, 255))

MAIN_IMAGE = pygame.image.load(os.path.join('Images', 'houseWColorAndPickture.png')).convert_alpha()
MAIN_WIDTH, MAIN_HEIGHT = 1030, 740
MAIN = pygame.transform.scale(MAIN_IMAGE, (MAIN_WIDTH, MAIN_HEIGHT))


OPENED_DOOR_IMAGE = pygame.image.load(os.path.join('Images','DoorOpenedColored.png'))
OPENED_DOOR_WIDTH, OPENED_DOOR_HEIGHT = 60, 100
OPENED_DOOR = pygame.transform.scale(OPENED_DOOR_IMAGE, (OPENED_DOOR_WIDTH, OPENED_DOOR_HEIGHT))

CLOSED_DOOR_IMAGE = pygame.image.load(os.path.join('Images','DoorClosedColored.png'))
CLOSED_DOOR_WIDTH, CLOSED_DOOR_HEIGHT = 60, 100
CLOSED_DOOR = pygame.transform.scale(CLOSED_DOOR_IMAGE, (CLOSED_DOOR_WIDTH, CLOSED_DOOR_HEIGHT))

def draw_window(tab):
    SCR.fill(COL)
    SCR.blit(TAB, (tab.x, tab.y))
    SCR.blit(INTRO_TEXT, (20, 40))
    SCR.blit(MAIN, (WIDTH//2 - MAIN_WIDTH// 2, HEIGHT//2 - MAIN_HEIGHT// 2 - 106))
    SCR.blit(OPENED_DOOR, (700, 695))
    SCR.blit(OPENED_DOOR, (1074,695))
    SCR.blit(OPENED_DOOR, (620, 503))
    SCR.blit(OPENED_DOOR, (880, 503))
    SCR.blit(OPENED_DOOR, (1174, 503))
    SCR.blit(OPENED_DOOR, (768, 285))
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
                exit()

        draw_window(tab)

main()

if __name__ == "__main__":
    main()
