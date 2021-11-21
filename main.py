import pygame
import sys

from pygame.constants import SYSTEM_CURSOR_WAITARROW
from pygame.draw import line


def main():
    # General Setup
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()
    clock = pygame.time.Clock()

    # Setting up the main window
    screen_width = 1300
    screen_height = 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Castle Wars')

    # Global variables
    bg_color = (173, 203, 222)
    accent_color = (15, 97, 20)
    deck = pygame.Rect(0,535,screen_width, screen_height/4)
    floor = pygame.Rect(0,495,screen_width, 40)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            ##não funciona
            elif event.type == pygame.MOUSEBUTTONDOWN:
                carta_escolhida = mover(x)
                carta_escolhida[0].left, carta_escolhida[0].top = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                carta_escolhida[0].left = carta_escolhida[1][0]
                carta_escolhida[0].top = carta_escolhida[1][1]

        # Background Stuff
        screen.fill(bg_color)
        pygame.draw.rect(screen, accent_color, deck)
        x = cards(screen, screen_width, screen_height) ##8 cartas [0-7]
        pygame.draw.rect(screen, (19, 161, 36), floor)
        
        #castle stuff
        castle1(screen)
        castle2(screen)

        # Rendering
        pygame.display.flip()
        clock.tick(60)

#########Não funciona
def mover(x):
    pos_mouse = pygame.mouse.get_pos()
    ##carta1
    if pos_mouse[1] > 545 and pos_mouse[1] < 695:
        if pos_mouse[0] > 50 and pos_mouse[0] < 180:
            posicao_inicial = [50,545]
            return x[0],posicao_inicial
        elif pos_mouse[0] > 200 and pos_mouse[0] < 330:
            posicao_inicial = [200,545]
            return x[1], posicao_inicial
        elif pos_mouse[0] > 350 and pos_mouse[0] < 480:
            posicao_inicial = [350,545]
            return x[2], posicao_inicial
        elif pos_mouse[0] > 500 and pos_mouse[0] < 630:
            posicao_inicial = [500,545]
            return x[3], posicao_inicial
        elif pos_mouse[0] > 650 and pos_mouse[0] < 780:
            posicao_inicial = [650,545]
            return x[4], posicao_inicial
        elif pos_mouse[0] > 800 and pos_mouse[0] < 630:
            posicao_inicial = [800,545]
            return x[5], posicao_inicial
        elif pos_mouse[0] > 950 and pos_mouse[0] < 1074:
            posicao_inicial = [950,545]
            return x[6], posicao_inicial
        elif pos_mouse[0] > 1100 and pos_mouse[0] < 1224:
            posicao_inicial = [1100,545]
            return x[7], posicao_inicial
        else:
            return
    else: 
        return


def cards(screen, screen_width, screen_height):
    cards_color = (125, 128, 125)
    card1 = pygame.Rect(50,545,screen_width/10, screen_height/4 - 25)
    card2 = pygame.Rect(200,545,screen_width/10, screen_height/4 - 25)
    card3 = pygame.Rect(350,545,screen_width/10, screen_height/4 - 25)
    card4 = pygame.Rect(500,545,screen_width/10, screen_height/4 - 25)
    card5 = pygame.Rect(650,545,screen_width/10, screen_height/4 - 25)
    card6 = pygame.Rect(800,545,screen_width/10, screen_height/4 - 25)
    '''card7 = pygame.Rect(950,545,screen_width/10, screen_height/4 - 25)
    card8 = pygame.Rect(1100,545,screen_width/10, screen_height/4 - 25)'''
    pygame.draw.rect(screen, cards_color, card1)
    pygame.draw.rect(screen, cards_color, card2)
    pygame.draw.rect(screen, cards_color, card3)
    pygame.draw.rect(screen, cards_color, card4)
    pygame.draw.rect(screen, cards_color, card5)
    pygame.draw.rect(screen, cards_color, card6)
    '''pygame.draw.rect(screen, cards_color, card7)
    pygame.draw.rect(screen, cards_color, card8)'''
    ship7 = pygame.image.load("G_back.png")
    screen.blit(ship7, (950,545))
    ship8 = pygame.image.load("B_back.png")
    screen.blit(ship8, (1100,545))
    return card1,card2,card3,card4,card5,card6,ship7,ship8

def castle1(screen):
    castle1 = pygame.Rect(100, 295, 200,200)
    tower1 = pygame.Rect(90,280,40,40)
    tower2 = pygame.Rect(150,280,40,40)
    tower3 = pygame.Rect(210,280,40,40)
    tower4 = pygame.Rect(270,280,40,40)
    line1 = pygame.Rect(100, 480, 200, 2)
    line2 = pygame.Rect(100, 460, 200, 2)
    line3 = pygame.Rect(100, 440, 200, 2)
    line4 = pygame.Rect(100, 420, 200, 2)
    line5 = pygame.Rect(100, 400, 200, 2)
    line6 = pygame.Rect(100, 380, 200, 2)
    line7 = pygame.Rect(100, 360, 200, 2)
    line8 = pygame.Rect(100, 340, 200, 2)
    line9 = pygame.Rect(100, 320, 200, 2)
    line10 = pygame.Rect(100, 300, 200, 2)
    line_color = (66, 109, 161)
    tower_color = (29, 48, 71)
    pygame.draw.rect(screen, (40, 68, 102), castle1)
    pygame.draw.rect(screen, line_color, line1)
    pygame.draw.rect(screen, line_color, line2)
    pygame.draw.rect(screen, line_color, line3)
    pygame.draw.rect(screen, line_color, line4)
    pygame.draw.rect(screen, line_color, line5)
    pygame.draw.rect(screen, line_color, line6)
    pygame.draw.rect(screen, line_color, line7)
    pygame.draw.rect(screen, line_color, line8)
    pygame.draw.rect(screen, line_color, line9)
    pygame.draw.rect(screen, line_color, line10)
    row_castle1(screen,line_color)
    pygame.draw.rect(screen, tower_color, tower1)
    pygame.draw.rect(screen, tower_color, tower2)
    pygame.draw.rect(screen, tower_color, tower3)
    pygame.draw.rect(screen, tower_color, tower4)

def row_castle1(screen,line_color):
    row1 = pygame.Rect(120,480,2,15)
    row2 = pygame.Rect(160,480,2,15)
    row3 = pygame.Rect(200,480,2,15)
    row4 = pygame.Rect(240,480,2,15)
    row5 = pygame.Rect(280,480,2,15)
    ##
    row6 = pygame.Rect(140,460,2,20)
    row7 = pygame.Rect(180,460,2,20)
    row8 = pygame.Rect(220,460,2,20)
    row9 = pygame.Rect(260,460,2,20)
    row10 = pygame.Rect(298,460,2,20)
    ##
    row11 = pygame.Rect(120,440,2,20)
    row12 = pygame.Rect(160,440,2,20)
    row13 = pygame.Rect(200,440,2,20)
    row14 = pygame.Rect(240,440,2,20)
    row15 = pygame.Rect(280,440,2,20)
    ##
    row16 = pygame.Rect(140,420,2,20)
    row17 = pygame.Rect(180,420,2,20)
    row18 = pygame.Rect(220,420,2,20)
    row19 = pygame.Rect(260,420,2,20)
    row20 = pygame.Rect(298,420,2,20)
    ##
    row21 = pygame.Rect(120,400,2,20)
    row22 = pygame.Rect(160,400,2,20)
    row23 = pygame.Rect(200,400,2,20)
    row24 = pygame.Rect(240,400,2,20)
    row25 = pygame.Rect(280,400,2,20)
    ##
    row26 = pygame.Rect(140,380,2,20)
    row27 = pygame.Rect(180,380,2,20)
    row28 = pygame.Rect(220,380,2,20)
    row29 = pygame.Rect(260,380,2,20)
    row30 = pygame.Rect(298,380,2,20)
    ##
    row31 = pygame.Rect(120,360,2,20)
    row32 = pygame.Rect(160,360,2,20)
    row33 = pygame.Rect(200,360,2,20)
    row34 = pygame.Rect(240,360,2,20)
    row35 = pygame.Rect(280,360,2,20)
    ##
    row36 = pygame.Rect(140,340,2,20)
    row37 = pygame.Rect(180,340,2,20)
    row38 = pygame.Rect(220,340,2,20)
    row39 = pygame.Rect(260,340,2,20)
    row40 = pygame.Rect(298,340,2,20)
    ##
    row41 = pygame.Rect(120,320,2,20)
    row42 = pygame.Rect(160,320,2,20)
    row43 = pygame.Rect(200,320,2,20)
    row44 = pygame.Rect(240,320,2,20)
    row45 = pygame.Rect(280,320,2,20)
    ##
    row46 = pygame.Rect(140,300,2,20)
    row47 = pygame.Rect(180,300,2,20)
    row48 = pygame.Rect(220,300,2,20)
    row49 = pygame.Rect(260,300,2,20)
    row50 = pygame.Rect(298,300,2,20)
    pygame.draw.rect(screen, line_color, row1)
    pygame.draw.rect(screen, line_color, row2)
    pygame.draw.rect(screen, line_color, row3)
    pygame.draw.rect(screen, line_color, row4)
    pygame.draw.rect(screen, line_color, row5)
    pygame.draw.rect(screen, line_color, row6)
    pygame.draw.rect(screen, line_color, row7)
    pygame.draw.rect(screen, line_color, row8)
    pygame.draw.rect(screen, line_color, row9)
    pygame.draw.rect(screen, line_color, row10)
    pygame.draw.rect(screen, line_color, row11)
    pygame.draw.rect(screen, line_color, row12)
    pygame.draw.rect(screen, line_color, row13)
    pygame.draw.rect(screen, line_color, row14)
    pygame.draw.rect(screen, line_color, row15)
    pygame.draw.rect(screen, line_color, row16)
    pygame.draw.rect(screen, line_color, row17)
    pygame.draw.rect(screen, line_color, row18)
    pygame.draw.rect(screen, line_color, row19)
    pygame.draw.rect(screen, line_color, row20)
    pygame.draw.rect(screen, line_color, row21)
    pygame.draw.rect(screen, line_color, row22)
    pygame.draw.rect(screen, line_color, row23)
    pygame.draw.rect(screen, line_color, row24)
    pygame.draw.rect(screen, line_color, row25)
    pygame.draw.rect(screen, line_color, row26)
    pygame.draw.rect(screen, line_color, row27)
    pygame.draw.rect(screen, line_color, row28)
    pygame.draw.rect(screen, line_color, row29)
    pygame.draw.rect(screen, line_color, row30)
    pygame.draw.rect(screen, line_color, row31)
    pygame.draw.rect(screen, line_color, row32)
    pygame.draw.rect(screen, line_color, row33)
    pygame.draw.rect(screen, line_color, row34)
    pygame.draw.rect(screen, line_color, row35)
    pygame.draw.rect(screen, line_color, row36)
    pygame.draw.rect(screen, line_color, row37)
    pygame.draw.rect(screen, line_color, row38)
    pygame.draw.rect(screen, line_color, row39)
    pygame.draw.rect(screen, line_color, row40)
    pygame.draw.rect(screen, line_color, row41)
    pygame.draw.rect(screen, line_color, row42)
    pygame.draw.rect(screen, line_color, row43)
    pygame.draw.rect(screen, line_color, row44)
    pygame.draw.rect(screen, line_color, row45)
    pygame.draw.rect(screen, line_color, row46)
    pygame.draw.rect(screen, line_color, row47)
    pygame.draw.rect(screen, line_color, row48)
    pygame.draw.rect(screen, line_color, row49)
    pygame.draw.rect(screen, line_color, row50)

def castle2(screen):
    castle2 = pygame.Rect(1000, 295, 200,200)
    tower1 = pygame.Rect(990,280,40,40)
    tower2 = pygame.Rect(1050,280,40,40)
    tower3 = pygame.Rect(1110,280,40,40)
    tower4 = pygame.Rect(1170,280,40,40)
    line1 = pygame.Rect(1000, 480, 200, 2)
    line2 = pygame.Rect(1000, 460, 200, 2)
    line3 = pygame.Rect(1000, 440, 200, 2)
    line4 = pygame.Rect(1000, 420, 200, 2)
    line5 = pygame.Rect(1000, 400, 200, 2)
    line6 = pygame.Rect(1000, 380, 200, 2)
    line7 = pygame.Rect(1000, 360, 200, 2)
    line8 = pygame.Rect(1000, 340, 200, 2)
    line9 = pygame.Rect(1000, 320, 200, 2)
    line10 = pygame.Rect(1000, 300, 200, 2)
    line_color = (156, 86, 64)
    tower_color = (66, 36, 27)
    pygame.draw.rect(screen, (125, 57, 35), castle2)
    pygame.draw.rect(screen, line_color, line1)
    pygame.draw.rect(screen, line_color, line2)
    pygame.draw.rect(screen, line_color, line3)
    pygame.draw.rect(screen, line_color, line4)
    pygame.draw.rect(screen, line_color, line5)
    pygame.draw.rect(screen, line_color, line6)
    pygame.draw.rect(screen, line_color, line7)
    pygame.draw.rect(screen, line_color, line8)
    pygame.draw.rect(screen, line_color, line9)
    pygame.draw.rect(screen, line_color, line10)
    row_castle2(screen, line_color)
    pygame.draw.rect(screen, tower_color, tower1)
    pygame.draw.rect(screen, tower_color, tower2)
    pygame.draw.rect(screen, tower_color, tower3)
    pygame.draw.rect(screen, tower_color, tower4)

def row_castle2(screen,line_color):
    row1 = pygame.Rect(1020,480,2,15)
    row2 = pygame.Rect(1060,480,2,15)
    row3 = pygame.Rect(1100,480,2,15)
    row4 = pygame.Rect(1140,480,2,15)
    row5 = pygame.Rect(1180,480,2,15)
    ##
    row6 = pygame.Rect(1040,460,2,20)
    row7 = pygame.Rect(1080,460,2,20)
    row8 = pygame.Rect(1120,460,2,20)
    row9 = pygame.Rect(1160,460,2,20)
    row10 = pygame.Rect(1198,460,2,20)
    ##
    row11 = pygame.Rect(1020,440,2,20)
    row12 = pygame.Rect(1060,440,2,20)
    row13 = pygame.Rect(1100,440,2,20)
    row14 = pygame.Rect(1140,440,2,20)
    row15 = pygame.Rect(1180,440,2,20)
    ##
    row16 = pygame.Rect(1040,420,2,20)
    row17 = pygame.Rect(1080,420,2,20)
    row18 = pygame.Rect(1120,420,2,20)
    row19 = pygame.Rect(1160,420,2,20)
    row20 = pygame.Rect(1198,420,2,20)
    ##
    row21 = pygame.Rect(1020,400,2,20)
    row22 = pygame.Rect(1060,400,2,20)
    row23 = pygame.Rect(1100,400,2,20)
    row24 = pygame.Rect(1140,400,2,20)
    row25 = pygame.Rect(1180,400,2,20)
    ##
    row26 = pygame.Rect(1040,380,2,20)
    row27 = pygame.Rect(1080,380,2,20)
    row28 = pygame.Rect(1120,380,2,20)
    row29 = pygame.Rect(1160,380,2,20)
    row30 = pygame.Rect(1198,380,2,20)
    ##
    row31 = pygame.Rect(1020,360,2,20)
    row32 = pygame.Rect(1060,360,2,20)
    row33 = pygame.Rect(1100,360,2,20)
    row34 = pygame.Rect(1140,360,2,20)
    row35 = pygame.Rect(1180,360,2,20)
    ##
    row36 = pygame.Rect(1040,340,2,20)
    row37 = pygame.Rect(1080,340,2,20)
    row38 = pygame.Rect(1120,340,2,20)
    row39 = pygame.Rect(1160,340,2,20)
    row40 = pygame.Rect(1198,340,2,20)
    ##
    row41 = pygame.Rect(1020,320,2,20)
    row42 = pygame.Rect(1060,320,2,20)
    row43 = pygame.Rect(1100,320,2,20)
    row44 = pygame.Rect(1140,320,2,20)
    row45 = pygame.Rect(1180,320,2,20)
    ##
    row46 = pygame.Rect(1040,300,2,20)
    row47 = pygame.Rect(1080,300,2,20)
    row48 = pygame.Rect(1120,300,2,20)
    row49 = pygame.Rect(1160,300,2,20)
    row50 = pygame.Rect(1198,300,2,20)
    pygame.draw.rect(screen, line_color, row1)
    pygame.draw.rect(screen, line_color, row2)
    pygame.draw.rect(screen, line_color, row3)
    pygame.draw.rect(screen, line_color, row4)
    pygame.draw.rect(screen, line_color, row5)
    pygame.draw.rect(screen, line_color, row6)
    pygame.draw.rect(screen, line_color, row7)
    pygame.draw.rect(screen, line_color, row8)
    pygame.draw.rect(screen, line_color, row9)
    pygame.draw.rect(screen, line_color, row10)
    pygame.draw.rect(screen, line_color, row11)
    pygame.draw.rect(screen, line_color, row12)
    pygame.draw.rect(screen, line_color, row13)
    pygame.draw.rect(screen, line_color, row14)
    pygame.draw.rect(screen, line_color, row15)
    pygame.draw.rect(screen, line_color, row16)
    pygame.draw.rect(screen, line_color, row17)
    pygame.draw.rect(screen, line_color, row18)
    pygame.draw.rect(screen, line_color, row19)
    pygame.draw.rect(screen, line_color, row20)
    pygame.draw.rect(screen, line_color, row21)
    pygame.draw.rect(screen, line_color, row22)
    pygame.draw.rect(screen, line_color, row23)
    pygame.draw.rect(screen, line_color, row24)
    pygame.draw.rect(screen, line_color, row25)
    pygame.draw.rect(screen, line_color, row26)
    pygame.draw.rect(screen, line_color, row27)
    pygame.draw.rect(screen, line_color, row28)
    pygame.draw.rect(screen, line_color, row29)
    pygame.draw.rect(screen, line_color, row30)
    pygame.draw.rect(screen, line_color, row31)
    pygame.draw.rect(screen, line_color, row32)
    pygame.draw.rect(screen, line_color, row33)
    pygame.draw.rect(screen, line_color, row34)
    pygame.draw.rect(screen, line_color, row35)
    pygame.draw.rect(screen, line_color, row36)
    pygame.draw.rect(screen, line_color, row37)
    pygame.draw.rect(screen, line_color, row38)
    pygame.draw.rect(screen, line_color, row39)
    pygame.draw.rect(screen, line_color, row40)
    pygame.draw.rect(screen, line_color, row41)
    pygame.draw.rect(screen, line_color, row42)
    pygame.draw.rect(screen, line_color, row43)
    pygame.draw.rect(screen, line_color, row44)
    pygame.draw.rect(screen, line_color, row45)
    pygame.draw.rect(screen, line_color, row46)
    pygame.draw.rect(screen, line_color, row47)
    pygame.draw.rect(screen, line_color, row48)
    pygame.draw.rect(screen, line_color, row49)
    pygame.draw.rect(screen, line_color, row50)

if __name__ == "__main__":
    main()
