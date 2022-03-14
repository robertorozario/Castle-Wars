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
