import pygame
import typing
import sys

from enum import Enum
from carta import Carta, AcaoCarta
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, FONTE_NAME
from cenario import Cenario

BG_COLOR = (173, 203, 222)
ACCENT_COLOR = (15, 97, 20)
TEXT_COLOR = (38, 40, 41)
FLOOR_COLOR = (19, 161, 36)


class Tela(Enum):
    INICIAL = 1
    JOGO = 2
    TROCA_DE_TURNO = 3


class JanelaDeJogo:
    """
    Define a interação da tela de jogo do CastleWars.
    """

    def __init__(self, screen: pygame.Surface, cenario: Cenario):
        self.__screen = screen
        self.__cenario = cenario
        self.__loop = False
        self.__carta_selecionada: Carta = None
        self.__pass_turn = False
        self.__tela: Tela = Tela.INICIAL

    def inicia_loop_jogo(self):
        self.__loop = True

        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.init()
        clock = pygame.time.Clock()

        pygame.display.set_caption("Castle Wars")

        while self.__loop:

            if self.__tela is Tela.INICIAL:
                self._desenha_tela_inicial()
            elif self.__tela is Tela.JOGO:
                self._desenha_tela_jogo()
            elif self.__tela is Tela.TROCA_DE_TURNO:
                self._desenha_tela_troca_de_turno()

            # Rendering
            pygame.display.flip()
            clock.tick(60)

    def _desenha_tela_inicial(self):
        screen = self.__screen

        font = pygame.font.Font(FONTE_NAME, 30)

        texto = font.render("Iniciar Jogo", False, TEXT_COLOR)
        rect_texto = texto.get_rect(
            center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        )
        btn = pygame.Rect(
            SCREEN_WIDTH / 2 - texto.get_width(),
            (SCREEN_HEIGHT / 2) - 32,
            texto.get_width() * 2,
            64,
        )

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if (
            SCREEN_WIDTH / 2 - texto.get_width()
            <= mouse_x
            <= SCREEN_WIDTH / 2 + texto.get_width()
            and (SCREEN_HEIGHT / 2) - 32 <= mouse_y <= (SCREEN_WIDTH / 2) + 32
        ):
            pygame.draw.rect(screen, (105, 105, 105), btn, border_radius=10)
        else:
            pygame.draw.rect(screen, (211, 211, 211), btn, border_radius=10)

        self.ouve_eventos_tela_inicial(comprimento_texto=texto.get_width())

        screen.blit(texto, rect_texto)

    def _desenha_tela_troca_de_turno(self):
        screen = self.__screen

        font = pygame.font.Font(FONTE_NAME, 20)

        screen.fill(BG_COLOR)
        pts_text = font.render(
            "Passe a Vez, Clique Para Continuar", FONTE_NAME, TEXT_COLOR
        )
        rect_pts_text = pts_text.get_rect(
            center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        )
        screen.blit(pts_text, rect_pts_text)
        self.ouve_eventos([])

    def _desenha_tela_jogo(self):
        # Setting up the main window
        screen = self.__screen

        deck = pygame.Rect(0, 535, SCREEN_WIDTH, SCREEN_HEIGHT / 4)
        floor = pygame.Rect(0, 495, SCREEN_WIDTH, 40)

        # Fonte de texto
        font = pygame.font.Font(FONTE_NAME, 20)

        cartas = cria_cartas_usuario()

        castelo_azul = self.__cenario.castelo_azul
        castelo_vermelho = self.__cenario.castelo_vermelho

        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.ouve_eventos(cartas)

        # Background Stuff
        screen.fill(BG_COLOR)

        # Desenha zonas de arraste das cartas.
        desenha_zona_de_jogo(screen, font)
        desenha_zona_de_descarte(screen, font)

        # Desenha espaço de deck e chão.
        pygame.draw.rect(screen, ACCENT_COLOR, deck)
        pygame.draw.rect(screen, FLOOR_COLOR, floor)

        passa_turno_texto = font.render("Passar Turno", False, TEXT_COLOR)
        rect_passa_turno_texto = passa_turno_texto.get_rect(
            center=(SCREEN_WIDTH / 2, 58)
        )
        passar_turno_btn = pygame.Rect(
            SCREEN_WIDTH / 2 - (passa_turno_texto.get_width() / 1.65),
            30,
            passa_turno_texto.get_width() * 1.2,
            60,
        )

        # Highlight do botão de passar turno quando o mouse estiver sobre
        # ele.
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if (
            (SCREEN_WIDTH / 2) - (passa_turno_texto.get_width() / 1.65)
            <= mouse_x
            <= SCREEN_WIDTH / 2 + passa_turno_texto.get_width()*1.2
            and 30 <= mouse_y <= 30 + 60
        ):

            pygame.draw.rect(screen, (152, 173, 139), passar_turno_btn, border_radius=10)
        else:
            pygame.draw.rect(screen, (211, 211, 211), passar_turno_btn, border_radius=10)
        screen.blit(passa_turno_texto, rect_passa_turno_texto)

        # Desenha castelos na tela.
        castelo_azul.draw(screen)
        castelo_azul.draw_info(screen)
        castelo_vermelho.draw(screen)
        castelo_vermelho.draw_info(screen)

        # Desenha as cartas da mão do usuário.
        for carta in cartas:
            carta.draw(screen)

    def ouve_eventos_tela_inicial(self, comprimento_texto: int):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (
                    SCREEN_WIDTH / 2 - comprimento_texto
                    <= mouse_x
                    <= SCREEN_WIDTH / 2 + comprimento_texto
                    and (SCREEN_HEIGHT / 2) - 32
                    <= mouse_y
                    <= (SCREEN_HEIGHT / 2) + 32
                ):
                    self.__tela = Tela.JOGO

    def ouve_eventos(self, cartas: typing.List[Carta]):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Se o mouse está clicado seleciona a carta que colidiu o
                # evento.
                for carta in cartas:
                    if carta.collidepoint(event.pos):
                        self.__carta_selecionada = carta
            elif event.type == pygame.MOUSEBUTTONUP:
                # Botão do mouse foi solto desceleciona a carta e deixa-a
                # parada.
                if self.__carta_selecionada is not None:
                    """
                    Rects não tem função pra deletar pelo que eu achei,
                    então só move cartas pra fora da tela e as condições
                    para as cartas serem deletadas não leva em consideração
                    em qual das zonas ela se encontra, apenas se está acima
                    da área da mão, elaborar isso na versão final
                    """
                    if self.__carta_selecionada.y < (
                        SCREEN_HEIGHT - ((SCREEN_HEIGHT / 4) + 40)
                    ):
                        self.__carta_selecionada.x = -200
                        self.__carta_selecionada.y = 0
                        self.__carta_selecionada = None
                    else:
                        carta_x = self.__carta_selecionada.posicao_inicial[0]
                        carta_y = self.__carta_selecionada.posicao_inicial[1]
                        self.__carta_selecionada.x = carta_x
                        self.__carta_selecionada.y = carta_y
                        self.__carta_selecionada = None
                elif (
                    ((SCREEN_WIDTH / 2) - (103/1.65)) <= mouse_x
                    and mouse_x <= ((SCREEN_WIDTH / 2) + (103*1.2))
                    and 30 <= mouse_y <= 30 + 60
                ):
                    self.__tela = Tela.TROCA_DE_TURNO
                else:
                    self.__tela = Tela.JOGO
            elif event.type == pygame.MOUSEMOTION:
                # No movimento do mouse "arrasta" a carta junto.
                if self.__carta_selecionada is not None:
                    botao_esquerdo_pressionado = event.buttons[0]
                    if botao_esquerdo_pressionado:
                        self.__carta_selecionada.x = event.pos[0]
                        self.__carta_selecionada.y = event.pos[1]


def cria_cartas_usuario() -> typing.List[Carta]:
    initial_left = 50
    TOP = 545
    return [
        Carta(
            acao=AcaoCarta,
            left=(i * 150) + initial_left,
            top=TOP,
            espadas=0,
            cristais=0,
            tijolos=0,
        )
        for i in range(8)
    ]


def desenha_zona_de_descarte(screen: pygame.Surface, font: pygame.font.Font):
    texto = font.render("Zona de Descarte", False, TEXT_COLOR)
    screen.blit(texto, (SCREEN_WIDTH - 400, 100))


def desenha_zona_de_jogo(screen: pygame.Surface, font: pygame.font.Font):
    texto = font.render("Zona de Jogo", False, TEXT_COLOR)
    screen.blit(texto, (250, 100))
