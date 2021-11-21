import typing
import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH, CARD_HEIGHT, CARD_WIDTH


class Carta(pygame.Rect):

    def __init__(self, tipo: str, valor: int, acao: str, left: float, top: float):
        super().__init__(left, top, CARD_WIDTH, CARD_HEIGHT)
        self._tipo = tipo
        self._valor = valor
        self._acao = acao
        self._posicao_inicial = (left, top)

    @property
    def posicao_inicial(self) -> typing.Tuple:
        return self._posicao_inicial

    def draw(self, screen: pygame.Surface):
        '''Draws the card into the pygame screen.'''
        # TODO: allow dinamically choose the color from self._tipo
        pygame.draw.rect(screen, 125, self)
