from typing import List

from carta import Carta
from jogador import Jogador

class Baralho:
    
    def __init__(self, cartas: List[Carta] = []):
        self.__cartas: List[Carta] = cartas
    
    def adiciona_carta(self, tipo: str, copias: int, jogador: Jogador):
        pass

    def inicializa_baralho(self):
        pass

    def baralho_tem_espaco(self):
        pass

    def numero_de_cartas_por_tipo(self, tipo: str) -> int:
        pass

    def copia(self) -> Baralho:
        pass
