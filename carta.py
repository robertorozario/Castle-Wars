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

    def draw(self, screen: pygame.Surface):
        '''Draws the card into the pygame screen.'''
        # TODO: allow dinamically choose the color from self._tipo
        pygame.draw.rect(screen, 125, self)

class CartaTower(Carta):
    
    def __init__(self):
        super().__init__(acao=AcaoCarta.TOWER, left=0, top=0, cristais=0, tijolos=10, espadas=0)
        

class CartaFireArcher(Carta):
    
    def __init__(self):
        super().__init__(acao=AcaoCarta.FIRE_ARCHER, left=0, top=0, cristais=0, tijolos=0, espadas=3)

class CartaKnight(Carta):
    
    def __init__(self):
        super().__init__(acao=AcaoCarta.KNIGHT, left=0, top=0, cristais=0, tijolos=0, espadas=10)

class CartaRecruit(Carta):
    
    def __init__(self):
        super().__init__(acao=AcaoCarta.RECRUIT, left=0, top=0, cristais=0, espadas=8, tijolos=0)

class CartaBuilder(Carta):
    
    def __init__(self):
        super().__init__(acao=AcaoCarta.BUILDER, left=0, top=0, cristais=0, espadas=0, tijolos=8)

class CartaTavern(Carta):
    
    def __init__(self):
        super().__init__(acao=AcaoCarta.TAVERN, left=0, top=0, cristais=0, espadas=0, tijolos=12)

class CartaMage(Carta):
    
    def __init__(self):
        super().__init__(acao=AcaoCarta.MAGE, left=0, top=0, cristais=8, espadas=0, tijolos=0)

class CartaAddBrick(Carta):
    
    def __init__(self):
        super().__init__(acao=AcaoCarta.ADD_BRICK, left=0, top=0, cristais=5, espadas=0, tijolos=0)

class CartaAddWeapon(Carta):
    
    def __init__(self):
        super().__init__(acao=AcaoCarta.ADD_WEAPON, left=0, top=0, cristais=5, espadas=0, tijolos=0)

class CartaMagicDefense(Carta):
    
    def __init__(self):
        super().__init__(acao=AcaoCarta.MAGIC_DEFENSE, left=0, top=0, cristais=15, espadas=0, tijolos=0)
