import pygame

from cenario import Cenario

class JanelaDeJogo:

    def __init__(self, screen: pygame.Surface, cenario: Cenario):
        self.__screen = screen
        self.__cenario = cenario
        self.__loop = False

    def inicia_loop_jogo(self):
        pass

    def ouve_eventos(self):
        pass
