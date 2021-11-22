import pygame
import sys
import typing

from pygame.constants import SYSTEM_CURSOR_WAITARROW
from pygame.draw import line
from constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    COLOR_BLUE,
    COLOR_RED,
    COLOR_BLUE_TOWER,
    COLOR_RED_TOWER,
    COLOR_FILL_BLUE,
    COLOR_FILL_RED,
)
from carta import Carta
from castelo import Castelo


# Global variables
BG_COLOR = (173, 203, 222)
ACCENT_COLOR = (15, 97, 20)
TEXT_COLOR = (38, 40, 41)
FLOOR_COLOR = (19, 161, 36)

def main():
    # General Setup
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()
    clock = pygame.time.Clock()

    # Setting up the main window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Castle Wars')

    deck = pygame.Rect(0, 535, SCREEN_WIDTH, SCREEN_HEIGHT / 4)
    floor = pygame.Rect(0, 495, SCREEN_WIDTH, 40)

    # Fonte de texto
    font = pygame.font.Font("freesansbold.ttf", 20)

    cartas = cria_cartas_usuario()
    carta_selecionada: Carta = None

    castelo_azul = Castelo(COLOR_BLUE, COLOR_BLUE_TOWER, COLOR_FILL_BLUE)
    castelo_vermelho = Castelo(COLOR_RED, COLOR_RED_TOWER, COLOR_FILL_RED)
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
                        carta_selecionada.x = event.pos[0]
                        carta_selecionada.y = event.pos[1]

        # Background Stuff
        screen.fill(BG_COLOR)

        # Desenha zonas de arraste das cartas.
        desenha_zona_de_jogo(screen, font)
        desenha_zona_de_descarte(screen, font)

        # Desenha espaço de deck e chão.
        pygame.draw.rect(screen, ACCENT_COLOR, deck)
        pygame.draw.rect(screen, FLOOR_COLOR, floor)

        # Desenha botão que irá direcionar para criação do deck.
        texto = font.render('Criar Deck' , False , TEXT_COLOR)
        rect_texto = texto.get_rect(center=(SCREEN_WIDTH/2, 64))
        cria_deck_btn = pygame.Rect(
            SCREEN_WIDTH/2-texto.get_width(),
            32,
            texto.get_width()*2,
            64,
        )

        # Highlight the create deck button if mouse hover over it.
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if SCREEN_WIDTH/2-texto.get_width() <= mouse_x <= SCREEN_WIDTH/2+texto.get_width() and 32 <= mouse_y <= 96:
            pygame.draw.rect(screen, (105, 105, 105), cria_deck_btn)
        else:
            pygame.draw.rect(screen, (211, 211, 211),cria_deck_btn)
        screen.blit(texto, rect_texto)

        # Desenha castelos na tela.
        castelo_azul.draw(screen)
        castelo_azul.draw_info(screen)
        castelo_vermelho.draw(screen)
        castelo_vermelho.draw_info(screen)

        # Desenha as cartas da mão do usuário.
        for carta in cartas:
            carta.draw(screen)

        # Rendering
        pygame.display.flip()
        clock.tick(60)


def cria_cartas_usuario() -> typing.List[Carta]:
    initial_left = 50
    TOP = 545
    return [Carta('', 0, '', (i * 150) + initial_left, TOP) for i in range(8)]


def desenha_zona_de_descarte(screen: pygame.Surface, font: pygame.font.Font):
    texto = font.render("Zona de Descarte", False, TEXT_COLOR)
    screen.blit(texto, (SCREEN_WIDTH - 480, 100))


def desenha_zona_de_jogo(screen: pygame.Surface, font: pygame.font.Font):
    texto = font.render("Zona de Jogo", False, TEXT_COLOR)
    screen.blit(texto, (350, 100))


if __name__ == "__main__":
    main()
