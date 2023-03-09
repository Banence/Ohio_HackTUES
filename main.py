import pygame
import os
import sys

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
CLOSED_DOOR_WIDTH, CLOSED_DOOR_HEIGHT = 20, 100
CLOSED_DOOR = pygame.transform.scale(CLOSED_DOOR_IMAGE, (CLOSED_DOOR_WIDTH, CLOSED_DOOR_HEIGHT))


D1_WIDTH, D1_HEIGHT = 700, 695
D2_WIDTH, D2_HEIGHT = 1074, 695
D3_WIDTH, D3_HEIGHT = 620, 503
D4_WIDTH, D4_HEIGHT = 880, 503
D5_WIDTH, D5_HEIGHT = 1174, 503
D6_WIDTH, D6_HEIGHT = 768, 285

# Colors for the squares
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

squares = [
    pygame.Rect((D1_WIDTH, D1_HEIGHT), (CLOSED_DOOR_WIDTH, CLOSED_DOOR_HEIGHT)),
    pygame.Rect((D2_WIDTH, D2_HEIGHT), (CLOSED_DOOR_WIDTH, CLOSED_DOOR_HEIGHT)),
    pygame.Rect((D3_WIDTH, D3_HEIGHT), (CLOSED_DOOR_WIDTH, CLOSED_DOOR_HEIGHT)),
    pygame.Rect((D4_WIDTH, D4_HEIGHT), (CLOSED_DOOR_WIDTH, CLOSED_DOOR_HEIGHT)),
    pygame.Rect((D5_WIDTH, D5_HEIGHT), (CLOSED_DOOR_WIDTH, CLOSED_DOOR_HEIGHT)),
    pygame.Rect((D6_WIDTH, D6_HEIGHT), (CLOSED_DOOR_WIDTH, CLOSED_DOOR_HEIGHT))
]

# Create a list to keep track of the state of each square
square_states = [False] * len(squares)

def draw_window(tab):
    SCR.fill(COL)
    SCR.blit(TAB, (tab.x, tab.y))
    SCR.blit(INTRO_TEXT, (20, 40))
    SCR.blit(MAIN, (WIDTH//2 - MAIN_WIDTH// 2, HEIGHT//2 - MAIN_HEIGHT// 2 - 106))
    
    
   

def main():
    tab = pygame.Rect(WIDTH//2 - TAB_WIDTH//2, HEIGHT - TAB_HEIGHT, TAB_WIDTH, TAB_HEIGHT)
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the user clicked on a square
                for i, square in enumerate(squares):
                    if square.collidepoint(event.pos):
                        # Toggle the state of the square
                        square_states[i] = not square_states[i]
        
        # Draw the squares onto the screen
        for i, square in enumerate(squares):
            if square_states[i]: 
                image = CLOSED_DOOR    
            else:
                image = OPENED_DOOR
            if i==0:
                if image == CLOSED_DOOR:
                    SCR.blit(CLOSED_DOOR, (D1_WIDTH + OPENED_DOOR_WIDTH -14 , D1_HEIGHT))
                else:
                    SCR.blit(OPENED_DOOR, square)
            if i==1:
                if image == CLOSED_DOOR:
                    SCR.blit(CLOSED_DOOR, (D2_WIDTH + OPENED_DOOR_WIDTH -15 , D2_HEIGHT))
                else:
                    SCR.blit(OPENED_DOOR, square)
            if i==2:
                if image == CLOSED_DOOR:
                    SCR.blit(CLOSED_DOOR, (D3_WIDTH + OPENED_DOOR_WIDTH -17 , D3_HEIGHT))
                else:
                    SCR.blit(OPENED_DOOR, square)
            if i==3:
                if image == CLOSED_DOOR:
                    SCR.blit(CLOSED_DOOR, (D4_WIDTH + OPENED_DOOR_WIDTH -18 , D4_HEIGHT))
                else:
                    SCR.blit(OPENED_DOOR, square)
            if i==4:
                if image == CLOSED_DOOR:
                    SCR.blit(CLOSED_DOOR, (D5_WIDTH + OPENED_DOOR_WIDTH -17 , D5_HEIGHT))
                else:
                    SCR.blit(OPENED_DOOR, square)
            if i==5:
                if image == CLOSED_DOOR:
                    SCR.blit(CLOSED_DOOR, (D6_WIDTH + OPENED_DOOR_WIDTH -16 , D6_HEIGHT))
                else:
                    SCR.blit(OPENED_DOOR, square)
        
        pygame.display.update()

        draw_window(tab)
main()

if __name__ == "__main__":
    main()
