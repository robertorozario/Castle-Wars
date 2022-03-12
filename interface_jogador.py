import pygame

from jogador import Jogador
from cenario import Cenario


class InterfaceJogador:
    """
    InterfaceJogador representa a interface do ator Jogador com o jogo.
    """

    def __init__(
            self, screen: pygame.Surface, jogador: Jogador, cenario: Cenario):
        self.__screen = screen
        self.__jogador = jogador
        self.__cenario = cenario

    def jogar_carta(self, indice: int):
        self.__jogador.jogar_carta(indice)

    def descartar_carta(self, indice: int):
        self.__jogador.descarta_carta(indice)
        if self.__jogador.descartou_max_cartas():
            self.__cenario.passa_turno_atual_jogador()

    def iniciar_jogo(self):
        self.__cenario.iniciar_jogo()

    def passar_turno(self):
        self.__cenario.passa_turno_atual_jogador()

    def seleciona_baralho(self, indice: int):
        baralho = self.__cenario.baralhos_padrao[indice]
        baralho_copia = baralho.copia()
        self.__jogador.baralho = baralho_copia
