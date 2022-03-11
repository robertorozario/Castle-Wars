from typing import List

from carta import *
from jogador import Jogador

TAMANHO_MAXIMO = 280

class Baralho:
    """
    Uma representação de um baralho de cartas para o CastleWars.

    Attributes
    ----------
    cartas : []Carta
        As cartas que o baralho possui.
    """
    
    def __init__(self, cartas: List[Carta] = []):
        self.__cartas: List[Carta] = cartas
    
    def adiciona_carta(self, acao: AcaoCarta, copias: int):
        """Adiciona cartas ao baralho.

        Parameters
        ----------
        acao : AcaoCarta
            Tipo de ação da carta para adicionar.
        copias : int
            Quantidade de cópias da carta para adicionar.
        """
        cartas_a_adicionar = []
        if carta.acao is AcaoCarta.TOWER:
            cartas_a_adicionar = [CartaTower() for i in range(copias)]
        elif carta.acao is FIRE_ARCHER:
            cartas_a_adicionar = [CartaFireArcher() for i in range(copias)]
        elif carta.acao is KNIGHT:
            cartas_a_adicionar = [CartaKnight() for i in range(copias)]
        elif carta.acao is RECRUIT:
            cartas_a_adicionar = [CartaRecruit() for i in range(copias)]
        elif carta.acao is BUILDER:
            cartas_a_adicionar = [CartaBuilder() for i in range(copias)]
        elif carta.acao is TAVERN:
            cartas_a_adicionar = [CartaTavern() for i in range(copias)]
        elif carta.acao is MAGE:
            cartas_a_adicionar = [CartaMage() for i in range(copias)]
        elif carta.acao is ADD_BRICK:
            cartas_a_adicionar = [CartaAddBrick() for i in range(copias)]
        elif carta.acao is ADD_WEAPON:
            cartas_a_adicionar = [CartaAddWeapon() for i in range(copias)]
        elif carta.acao is MAGIC_DEFENSE:
            cartas_a_adicionar = [CartaMagicDefense() for i in range(copias)]
        
        for carta in cartas_a_adicionar:
            self.__cartas.append(carta)

    def baralho_tem_espaco(self) -> bool:
        """Verifica se o baralho possui espaço, ou seja, len(cartas) <= 280.

        Returns
        -------
        bool
            indicação se o baralho possui espaço.
        """
        return len(self.__cartas) <= 280

    def numero_de_cartas_por_acao(self, acao: AcaoCarta) -> int:
        """Obtem o número de cartas pelo tipo de ação existentes atualmente no
        baralho.

        Parameters
        ----------
        acao : AcaoCarta
            Tipo de acão da carta.
        
        Returns
        -------
        int
            quantidade de cartas desta ação no baralho.
        """
        cont = 0
        for carta in self.__cartas:
            if carta.acao is acao:
                cont += 1
        return cont

    def copia(self) -> Baralho:
        """Faz uma cópia exato do baralho no estado atual.

        Returns
        -------
        Baralho
            uma cópia exata do Baralho atual.
        """
        return Baralho(cartas=self.__cartas)
