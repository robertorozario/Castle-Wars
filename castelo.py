import pygame

from constants import (
    COLOR_BLUE,
    COLOR_FILL_BLUE,
    COLOR_BLUE_TOWER,
    COLOR_FILL_RED,
    COLOR_RED,
    COLOR_RED_TOWER,
    SCREEN_WIDTH,
)
from jogador import Jogador
from carta import Carta


class Castelo:

    def __init__(self, jogador: Jogador, color, tower_color, color_fill):
        self.__nivel = 0
        self.__jogador: Jogador = jogador
        self.__construtores = 0
        self.__magos = 0
        self.__soldados = 0
        self.__tijolos = 0
        self.__espadas = 0
        self.__cristais = 0
        self.__escudo_magico_buff = False
        self.__color = color
        self.__tower_color = tower_color
        self.__color_fill = color_fill

    @staticmethod
    def vermelho(cls, jogador: Jogador):
        """Cria um castelo da cor vermelha recebendo o Jogador dono dele.

        Parameters
        ----------
        jogador : Jogador
            O jogador dono do castelo.

        Returns
        -------
        Castelo
            o castelo vermelho criado.
        """

        return cls(
            jogador=jogador,
            color=COLOR_RED,
            color_fill=COLOR_FILL_RED,
            tower_color=COLOR_RED_TOWER)

    @staticmethod
    def azul(cls, jogador: Jogador):
        """Cria um castelo da cor azul recebendo o Jogador dono dele.

        Parameters
        ----------
        jogador : Jogador
            O jogador dono do castelo.

        Returns
        -------
        Castelo
            o castelo azul criado.
        """

        return cls(
            jogador=jogador,
            color=COLOR_BLUE,
            color_fill=COLOR_FILL_BLUE,
            tower_color=COLOR_BLUE_TOWER)

    @property
    def nivel(self) -> int:
        return self.__nivel

    @nivel.setter
    def nivel(self, nivel: int):
        self.__nivel = nivel

    @property
    def jogador(self) -> Jogador:
        return self.__jogador

    @property
    def construtores(self) -> int:
        return self.__construtores

    @construtores.setter
    def construtores(self, construtores: int):
        self.__construtores = construtores

    @property
    def magos(self) -> int:
        return self.__magos

    @magos.setter
    def magos(self, magos: int):
        self.__magos = magos

    @property
    def soldados(self) -> int:
        return self.__soldados

    @soldados.setter
    def soldados(self, soldados: int):
        self.__soldados = soldados

    @property
    def tijolos(self) -> int:
        return self.__tijolos

    @tijolos.setter
    def tijolos(self, tijolos: int):
        self.__tijolos = tijolos

    @property
    def espadas(self) -> int:
        return self.__espadas

    @espadas.setter
    def espadas(self, espadas: int):
        self.__espadas = espadas

    @property
    def cristais(self) -> int:
        return self.__cristais

    @cristais.setter
    def cristais(self, cristais: int):
        self.__cristais = cristais

    @property
    def escudo_magico_buff(self) -> bool:
        return self.__escudo_magico_buff

    @escudo_magico_buff.setter
    def escudo_magico_buff(self, valor: bool):
        self.__escudo_magico_buff = valor

    def possui_recurso_pra_carta(self, carta: Carta) -> bool:
        """Verifica se o Castelo possui recursos para jogar a carta.

        Parameters
        ----------
        carta : Carta
            A carta para verificar quantidade de recursos do Castelo.

        Returns
        -------
        bool
            se o Castelo possui recursos para jogar a carta.
        """

        possui_cristais = self.__cristais >= carta.cristais
        possui_tijolos = self.__tijolos >= carta.tijolos
        possui_espadas = self.__espadas >= carta.espadas
        if possui_cristais and possui_tijolos and possui_espadas:
            self.__cristais -= carta.cristais
            self.__tijolos -= carta.tijolos
            self.__espadas -= carta.espadas
            return True
        else:
            return False

    def aplica_configuracao_inicial(self):
        """Aplica a configuração inicial, ou seja, de início de jogo ao Castelo.
        """

        self.__nivel = 30
        self.__magos = 2
        self.__construtores = 2
        self.__soldados = 2
        self.__cristais = 5
        self.__espadas = 5
        self.__tijolos = 5

    def adicionar_recursos(self):
        """Adiciona os recursos de troca de turno ao Castelo."""

        self.__tijolos += self.__construtores
        self.__cristais += self.__magos
        self.__espadas += self.__soldados

    def draw(self, screen: pygame.Surface):
        # Desenha retângulo do castelo.
        left = 900
        if self.__color == COLOR_BLUE:
            left = 200
        pygame.draw.rect(
            screen,
            self.__color_fill,
            pygame.Rect(left, 295, 200, 200),
        )

        # Desenha as linhas iniciais.
        for i in range(10):
            pygame.draw.rect(
                screen,
                self.__color,
                pygame.Rect(left, 480-(20*i), 200, 2),
            )

        # Desenha os tijolos do castelo.
        odd_row_left = 920
        even_row_left = 940
        if self.__color == COLOR_BLUE:
            odd_row_left = 220
            even_row_left = 240
        for i in range(5):
            pygame.draw.rect(
                screen,
                self.__color,
                pygame.Rect(odd_row_left+(40*i), 480, 2, 15),
            )
            pygame.draw.rect(
                screen,
                self.__color,
                pygame.Rect(even_row_left+(40*i)-(2 * (i // 4)), 460, 2, 20),
            )
            pygame.draw.rect(
                screen,
                self.__color,
                pygame.Rect(odd_row_left+(40*i), 440, 2, 20),
            )
            pygame.draw.rect(
                screen,
                self.__color,
                pygame.Rect(even_row_left+(40*i)-(2 * (i // 4)), 420, 2, 20),
            )
            pygame.draw.rect(
                screen,
                self.__color,
                pygame.Rect(odd_row_left+(40*i), 400, 2, 20),
            )
            pygame.draw.rect(
                screen,
                self.__color,
                pygame.Rect(even_row_left+(40*i)-(2 * (i // 4)), 380, 2, 20),
            )
            pygame.draw.rect(
                screen,
                self.__color,
                pygame.Rect(odd_row_left+(40*i), 360, 2, 20),
            )
            pygame.draw.rect(
                screen,
                self.__color,
                pygame.Rect(even_row_left+(40*i)-(2 * (i // 4)), 340, 2, 20),
            )
            pygame.draw.rect(
                screen,
                self.__color,
                pygame.Rect(odd_row_left+(40*i), 320, 2, 20),
            )
            pygame.draw.rect(
                screen,
                self.__color,
                pygame.Rect(even_row_left+(40*i)-(2 * (i // 4)), 300, 2, 20),
            )

        # Desenha as torres do castelo.
        tower_left = 890
        if self.__color == COLOR_BLUE:
            tower_left = 190
        for i in range(4):
            pygame.draw.rect(
                screen,
                self.__tower_color,
                pygame.Rect(tower_left+(60*i), 280, 40, 40),
            )

    def draw_info(self, screen: pygame.Surface):
        info = {
            'Nível': str(self.__nivel),
            'Construtores': str(self.__construtores),
            'Magos': str(self.__magos),
            'Soldados': str(self.__soldados),
            'Tijolos': str(self.__tijolos),
            'Espadas': str(self.__espadas),
            'Cristais': str(self.__cristais),
            'Escudo Mágico': 'ON' if self.__escudo_magico_buff else 'OFF',
        }

        font = pygame.font.SysFont(None, 20)
        textos = []
        for key, val in info.items():
            texto = font.render(key + ': ' + val, False, (0, 0, 0))
            textos.append(texto)

        maior_width_textos = 0
        for texto in textos:
            if texto.get_width() > maior_width_textos:
                maior_width_textos = texto.get_width()

        left = 25
        if self.__color == COLOR_RED:
            left = SCREEN_WIDTH - maior_width_textos - 32

        top = 350
        for i in range(len(textos)):
            screen.blit(textos[i], (left, top + (i*16)))

    def reset(self):
        """Reinicia os atributos do Castelo para o mesmo estado de
        instanciação.
        """
        self.__nivel = 0
        self.__construtores = 0
        self.__magos = 0
        self.__soldados = 0
        self.__tijolos = 0
        self.__espadas = 0
        self.__cristais = 0
        self.__escudo_magico_buff = False
