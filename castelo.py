import pygame

from constants import COLOR_BLUE, COLOR_RED

class Castelo:

    def __init__(self, color, tower_color, color_fill):
        self._nivel = 0
        self._nivel_do_muro = 0
        self._jogador = None
        self._construtores = 0
        self._magos = 0
        self._soldados = 0
        self._tijolos = 0
        self._espadas = 0
        self._cristais = 0
        self._tijolos_magicos_buff = False
        self._protecao_de_recursos_buff = False
        self._espadas_magicas_buff = False
        self._escudo_magico_buff = False
        self._color = color
        self._tower_color = tower_color
        self._color_fill = color_fill

    def draw(self, screen: pygame.Surface):
        # Desenha retângulo do castelo.
        left = 1000
        if self._color == COLOR_BLUE:
            left = 100
        pygame.draw.rect(
            screen,
            self._color_fill,
            pygame.Rect(left, 295, 200, 200),
        )

        # Desenha as linhas iniciais.
        for i in range(10):
            pygame.draw.rect(
                screen,
                self._color,
                pygame.Rect(left, 480-(20*i), 200, 2),
            )

        # Desenha os tijolos do castelo.
        odd_row_left = 1020
        even_row_left = 1040
        if self._color == COLOR_BLUE:
            odd_row_left = 120
            even_row_left = 140
        for i in range(5):
            pygame.draw.rect(
                screen,
                self._color,
                pygame.Rect(odd_row_left+(40*i), 480, 2, 15),
            )
            pygame.draw.rect(
                screen,
                self._color,
                pygame.Rect(even_row_left+(40*i)-(2 * (i // 4)), 460, 2, 20),
            )
            pygame.draw.rect(
                screen,
                self._color,
                pygame.Rect(odd_row_left+(40*i), 440, 2, 20),
            )
            pygame.draw.rect(
                screen,
                self._color,
                pygame.Rect(even_row_left+(40*i)-(2 * (i // 4)), 420, 2, 20),
            )
            pygame.draw.rect(
                screen,
                self._color,
                pygame.Rect(odd_row_left+(40*i), 400, 2, 20),
            )
            pygame.draw.rect(
                screen,
                self._color,
                pygame.Rect(even_row_left+(40*i)-(2 * (i // 4)), 380, 2, 20),
            )
            pygame.draw.rect(
                screen,
                self._color,
                pygame.Rect(odd_row_left+(40*i), 360, 2, 20),
            )
            pygame.draw.rect(
                screen,
                self._color,
                pygame.Rect(even_row_left+(40*i)-(2 * (i // 4)), 340, 2, 20),
            )
            pygame.draw.rect(
                screen,
                self._color,
                pygame.Rect(odd_row_left+(40*i), 320, 2, 20),
            )
            pygame.draw.rect(
                screen,
                self._color,
                pygame.Rect(even_row_left+(40*i)-(2 * (i // 4)), 300, 2, 20),
            )

        # Desenha as torres do castelo.
        tower_left = 990
        if self._color == COLOR_BLUE:
            tower_left = 90
        for i in range(4):
            pygame.draw.rect(
                screen,
                self._tower_color,
                pygame.Rect(tower_left+(60*i), 280, 40, 40),
            )
