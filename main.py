import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from cenario import Cenario
from janela_de_jogo import JanelaDeJogo


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    jogo = JanelaDeJogo(screen=screen, cenario=Cenario())
    jogo.inicia_loop_jogo()


if __name__ == "__main__":
    main()
