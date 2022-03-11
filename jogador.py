from typing import List

from baralho import Baralho
from carta import Carta

class Jogador:

    def __init__(self):
        self.__vencedor: bool = False
        self.__baralho: Baralho = None
        self.__mao: List[Carta] = []
        self.__em_turno: bool = False
        self.__pronto: bool = False

    @property
    def em_turno(self) -> bool:
        return self.__em_turno

    @em_turno.setter
    def em_turno(self, em_turno: bool):
        self.__em_turno = em_turno

    @property
    def vencedor(self) -> bool:
        return self.__vencedor
    
    @vencedor.setter
    def vencedor(self, vencedor: bool):
        self.__vencedor = vencedor
    
    @property
    def baralho(self) -> Baralho:
        return self.__baralho

    @baralho.setter
    def baralho(self, baralho: Baralho):
        self.__baralho = baralho

    @property
    def mao(self) -> List[Carta]:
        return self.__mao

    @mao.setter
    def mao(self, mao: List[Carta]):
        self.__mao = mao
    
    @property
    def pronto(self) -> bool:
        return self.__pronto
    
    @pronto.setter
    def pronto(self, pronto: bool):
        self.__pronto = pronto

    def descartar(self, indice: int):
        pass

    def obtem_carta_da_mao(self, indice: int) -> Carta:
        pass

    def descartou_max_cartas(self) -> bool:
        pass

    def jogar_carta(self, indice: int):
        pass
