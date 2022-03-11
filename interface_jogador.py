import pygame

from jogador import Jogador
from cenario import Cenario

class InterfaceJogador:
    
    def __init__(self, screen: pygame.Surface, jogador: Jogador, cenario: Cenario):
        self.__screen = screen
        self.__jogador = jogador
        self.__cenario = cenario

    def descartar_carta(indice: int):
        pass

    def iniciar_jogo(self):
        pass

    def passar_turno(self):
        pass

    def adiciona_carta(self, tipo: str, copias: int):
        pass

    def remove_carta(self, tipo: str, copias: int):
        pass

    def seleciona_baralho(self, indice: int):
        pass