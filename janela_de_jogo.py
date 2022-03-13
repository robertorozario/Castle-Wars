import pygame
import typing
import sys

from enum import Enum
from pygame._sdl2 import messagebox
from carta import Carta
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, FONTE_NAME
from cenario import Cenario
from interface_jogador import InterfaceJogador

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
        self.__tela: Tela = Tela.INICIAL
        self.__interface_jogador = InterfaceJogador(
            screen,
            self.__cenario.jogador_azul,
            self.__cenario.jogador_vermelho,
            self.__cenario,
        )

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
            clock.tick(30)

    def _desenha_tela_inicial(self):
        screen = self.__screen

        font = pygame.font.Font(FONTE_NAME, 30)

        texto = font.render("Iniciar Jogo", False, TEXT_COLOR)
        rect_texto = texto.get_rect(
            center=(
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2,
            )
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
            and (SCREEN_HEIGHT / 2) - 32 <= mouse_y <= (SCREEN_HEIGHT / 2) + 32
        ):
            pygame.draw.rect(screen, (105, 105, 105), btn, border_radius=10)
        else:
            pygame.draw.rect(screen, (211, 211, 211), btn, border_radius=10)

        botoes_baralho_azul = []
        for baralho in self.__cenario.baralhos_padrao:
            indice = self.__cenario.baralhos_padrao.index(baralho)
            left = 32
            top = 96 + (80 * indice)
            botao_baralho = pygame.Rect(left, top, 300, 32)
            botoes_baralho_azul.append(
                {
                    "top": top,
                    "left": left,
                    "bottom": top + 32,
                    "right": left + 300,
                }
            )
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (
                self.__cenario.jogador_azul.baralho is not None
            ) and baralho.nome == self.__cenario.jogador_azul.baralho.nome:
                pygame.draw.rect(
                    screen,
                    (0, 0, 204),
                    botao_baralho,
                    border_radius=10,
                )
            else:
                if left <= mouse_x <= 300 and top <= mouse_y <= top + 32:
                    pygame.draw.rect(
                        screen,
                        (105, 105, 105),
                        botao_baralho,
                        border_radius=10,
                    )
                else:
                    pygame.draw.rect(
                        screen,
                        (211, 211, 211),
                        botao_baralho,
                        border_radius=10,
                    )

        botoes_baralho_vermelho = []
        for baralho in self.__cenario.baralhos_padrao:
            indice = self.__cenario.baralhos_padrao.index(baralho)
            left = SCREEN_WIDTH - 32 - 300
            top = 96 + (80 * indice)
            botao_baralho = pygame.Rect(left, top, 300, 32)
            botoes_baralho_vermelho.append(
                {
                    "top": top,
                    "left": left,
                    "bottom": top + 32,
                    "right": left + 300,
                }
            )
            if (
                self.__cenario.jogador_vermelho.baralho is not None
            ) and baralho.nome == self.__cenario.jogador_vermelho.baralho.nome:
                pygame.draw.rect(
                    screen,
                    (204, 0, 0),
                    botao_baralho,
                    border_radius=10,
                )
            else:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if (left <= mouse_x <= SCREEN_WIDTH - 32) and (
                    top <= mouse_y <= (top + 32)
                ):
                    pygame.draw.rect(
                        screen,
                        (105, 105, 105),
                        botao_baralho,
                        border_radius=10,
                    )
                else:
                    pygame.draw.rect(
                        screen,
                        (211, 211, 211),
                        botao_baralho,
                        border_radius=10,
                    )

        for baralho in self.__cenario.baralhos_padrao:
            indice = self.__cenario.baralhos_padrao.index(baralho)
            texto_baralho = font.render(baralho.nome, False, TEXT_COLOR)
            rect_texto_baralho = texto.get_rect(
                center=(
                    198,
                    96 + ((160 * indice) + 32) / 2,
                )
            )
            screen.blit(texto_baralho, rect_texto_baralho)

        for baralho in self.__cenario.baralhos_padrao:
            indice = self.__cenario.baralhos_padrao.index(baralho)
            texto_baralho = font.render(baralho.nome, False, TEXT_COLOR)
            rect_texto_baralho = texto.get_rect(
                center=(
                    SCREEN_WIDTH - 154,
                    96 + ((160 * indice) + 32) / 2,
                )
            )
            screen.blit(texto_baralho, rect_texto_baralho)

        screen.blit(
            font.render("Escolha baralho do jogador azul", False, TEXT_COLOR),
            (32, 32),
        )

        texto_escolha_vermelho = font.render(
            "Escolha baralho do jogador vermelho",
            False,
            TEXT_COLOR,
        )
        screen.blit(
            texto_escolha_vermelho,
            (SCREEN_WIDTH - 32 - texto_escolha_vermelho.get_width(), 32),
        )

        screen.blit(texto, rect_texto)

        comprimento_texto = texto.get_width()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__loop = False
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                half_width = SCREEN_WIDTH / 2
                half_height = SCREEN_HEIGHT / 2
                if (
                    (half_width - comprimento_texto)
                    <= mouse_x
                    <= (half_width + comprimento_texto)
                ) and ((half_height - 32) <= mouse_y <= (half_height + 32)):
                    if self.__cenario.jogadores_estao_prontos():
                        self.__tela = Tela.JOGO
                        self.__cenario.iniciar_jogo()
                    else:
                        messagebox(
                            "Erro",
                            "Algum jogador ainda não selecionou o baralho",
                        )

                for botao in botoes_baralho_vermelho:
                    if (botao["left"] <= mouse_x <= botao["right"]) and (
                        botao["top"] <= mouse_y <= botao["bottom"]
                    ):
                        indice = botoes_baralho_vermelho.index(botao)
                        self.__interface_jogador.seleciona_baralho(
                            indice,
                            "vermelho",
                        )

                for botao in botoes_baralho_azul:
                    if (botao["left"] <= mouse_x <= botao["right"]) and (
                        botao["top"] <= mouse_y <= botao["bottom"]
                    ):
                        indice = botoes_baralho_azul.index(botao)
                        self.__interface_jogador.seleciona_baralho(
                            indice,
                            "azul",
                        )

    def _desenha_tela_troca_de_turno(self):
        screen = self.__screen

        font = pygame.font.Font(FONTE_NAME, 20)

        jogador_em_turno_eh_vermelho = (
            self.__cenario.jogador_em_turno == self.__cenario.jogador_vermelho
        )

        screen.fill(BG_COLOR)
        if jogador_em_turno_eh_vermelho:
            pts_text = font.render(
                "Turno do jogador vermelho, clique para continuar",
                FONTE_NAME,
                TEXT_COLOR,
            )
        else:
            pts_text = font.render(
                "Turno do jogador azul, clique para continuar",
                FONTE_NAME,
                TEXT_COLOR,
            )
        rect_pts_text = pts_text.get_rect(
            center=(
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2,
            )
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

        jogador_em_turno_eh_vermelho = (
            self.__cenario.jogador_em_turno == self.__cenario.jogador_vermelho
        )
        cartas = []
        if jogador_em_turno_eh_vermelho:
            cartas = self.__cenario.jogador_vermelho.mao
        else:
            cartas = self.__cenario.jogador_azul.mao

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
            <= (SCREEN_WIDTH / 2 + passa_turno_texto.get_width() * 1.2)
        ) and 30 <= mouse_y <= 30 + 60:

            pygame.draw.rect(
                screen,
                (152, 173, 139),
                passar_turno_btn,
                border_radius=10,
            )
        else:
            pygame.draw.rect(
                screen,
                (211, 211, 211),
                passar_turno_btn,
                border_radius=10,
            )
        screen.blit(passa_turno_texto, rect_passa_turno_texto)

        # Desenha castelos na tela.
        castelo_azul.draw(screen)
        castelo_azul.draw_info(screen)
        castelo_vermelho.draw(screen)
        castelo_vermelho.draw_info(screen)

        # Desenha as cartas da mão do usuário.
        initial_left = 50
        TOP = 545
        for carta in cartas:
            if carta.posicao_inicial is None:
                left = (cartas.index(carta) * 150) + initial_left
                top = TOP
                carta.draw(screen, top, left)
            else:
                carta.draw(screen, carta.top, carta.left)

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
                        carta_x = self.__carta_selecionada.left
                        carta_y = self.__carta_selecionada.top
                        self.__carta_selecionada.left = carta_x
                        self.__carta_selecionada.top = carta_y
                        self.__carta_selecionada = None
                elif (
                    ((SCREEN_WIDTH / 2) - (103 / 1.65)) <= mouse_x
                    and mouse_x <= ((SCREEN_WIDTH / 2) + (103 * 1.2))
                    and 30 <= mouse_y <= 30 + 60
                ):
                    self.__tela = Tela.TROCA_DE_TURNO
                    self.__interface_jogador.passar_turno()
                else:
                    self.__tela = Tela.JOGO
            elif event.type == pygame.MOUSEMOTION:
                # No movimento do mouse "arrasta" a carta junto.
                if self.__carta_selecionada is not None:
                    botao_esquerdo_pressionado = event.buttons[0]
                    if botao_esquerdo_pressionado:
                        self.__carta_selecionada.left = event.pos[0]
                        self.__carta_selecionada.top = event.pos[1]


def desenha_zona_de_descarte(screen: pygame.Surface, font: pygame.font.Font):
    texto = font.render("Zona de Descarte", False, TEXT_COLOR)
    screen.blit(texto, (SCREEN_WIDTH - 400, 100))


def desenha_zona_de_jogo(screen: pygame.Surface, font: pygame.font.Font):
    texto = font.render("Zona de Jogo", False, TEXT_COLOR)
    screen.blit(texto, (250, 100))
