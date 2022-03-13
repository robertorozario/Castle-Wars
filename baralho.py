from typing import List
from random import randint

from carta import (
    AcaoCarta,
    Carta,
    CartaAddBrick,
    CartaAddWeapon,
    CartaBuilder,
    CartaFireArcher,
    CartaKnight,
    CartaMage,
    CartaMagicDefense,
    CartaRecruit,
    CartaTavern,
    CartaTower,
)

TAMANHO_MAXIMO = 280


class Baralho:
    """
    Uma representação de um baralho de cartas para o CastleWars.

    Attributes
    ----------
    cartas : []Carta
        As cartas que o baralho possui.
    nome : str
        O nome do baralho para mostrar ao Jogador.
    """

    def __init__(self, nome: str, cartas: List[Carta] = []):
        self.__cartas: List[Carta] = cartas
        self.__nome = nome

    @property
    def nome(self) -> str:
        return self.__nome

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
        if acao is AcaoCarta.TOWER:
            cartas_a_adicionar = [CartaTower() for i in range(copias)]
        elif acao is AcaoCarta.FIRE_ARCHER:
            cartas_a_adicionar = [CartaFireArcher() for i in range(copias)]
        elif acao is AcaoCarta.KNIGHT:
            cartas_a_adicionar = [CartaKnight() for i in range(copias)]
        elif acao is AcaoCarta.RECRUIT:
            cartas_a_adicionar = [CartaRecruit() for i in range(copias)]
        elif acao is AcaoCarta.BUILDER:
            cartas_a_adicionar = [CartaBuilder() for i in range(copias)]
        elif acao is AcaoCarta.TAVERN:
            cartas_a_adicionar = [CartaTavern() for i in range(copias)]
        elif acao is AcaoCarta.MAGE:
            cartas_a_adicionar = [CartaMage() for i in range(copias)]
        elif acao is AcaoCarta.ADD_BRICK:
            cartas_a_adicionar = [CartaAddBrick() for i in range(copias)]
        elif acao is AcaoCarta.ADD_WEAPON:
            cartas_a_adicionar = [CartaAddWeapon() for i in range(copias)]
        elif acao is AcaoCarta.MAGIC_DEFENSE:
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

    def copia(self):
        """Faz uma cópia exato do baralho no estado atual.

        Returns
        -------
        Baralho
            uma cópia exata do Baralho atual.
        """
        return Baralho(self.__nome, cartas=self.__cartas)

    def obtem_carta_aleatoria(self) -> Carta:
        indice_aleatorio = randint(0, len(self.__cartas)-1)
        carta = self.__cartas.pop(indice_aleatorio)
        return carta
