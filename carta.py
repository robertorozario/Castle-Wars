import typing
import pygame

from enum import Enum

from constants import SCREEN_HEIGHT, SCREEN_WIDTH, CARD_HEIGHT, CARD_WIDTH

class AcaoCarta(Enum):
    TOWER = 1
    FIRE_ARCHER = 2
    KNIGHT = 3
    RECRUIT = 4
    BUILDER = 5
    TAVERN = 6
    MAGE = 7
    ADD_BRICK = 8
    ADD_WEAPON = 9
    MAGIC_DEFENSE = 10

class Carta(pygame.Rect):
    """
    Representação das cartas do jogo que realizam ações.

    Attributes
    ----------
    acao : AcaoCarta
        Tipo de ação que a carta deve efetuar.
    cristais : int
        Quantidade de cristais necessárias para jogar a carta.
    espadas : int
        Quantidade de espadas necessárias para jogar a carta.
    tijolos : int
        Quantidade de tijolos necessários para jogar a carta.
    """

    def __init__(self, acao: AcaoCarta, left: float, top: float, cristais: int, tijolos: int, espadas: int):
        super().__init__(left, top, CARD_WIDTH, CARD_HEIGHT)
        self._acao = acao
        self._posicao_inicial = (left, top)
        self._cristais = cristais
        self._espadas = espadas
        self._tijolos = tijolos

    @property
    def posicao_inicial(self) -> typing.Tuple:
        return self._posicao_inicial

    @property
    def espadas(self) -> int:
        return self._espadas

    @property
    def cristais(self) -> int:
        return self._cristais

    @property
    def tijolos(self) -> int:
        return self._tijolos

    @property
    def acao(self) -> AcaoCarta:
        return self._acao

    def draw(self, screen: pygame.Surface):
        '''Draws the card into the pygame screen.'''
        # TODO: allow dinamically choose the color from self._tipo
        pygame.draw.rect(screen, 125, self)

class CartaTower(Carta):
    """
    Carta que efetua a ação de aumentar 10 níveis do castelo do Jogador.
    """

    def __init__(self):
        super().__init__(acao=AcaoCarta.TOWER, left=0, top=0, cristais=0, tijolos=10, espadas=0)

class CartaFireArcher(Carta):
    """
    Carta que efetua a ação de diminuir 5 níveis do castelo do Jogador
    adversário.
    """

    def __init__(self):
        super().__init__(acao=AcaoCarta.FIRE_ARCHER, left=0, top=0, cristais=0, tijolos=0, espadas=3)

class CartaKnight(Carta):
    """
    Carta que efetua a ação de atacar o castelo do Jogador adversário causando
    12 de dano, ou seja, diminuindo 12 níveis.
    """
    
    def __init__(self):
        super().__init__(acao=AcaoCarta.KNIGHT, left=0, top=0, cristais=0, tijolos=0, espadas=10)

class CartaRecruit(Carta):
    """
    Carta que efetua a ação de acrescentar 1 soldado ao castelo do Jogador.
    """

    def __init__(self):
        super().__init__(acao=AcaoCarta.RECRUIT, left=0, top=0, cristais=0, espadas=8, tijolos=0)

class CartaBuilder(Carta):
    """
    Carta que efetua a ação de acrescentar 1 construtor ao castelo do Jogador.
    """
    
    def __init__(self):
        super().__init__(acao=AcaoCarta.BUILDER, left=0, top=0, cristais=0, espadas=0, tijolos=8)

class CartaTavern(Carta):
    """
    Carta que efetua a ação de acrescentar 15 níveis ao castelo do Jogador.
    """
    
    def __init__(self):
        super().__init__(acao=AcaoCarta.TAVERN, left=0, top=0, cristais=0, espadas=0, tijolos=12)

class CartaMage(Carta):
    """
    Carta que efetua a ação de acrescentar 1 mago ao castelo do Jogador.
    """
    
    def __init__(self):
        super().__init__(acao=AcaoCarta.MAGE, left=0, top=0, cristais=8, espadas=0, tijolos=0)

class CartaAddBrick(Carta):
    """
    Carta que efetua a ação de acrescentar 8 tijolos ao castelo do Jogador.
    """
    
    def __init__(self):
        super().__init__(acao=AcaoCarta.ADD_BRICK, left=0, top=0, cristais=5, espadas=0, tijolos=0)

class CartaAddWeapon(Carta):
    """
    Carta que efetua a ação de acrescentar 8 espadas ao castelo do Jogador.
    """

    def __init__(self):
        super().__init__(acao=AcaoCarta.ADD_WEAPON, left=0, top=0, cristais=5, espadas=0, tijolos=0)

class CartaMagicDefense(Carta):
    """
    Carta que efetua a ação de ativar o BUFF de escudo mágico no castelo do
    Jogador.
    """
    
    def __init__(self):
        super().__init__(acao=AcaoCarta.MAGIC_DEFENSE, left=0, top=0, cristais=15, espadas=0, tijolos=0)
