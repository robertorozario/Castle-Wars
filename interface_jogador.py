import pygame

from jogador import Jogador
from cenario import Cenario


class InterfaceJogador:
    """
    InterfaceJogador representa a interface do ator Jogador com o jogo.
    """

    def __init__(
        self,
        screen: pygame.Surface,
        jogador_azul: Jogador,
        jogador_vermelho: Jogador,
        cenario: Cenario,
    ):
        self.__screen = screen
        self.__jogador_vermelho = jogador_vermelho
        self.__jogador_azul = jogador_azul
        self.__cenario = cenario

    def jogar_carta(self, indice: int):
        if self.__jogador_azul.em_turno:
            self.__jogador_azul.jogar_carta(indice)
        else:
            self.__jogador_vermelho.jogar_carta(indice)

    def descartar_carta(self, indice: int):
        if self.__jogador_azul.em_turno:
            self.__jogador_azul.descarta_carta(indice)
            if self.__jogador_azul.descartou_max_cartas():
                self.__cenario.passa_turno_atual_jogador()
        else:
            self.__jogador_vermelho.descarta_carta(indice)
            if self.__jogador_vermelho.descartou_max_cartas():
                self.__cenario.passa_turno_atual_jogador()

    def iniciar_jogo(self):
        self.__cenario.iniciar_jogo()

    def passar_turno(self):
        self.__cenario.passa_turno_atual_jogador()

    def seleciona_baralho(self, indice: int, lado: str):
        baralho = self.__cenario.baralhos_padrao[indice]
        baralho_copia = baralho.copia()
        if lado == 'azul':
            self.__jogador_azul.baralho = baralho_copia
        else:
            self.__jogador_vermelho.baralho = baralho_copia
