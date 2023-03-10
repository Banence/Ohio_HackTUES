import pygame
import os
import sys

pygame.init()

WIDTH = 1920
HEIGHT = 1080
SCR = pygame.display.set_mode((WIDTH, HEIGHT))
COL = (220, 92, 0)
pygame.display.set_caption('Ohio Security')
TAB_image = pygame.image.load(os.path.join('Images', 'TabletWHandsColor.png'))
TAB_WIDTH, TAB_HEIGHT = 1540, 950 
TAB = pygame.transform.scale(TAB_image, (TAB_WIDTH, TAB_HEIGHT))
FPS = 60

MAIN_IMAGE = pygame.image.load(os.path.join('Images', 'houseWColorAndPickture.png')).convert_alpha()
MAIN_WIDTH, MAIN_HEIGHT = 1030, 740
MAIN = pygame.transform.scale(MAIN_IMAGE, (MAIN_WIDTH, MAIN_HEIGHT))


OPENED_DOOR_IMAGE = pygame.image.load(os.path.join('images','DoorOpenedColored.png'))
OPENED_DOOR_WIDTH, OPENED_DOOR_HEIGHT = 60, 100
OPENED_DOOR = pygame.transform.scale(OPENED_DOOR_IMAGE, (OPENED_DOOR_WIDTH, OPENED_DOOR_HEIGHT))

CLOSED_DOOR_IMAGE = pygame.image.load(os.path.join('images','DoorClosedColored.png'))
CLOSED_DOOR_WIDTH, CLOSED_DOOR_HEIGHT = 20, 100
CLOSED_DOOR = pygame.transform.scale(CLOSED_DOOR_IMAGE, (CLOSED_DOOR_WIDTH, CLOSED_DOOR_HEIGHT))

GREY_BG = pygame.image.load(os.path.join('images', 'Grey.jpg'))
GREY_BG_WIDTH, MATRIX_BG_HEIGHT = 1920, 1080
GREY = pygame.transform.scale(GREY_BG, (GREY_BG_WIDTH, MATRIX_BG_HEIGHT))


D1_WIDTH, D1_HEIGHT = 700, 695
D2_WIDTH, D2_HEIGHT = 1074, 695
D3_WIDTH, D3_HEIGHT = 620, 503
D4_WIDTH, D4_HEIGHT = 880, 503
D5_WIDTH, D5_HEIGHT = 1174, 503
D6_WIDTH, D6_HEIGHT = 768, 285

THIEFCOLORED = pygame.image.load(os.path.join('images', 'ThiefColored.png'))
THIEFCOLORED_WIDTH, THIEFCOLORED_HEIGHT = 70, 80
THIEF = pygame.transform.scale(THIEFCOLORED, (THIEFCOLORED_WIDTH, THIEFCOLORED_HEIGHT))

THIEFCOLOREDINVERTED = pygame.image.load(os.path.join('images', 'ThiefColoredRotated.png'))
THIEFCOLOREDINVERTED_WIDTH, THIEFCOLOREDINVERTED_HEIGHT = 70, 80
THIEF_INVERTED = pygame.transform.scale(THIEFCOLOREDINVERTED, (THIEFCOLOREDINVERTED_WIDTH, THIEFCOLOREDINVERTED_HEIGHT))

PLAYER_LOAD = pygame.image.load(os.path.join('images', 'playerColored.png'))
PLAYER_WIDTH, PLAYER_HEIGHT = 40, 120
PLAYER = pygame.transform.scale(PLAYER_LOAD, (PLAYER_WIDTH, PLAYER_HEIGHT))

squares = [
    pygame.Rect((D1_WIDTH, D1_HEIGHT), (CLOSED_DOOR_WIDTH, CLOSED_DOOR_HEIGHT)),
    pygame.Rect((D2_WIDTH, D2_HEIGHT), (CLOSED_DOOR_WIDTH, CLOSED_DOOR_HEIGHT)),
    pygame.Rect((D3_WIDTH, D3_HEIGHT), (CLOSED_DOOR_WIDTH, CLOSED_DOOR_HEIGHT)),
    pygame.Rect((D4_WIDTH, D4_HEIGHT), (CLOSED_DOOR_WIDTH, CLOSED_DOOR_HEIGHT)),
    pygame.Rect((D5_WIDTH, D5_HEIGHT), (CLOSED_DOOR_WIDTH, CLOSED_DOOR_HEIGHT)),
    pygame.Rect((D6_WIDTH, D6_HEIGHT), (CLOSED_DOOR_WIDTH, CLOSED_DOOR_HEIGHT))
]

square_states = [False] * len(squares)

def main():
    tab = pygame.Rect(WIDTH//2 - TAB_WIDTH//2, HEIGHT - TAB_HEIGHT, TAB_WIDTH, TAB_HEIGHT)
    clock = pygame.time.Clock()

    square_size = 50
    square_x = 550
    square_y = D1_HEIGHT + OPENED_DOOR_HEIGHT - square_size - 32
    speed = 3
    direction = 1
    z = 0

    paused = False
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, square in enumerate(squares):
                    if square.collidepoint(event.pos):
                        square_states[i] = not square_states[i]
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = True # toggle pause state
                elif event.key == pygame.K_SPACE:
                    paused = False # resume game
                elif event.key == pygame.K_q and paused == True:
                    pygame.quit()
                    quit()

        if not paused: # game runs only if not paused
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

            square_x += speed * direction

            # Check if square has reached end of screen
            if square_x < 550 or square_x > 1300:
                # Move square up and flip direction
                if z != 0:
                    square_y -= 217
                    direction *= -1  
                else:
                    square_y -= 191
                    direction *= -1
                
                z += 1
            # Draw square
            if direction == 1:
                SCR.blit(THIEF, (square_x, square_y))
            else: 
                SCR.blit(THIEF_INVERTED, (square_x, square_y))
            # Update screen
            pygame.display.flip()

            pygame.time.wait(10)
            
            pygame.display.update()

        else: # game is paused
            # display pause screen
            SCR.blit(GREY, (WIDTH//2 - GREY.get_width()//2, HEIGHT//2 - GREY.get_height()//2))
            font = pygame.font.SysFont('comicsans', 50)
            text = font.render('Game Paused (Press "SPACE" to resume or "Q" to QUIT)', True, (69, 69, 69))
            SCR.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
            pygame.display.update()

        SCR.fill(COL)
        SCR.blit(TAB, (tab.x, tab.y))
        SCR.blit(MAIN, (WIDTH//2 - MAIN_WIDTH// 2, HEIGHT//2 - MAIN_HEIGHT// 2 - 106))
        SCR.blit(PLAYER, (1380, 265))
        
main()

if __name__ == "__main__":
    main()
