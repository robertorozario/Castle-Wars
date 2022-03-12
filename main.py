import pygame

from janela_de_jogo import JanelaDeJogo
from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    jogo = JanelaDeJogo(screen=screen, cenario=None)
    jogo.inicia_loop_jogo()


if __name__ == "__main__":
    main()
