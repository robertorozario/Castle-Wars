import pygame

from typing import List

from baralho import Baralho
from castelo import Castelo
from jogador import Jogador

class Cenario:

    def __init__(self):
        self.__castelo_azul = Castelo('azul', 'azul', 'azul')
        self.__castelo_vermelho = Castelo('vermelho', 'vermelho', 'vermelho')
        self.__jogador_vermelho = Jogador()
        self.__jogador_azul = Jogador()
        self.__partida_em_andamento = False
        self.__baralhos_padrao: List[Baralho] = []
        self.__jogador_em_turno: Jogador = None
        self.__jogador_em_turno_pronto: bool = False

    @property
    def castelo_azul(self) -> Castelo:
        return self.__castelo_azul
    
    @property
    def castelo_vermelho(self) -> Castelo:
        return self.__castelo_vermelho
    
    @property
    def jogador_vermelho(self) -> Jogador:
        return self.__jogador_vermelho

    @property
    def jogador_azul(self) -> Jogador:
        return self.__jogador_azul

    @property
    def partida_em_andamento(self) -> bool:
        return self.__partida_em_andamento
    
    @partida_em_andamento.setter
    def partida_em_andamento(self, partida_em_andamento: bool):
        self.__partida_em_andamento = partida_em_andamento

    @property
    def baralhos_padrao(self) -> List[Baralho]:
        return self.__baralhos_padrao
    
    @property
    def jogador_em_turno(self) -> Jogador:
        return self.__jogador_em_turno
    
    @jogador_em_turno.setter
    def jogador_em_turno(self, jogador_em_turno: Jogador):
        self.__jogador_em_turno = jogador_em_turno
    
    @property
    def jogador_em_turno_pronto(self) -> bool:
        return self.__jogador_em_turno_pronto
    
    @jogador_em_turno_pronto.setter
    def jogador_em_turno_pronto(self, jogador_em_turno_pronto: bool):
        return self.__jogador_em_turno_pronto

    def obtem_castelo_jogador(self, jogador: Jogador) -> Castelo:
        pass

    def efetua_acao_da_carta(self, carta: Carta, castelo_jogador: Castelo):
        pass

    def atualiza_estado_jogo(self, acao: str, castelo_jogador: Castelo):
        pass

    def passar_turno(self):
        pass

    def passar_turno(self, jogador: Jogador):
        pass

    def passa_turno_atual_jogador(self):
        pass

    def anuncia_vencedor(self):
        pass

    def finaliza_partida(self):
        pass

    def iniciar_jogo(self):
        pass

    def jogadores_estao_prontos(self) -> bool:
        pass

    def salva_baralho(self, jogador: Jogador):
        pass

    def avalia_encerramento_partida(self):
        pass

    def notifica_vencedor(self):
        pass

    def draw(self, surface: pygame.Surface):
        pass

    def draw_initial_screen(self, surface: pygame.Surface):
        pass
