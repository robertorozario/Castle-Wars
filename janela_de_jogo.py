import pygame
import sys

from enum import Enum
from pygame._sdl2 import messagebox
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, FONTE_NAME
from cenario import Cenario
from interface_jogador import InterfaceJogador

BG_COLOR = (173, 203, 222)
ACCENT_COLOR = (145, 145, 145)
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
        self.__carta_selecionada = None
        self.__hand_group = pygame.sprite.Group()
        self.__grupo_selecionada = pygame.sprite.Group()
        self.__tela: Tela = Tela.INICIAL
        self.__interface_jogador = InterfaceJogador(
            screen,
            self.__cenario.jogador_azul,
            self.__cenario.jogador_vermelho,
            self.__cenario,
        )

    def inicia_loop_jogo(self):
        self.__loop = True
        self.__cenario.jogador_em_turno = self.__cenario.jogador_azul

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
            top = 96 + (100 * indice)
            botao_baralho = pygame.Rect(left, top, 300, 60)
            botoes_baralho_azul.append(
                {
                    "top": top,
                    "left": left,
                    "bottom": top + 100,
                    "right": left + 300,
                }
            )
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (
                self.__cenario.jogador_azul.baralho is not None
            ) and baralho.nome == self.__cenario.jogador_azul.baralho.nome:
                pygame.draw.rect(
                    screen,
                    (86, 86, 232),
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
            top = 96 + (100 * indice)
            botao_baralho = pygame.Rect(left, top, 300, 60)
            botoes_baralho_vermelho.append(
                {
                    "top": top,
                    "left": left,
                    "bottom": top + 60,
                    "right": left + 300,
                }
            )
            if (
                self.__cenario.jogador_vermelho.baralho is not None
            ) and baralho.nome == self.__cenario.jogador_vermelho.baralho.nome:
                pygame.draw.rect(
                    screen,
                    (230, 80, 80),
                    botao_baralho,
                    border_radius=10,
                )
            else:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if (left <= mouse_x <= SCREEN_WIDTH - 60) and (
                    top <= mouse_y <= (top + 60)
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
                    96 + ((200 * indice) + 60) / 2,
                )
            )
            screen.blit(texto_baralho, rect_texto_baralho)

        for baralho in self.__cenario.baralhos_padrao:
            indice = self.__cenario.baralhos_padrao.index(baralho)
            texto_baralho = font.render(baralho.nome, False, TEXT_COLOR)
            rect_texto_baralho = texto.get_rect(
                center=(
                    SCREEN_WIDTH - 154,
                    96 + ((200 * indice) + 60) / 2,
                )
            )
            screen.blit(texto_baralho, rect_texto_baralho)

        screen.blit(
            font.render("Escolha baralho do jogador azul", False, (255,255,255)),
            (32, 32),
        )

        texto_escolha_vermelho = font.render(
            "Escolha baralho do jogador vermelho",
            False,
            (255,255,255),
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
            if self.__carta_selecionada is not None:
                self.__cenario.jogador_azul.baralho.adiciona_carta(self.__carta_selecionada, 1)
                self.__cenario.jogador_azul.mao.remove(self.__carta_selecionada)
                self.__cenario.jogador_azul.obtem_mao_jogador()
        else:
            pts_text = font.render(
                "Turno do jogador azul, clique para continuar",
                FONTE_NAME,
                TEXT_COLOR,
            )
            if self.__carta_selecionada is not None:
                self.__cenario.jogador_vermelho.baralho.adiciona_carta(self.__carta_selecionada, 1)
                self.__cenario.jogador_vermelho.mao.remove(self.__carta_selecionada)
                self.__cenario.jogador_vermelho.obtem_mao_jogador()
        rect_pts_text = pts_text.get_rect(
            center=(
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2,
            )
        )
        screen.blit(pts_text, rect_pts_text)
        self.__hand_group.empty()
        self.__carta_selecionada = None
        self.ouve_eventos(pygame.Rect(-100, -100, 1, 1))

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

        #Grupo de Sprites pra desenhar mão do jogador
        hand_group = pygame.sprite.Group()

        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_rect = pygame.Rect(mouse_x, mouse_y, 60, 60)
        pygame.draw.rect(self.__screen, "Grey", mouse_rect)
        self.ouve_eventos(mouse_rect)

        # Background Stuff
        screen.fill(BG_COLOR)

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

        # Desenha zonas de arraste das cartas.
        desenha_zona_de_jogo(screen, font)
        desenha_zona_de_descarte(screen, font)

        # Desenha as cartas da mão do usuário.
        pos_x = 115
        pos_y = 620
        for carta in cartas:
            if carta.posicao_inicial is None:
                left = (cartas.index(carta) * 150) + pos_x
                top = pos_y
                carta.rect = carta.image.get_rect(center=(left, top))
                self.__hand_group.add(carta)
            else:
                self.__hand_group.add(carta)
        self.__hand_group.draw(screen)

        if jogador_em_turno_eh_vermelho:
            screen.blit(font.render("turno do jogador Vermelho", False, (0,0,0)),(SCREEN_WIDTH/2.5, 100))
        else:
            screen.blit(font.render("turno do jogador Azul", False, (0,0,0)),(SCREEN_WIDTH/2.4, 100))

    def ouve_eventos(self, mouse_rect):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        print(self.__carta_selecionada)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.MOUSEBUTTONUP:
                # Botão do mouse foi solto, seleciona carta ou ativa botões
                for carta in self.__hand_group:
                    if pygame.Rect.colliderect(carta.rect, mouse_rect):
                        self.__carta_selecionada = carta

                if (
                    ((SCREEN_WIDTH / 2) - (103 / 1.65)) <= mouse_x
                    and mouse_x <= ((SCREEN_WIDTH / 2) + (103 * 1.2))
                    and 30 <= mouse_y <= 30 + 60
                    and self.__tela == Tela.JOGO
                ):
                    self.__tela = Tela.TROCA_DE_TURNO
                    self.__interface_jogador.passar_turno()

                elif self.__carta_selecionada is not None:
                    if (
                        225 <= mouse_x <= 375
                       ) and 80 <= mouse_y <= 140\
                         and self.__tela == Tela.JOGO:
                        if (self.__cenario.obtem_castelo_jogador(self.__cenario.jogador_em_turno).possui_recurso_pra_carta(self.__carta_selecionada)):
                            self.__cenario.efetua_acao_da_carta(self.__carta_selecionada, self.__cenario.obtem_castelo_jogador(self.__cenario.jogador_em_turno))
                            self.__tela = Tela.TROCA_DE_TURNO
                            self.__interface_jogador.passar_turno()
                        else:
                            messagebox(
                                "Erro",
                                "Recursos insuficientes.",
                            )
                else:
                    self.__tela = Tela.JOGO


def desenha_zona_de_descarte(screen: pygame.Surface, font: pygame.font.Font):
    descarta_texto = font.render("Descartar Carta", False, TEXT_COLOR)
    rect_texto = descarta_texto.get_rect(
        center=(1000, 110)
    )
    descarta_btn = pygame.Rect(
        SCREEN_WIDTH - (descarta_texto.get_width() *2.32),
        80,
        descarta_texto.get_width() * 1.2,
        60,
    )

    # Highlight do botão de passar turno quando o mouse estiver sobre
    # ele.
    mouse_x, mouse_y = pygame.mouse.get_pos()
    #print(((SCREEN_WIDTH) - (descarta_texto.get_width() * 2.32) + descarta_texto.get_width() * 1.2)) 1106.24
    #print((SCREEN_WIDTH) - (descarta_texto.get_width() * 2.32)) 898.64
    #print(80) 80
    # print(80 + 60) 140
    if (
        (SCREEN_WIDTH) - (descarta_texto.get_width() * 2.32)
        <= mouse_x
        <= ((SCREEN_WIDTH) - (descarta_texto.get_width() * 2.32) + descarta_texto.get_width() * 1.2)
    ) and 80 <= mouse_y <= 80 + 60:

        pygame.draw.rect(
            screen,
            (152, 173, 139),
            descarta_btn,
            border_radius=10,
        )
    else:
        pygame.draw.rect(
            screen,
            (211, 211, 211),
            descarta_btn,
            border_radius=10,
        )
    screen.blit(descarta_texto, rect_texto)


def desenha_zona_de_jogo(screen: pygame.Surface, font: pygame.font.Font):
    jogar_texto = font.render("Jogar Carta", False, TEXT_COLOR)
    rect_texto = jogar_texto.get_rect(
        center=(300, 110)
    )
    jogar_btn = pygame.Rect(
        225,
        80,
        jogar_texto.get_width() * 1.2,
        60,
    )
    # Highlight do botão de passar turno quando o mouse estiver sobre
    # ele.
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # print(225) 225
    #print(225 + (jogar_texto.get_width() / 1.2)) 330
    # print(80) 80
    # print(80 + 60) 140
    if (
        (225)
        <= mouse_x
        <= (375)
    ) and 80 <= mouse_y <= 80 + 60:

        pygame.draw.rect(
            screen,
            (152, 173, 139),
            jogar_btn,
            border_radius=10,
        )
    else:
        pygame.draw.rect(
            screen,
            (211, 211, 211),
            jogar_btn,
            border_radius=10,
        )
    screen.blit(jogar_texto, rect_texto)
