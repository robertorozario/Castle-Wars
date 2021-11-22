import pygame

from constants import COLOR_BLUE, COLOR_RED, SCREEN_WIDTH

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
        left = 900
        if self._color == COLOR_BLUE:
            left = 200
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
        odd_row_left = 920
        even_row_left = 940
        if self._color == COLOR_BLUE:
            odd_row_left = 220
            even_row_left = 240
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
        tower_left = 890
        if self._color == COLOR_BLUE:
            tower_left = 190
        for i in range(4):
            pygame.draw.rect(
                screen,
                self._tower_color,
                pygame.Rect(tower_left+(60*i), 280, 40, 40),
            )

    def draw_info(self, screen: pygame.Surface):
        info = {
            'Nível': str(self._nivel),
            'Nível Muro': str(self._nivel_do_muro),
            'Construtores': str(self._construtores),
            'Magos': str(self._magos),
            'Soldados': str(self._soldados),
            'Tijolos': str(self._tijolos),
            'Espadas': str(self._espadas),
            'Cristais': str(self._cristais),
            'Tijolos Mágicos': 'ON' if self._escudo_magico_buff else 'OFF',
            'Proteção de Recursos': 'ON' if self._protecao_de_recursos_buff else 'OFF',
            'Espadas Mágicas': 'ON' if self._espadas_magicas_buff else 'OFF',
            'Escudo Mágico': 'ON' if self._escudo_magico_buff else 'OFF',
        }
        
        font = pygame.font.Font("freesansbold.ttf", 12)
        textos = []
        for key, val in info.items():
            texto = font.render(key + ': ' + val, False, (0, 0, 0))
            textos.append(texto)

        maior_width_textos = 0
        for texto in textos:
            if texto.get_width() > maior_width_textos:
                maior_width_textos = texto.get_width()
        
        left = 32
        if self._color == COLOR_RED:
            left = SCREEN_WIDTH - maior_width_textos - 32
        
        top = 32
        for i in range(len(textos)):
            screen.blit(textos[i], (left, top + (i*16)))
