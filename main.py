import pygame
import sys
import typing

from pygame.constants import SYSTEM_CURSOR_WAITARROW
from pygame.draw import line
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from carta import Carta


def main():
    # General Setup
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()
    clock = pygame.time.Clock()

    # Setting up the main window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Castle Wars')

    # Global variables
    bg_color = (173, 203, 222)
    accent_color = (15, 97, 20)
    text_color = (38, 40, 41)
    deck = pygame.Rect(0, 535, SCREEN_WIDTH, SCREEN_HEIGHT / 4)
    floor = pygame.Rect(0, 495, SCREEN_WIDTH, 40)

    # Texto
    font = pygame.font.Font("freesansbold.ttf", 20)

    cartas = cria_cartas_usuario()
    carta_selecionada: Carta = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Se o mouse está clicado seleciona a carta que colidiu o evento.
                for carta in cartas:
                    if carta.collidepoint(event.pos):
                        carta_selecionada = carta
            elif event.type == pygame.MOUSEBUTTONUP:
                # Botão do mouse foi solto desceleciona a carta e deixa-a parada.
                if carta_selecionada is not None:
                    """ 
                    Rects não tem função pra deletar pelo que eu achei, entã só move cartas pra fora da tela
                    e as condições para as cartas serem deletadas não leva em consideração em qual daz zonas
                    ela se encontra, apensa se está acima da área da mão, elaborar isso na versão final
                    """
                    if carta_selecionada.y < (SCREEN_HEIGHT - ((SCREEN_HEIGHT / 4) + 40)):
                        carta_selecionada.x = -200
                        carta_selecionada.y = 0
                        carta_selecionada = None
                    else:
                        carta_selecionada.x = carta_selecionada.posicao_inicial[0]
                        carta_selecionada.y = carta_selecionada.posicao_inicial[1]
                        carta_selecionada = None
            elif event.type == pygame.MOUSEMOTION:
                # No movimento do mouse "arrasta" a carta junto.
                if carta_selecionada is not None:
                    botao_esquerdo_pressionado = event.buttons[0]
                    if botao_esquerdo_pressionado:
                        print(event)
                        carta_selecionada.x = event.pos[0]
                        carta_selecionada.y = event.pos[1]

        # Background Stuff
        screen.fill(bg_color)
        pygame.draw.rect(screen, accent_color, deck)
        pygame.draw.rect(screen, (19, 161, 36), floor)
        zona_jogo = font.render("Zona de Jogo", False, text_color)
        zona_descarte = font.render("Zona de Descarte", False, text_color)
        screen.blit(zona_jogo, (200, 100))
        screen.blit(zona_descarte, (SCREEN_WIDTH - 350, 100))

        # castle stuff
        castle1(screen)
        castle2(screen)

        for carta in cartas:
            carta.draw(screen)
        # Rendering
        pygame.display.flip()
        clock.tick(60)


def cria_cartas_usuario() -> typing.List[Carta]:
    initial_left = 50
    TOP = 545
    return [Carta('', 0, '', (i * 150) + initial_left, TOP) for i in range(8)]


def castle1(screen):
    castle1 = pygame.Rect(100, 295, 200, 200)
    tower1 = pygame.Rect(90, 280, 40, 40)
    tower2 = pygame.Rect(150, 280, 40, 40)
    tower3 = pygame.Rect(210, 280, 40, 40)
    tower4 = pygame.Rect(270, 280, 40, 40)
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
    row_castle1(screen, line_color)
    pygame.draw.rect(screen, tower_color, tower1)
    pygame.draw.rect(screen, tower_color, tower2)
    pygame.draw.rect(screen, tower_color, tower3)
    pygame.draw.rect(screen, tower_color, tower4)


def row_castle1(screen, line_color):
    row1 = pygame.Rect(120, 480, 2, 15)
    row2 = pygame.Rect(160, 480, 2, 15)
    row3 = pygame.Rect(200, 480, 2, 15)
    row4 = pygame.Rect(240, 480, 2, 15)
    row5 = pygame.Rect(280, 480, 2, 15)
    ##
    row6 = pygame.Rect(140, 460, 2, 20)
    row7 = pygame.Rect(180, 460, 2, 20)
    row8 = pygame.Rect(220, 460, 2, 20)
    row9 = pygame.Rect(260, 460, 2, 20)
    row10 = pygame.Rect(298, 460, 2, 20)
    ##
    row11 = pygame.Rect(120, 440, 2, 20)
    row12 = pygame.Rect(160, 440, 2, 20)
    row13 = pygame.Rect(200, 440, 2, 20)
    row14 = pygame.Rect(240, 440, 2, 20)
    row15 = pygame.Rect(280, 440, 2, 20)
    ##
    row16 = pygame.Rect(140, 420, 2, 20)
    row17 = pygame.Rect(180, 420, 2, 20)
    row18 = pygame.Rect(220, 420, 2, 20)
    row19 = pygame.Rect(260, 420, 2, 20)
    row20 = pygame.Rect(298, 420, 2, 20)
    ##
    row21 = pygame.Rect(120, 400, 2, 20)
    row22 = pygame.Rect(160, 400, 2, 20)
    row23 = pygame.Rect(200, 400, 2, 20)
    row24 = pygame.Rect(240, 400, 2, 20)
    row25 = pygame.Rect(280, 400, 2, 20)
    ##
    row26 = pygame.Rect(140, 380, 2, 20)
    row27 = pygame.Rect(180, 380, 2, 20)
    row28 = pygame.Rect(220, 380, 2, 20)
    row29 = pygame.Rect(260, 380, 2, 20)
    row30 = pygame.Rect(298, 380, 2, 20)
    ##
    row31 = pygame.Rect(120, 360, 2, 20)
    row32 = pygame.Rect(160, 360, 2, 20)
    row33 = pygame.Rect(200, 360, 2, 20)
    row34 = pygame.Rect(240, 360, 2, 20)
    row35 = pygame.Rect(280, 360, 2, 20)
    ##
    row36 = pygame.Rect(140, 340, 2, 20)
    row37 = pygame.Rect(180, 340, 2, 20)
    row38 = pygame.Rect(220, 340, 2, 20)
    row39 = pygame.Rect(260, 340, 2, 20)
    row40 = pygame.Rect(298, 340, 2, 20)
    ##
    row41 = pygame.Rect(120, 320, 2, 20)
    row42 = pygame.Rect(160, 320, 2, 20)
    row43 = pygame.Rect(200, 320, 2, 20)
    row44 = pygame.Rect(240, 320, 2, 20)
    row45 = pygame.Rect(280, 320, 2, 20)
    ##
    row46 = pygame.Rect(140, 300, 2, 20)
    row47 = pygame.Rect(180, 300, 2, 20)
    row48 = pygame.Rect(220, 300, 2, 20)
    row49 = pygame.Rect(260, 300, 2, 20)
    row50 = pygame.Rect(298, 300, 2, 20)
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
    castle2 = pygame.Rect(1000, 295, 200, 200)
    tower1 = pygame.Rect(990, 280, 40, 40)
    tower2 = pygame.Rect(1050, 280, 40, 40)
    tower3 = pygame.Rect(1110, 280, 40, 40)
    tower4 = pygame.Rect(1170, 280, 40, 40)
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


def row_castle2(screen, line_color):
    row1 = pygame.Rect(1020, 480, 2, 15)
    row2 = pygame.Rect(1060, 480, 2, 15)
    row3 = pygame.Rect(1100, 480, 2, 15)
    row4 = pygame.Rect(1140, 480, 2, 15)
    row5 = pygame.Rect(1180, 480, 2, 15)
    ##
    row6 = pygame.Rect(1040, 460, 2, 20)
    row7 = pygame.Rect(1080, 460, 2, 20)
    row8 = pygame.Rect(1120, 460, 2, 20)
    row9 = pygame.Rect(1160, 460, 2, 20)
    row10 = pygame.Rect(1198, 460, 2, 20)
    ##
    row11 = pygame.Rect(1020, 440, 2, 20)
    row12 = pygame.Rect(1060, 440, 2, 20)
    row13 = pygame.Rect(1100, 440, 2, 20)
    row14 = pygame.Rect(1140, 440, 2, 20)
    row15 = pygame.Rect(1180, 440, 2, 20)
    ##
    row16 = pygame.Rect(1040, 420, 2, 20)
    row17 = pygame.Rect(1080, 420, 2, 20)
    row18 = pygame.Rect(1120, 420, 2, 20)
    row19 = pygame.Rect(1160, 420, 2, 20)
    row20 = pygame.Rect(1198, 420, 2, 20)
    ##
    row21 = pygame.Rect(1020, 400, 2, 20)
    row22 = pygame.Rect(1060, 400, 2, 20)
    row23 = pygame.Rect(1100, 400, 2, 20)
    row24 = pygame.Rect(1140, 400, 2, 20)
    row25 = pygame.Rect(1180, 400, 2, 20)
    ##
    row26 = pygame.Rect(1040, 380, 2, 20)
    row27 = pygame.Rect(1080, 380, 2, 20)
    row28 = pygame.Rect(1120, 380, 2, 20)
    row29 = pygame.Rect(1160, 380, 2, 20)
    row30 = pygame.Rect(1198, 380, 2, 20)
    ##
    row31 = pygame.Rect(1020, 360, 2, 20)
    row32 = pygame.Rect(1060, 360, 2, 20)
    row33 = pygame.Rect(1100, 360, 2, 20)
    row34 = pygame.Rect(1140, 360, 2, 20)
    row35 = pygame.Rect(1180, 360, 2, 20)
    ##
    row36 = pygame.Rect(1040, 340, 2, 20)
    row37 = pygame.Rect(1080, 340, 2, 20)
    row38 = pygame.Rect(1120, 340, 2, 20)
    row39 = pygame.Rect(1160, 340, 2, 20)
    row40 = pygame.Rect(1198, 340, 2, 20)
    ##
    row41 = pygame.Rect(1020, 320, 2, 20)
    row42 = pygame.Rect(1060, 320, 2, 20)
    row43 = pygame.Rect(1100, 320, 2, 20)
    row44 = pygame.Rect(1140, 320, 2, 20)
    row45 = pygame.Rect(1180, 320, 2, 20)
    ##
    row46 = pygame.Rect(1040, 300, 2, 20)
    row47 = pygame.Rect(1080, 300, 2, 20)
    row48 = pygame.Rect(1120, 300, 2, 20)
    row49 = pygame.Rect(1160, 300, 2, 20)
    row50 = pygame.Rect(1198, 300, 2, 20)
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
