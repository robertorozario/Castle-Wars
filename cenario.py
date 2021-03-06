from pygame._sdl2 import messagebox

import pygame

from typing import List

from carta import (
    Carta,
    AcaoCarta,
    CartaAddBrick,
    CartaAddWeapon,
    CartaBuilder,
    CartaFireArcher,
    CartaKnight,
    CartaMage,
    CartaMagicDefense,
    CartaRecruit,
    CartaTower,
    CartaTavern,
)
from baralho import Baralho
from castelo import Castelo
from jogador import Jogador


class Cenario:
    def __init__(self):
        self.__jogador_vermelho = Jogador()
        self.__jogador_azul = Jogador()
        self.__castelo_azul = Castelo.azul(Castelo, self.__jogador_azul)
        self.__castelo_vermelho = Castelo.vermelho(
            Castelo,
            self.__jogador_vermelho,
        )
        self.__partida_em_andamento = False
        self.__baralhos_padrao: List[Baralho] = [
            Baralho(
                nome="Completo",
                cartas=[CartaFireArcher() for _ in range(5)]
                + [CartaKnight() for _ in range(5)]
                + [CartaRecruit() for _ in range(5)]
                + [CartaBuilder() for _ in range(5)]
                + [CartaTower() for _ in range(5)]
                + [CartaTavern() for _ in range(5)]
                + [CartaMage() for _ in range(5)]
                + [CartaAddBrick() for _ in range(5)]
                + [CartaAddWeapon() for _ in range(5)]
                + [CartaMagicDefense() for _ in range(5)],
            ),
            Baralho(
                nome="Balanceado",
                cartas=[CartaFireArcher() for _ in range(5)]
                + [CartaKnight() for _ in range(3)]
                + [CartaRecruit() for _ in range(3)]
                + [CartaBuilder() for _ in range(2)]
                + [CartaTower() for _ in range(5)]
                + [CartaTavern() for _ in range(2)],
            ),
            Baralho(
                nome="Controle",
                cartas=[CartaBuilder() for _ in range(4)]
                + [CartaTower() for _ in range(5)]
                + [CartaTavern() for _ in range(5)]
                + [CartaAddBrick() for _ in range(5)]
                + [CartaMagicDefense() for _ in range(3)]
                + [CartaMage() for _ in range(3)],
            ),
            Baralho(
                nome="Slow Burn",
                cartas=[CartaBuilder() for _ in range(5)]
                + [CartaMage() for _ in range(5)]
                + [CartaFireArcher() for _ in range(5)]
                + [CartaMagicDefense() for _ in range(5)]
                + [CartaTower() for _ in range(5)],
            ),
            Baralho(
                nome="Mass Attack",
                cartas=[CartaRecruit() for _ in range(5)]
                + [CartaKnight() for _ in range(5)]
                + [CartaMage() for _ in range(3)]
                + [CartaAddWeapon() for _ in range(5)]
                + [CartaFireArcher() for _ in range(2)]
                + [CartaTower() for _ in range(3)],
            ),
        ]
        self.__jogador_em_turno: Jogador = None
        self.__jogador_em_turno_pronto: bool = False

    @property
    def castelo_azul(self) -> Castelo:
        return self.__castelo_azul

    @property
    def castelo_vermelho(self) -> Castelo:
        return self.__castelo_vermelho

    @property
    def jogador_vermelho(self) -> Jogador:
        return self.__jogador_vermelho

    @property
    def jogador_azul(self) -> Jogador:
        return self.__jogador_azul

    @property
    def partida_em_andamento(self) -> bool:
        return self.__partida_em_andamento

    @partida_em_andamento.setter
    def partida_em_andamento(self, partida_em_andamento: bool):
        self.__partida_em_andamento = partida_em_andamento

    @property
    def baralhos_padrao(self) -> List[Baralho]:
        return self.__baralhos_padrao

    @property
    def jogador_em_turno(self) -> Jogador:
        return self.__jogador_em_turno

    @jogador_em_turno.setter
    def jogador_em_turno(self, jogador_em_turno: Jogador):
        self.__jogador_em_turno = jogador_em_turno

    @property
    def jogador_em_turno_pronto(self) -> bool:
        return self.__jogador_em_turno_pronto

    @jogador_em_turno_pronto.setter
    def jogador_em_turno_pronto(self, jogador_em_turno_pronto: bool):
        self.__jogador_em_turno_pronto = jogador_em_turno_pronto

    def obtem_castelo_jogador(self, jogador: Jogador) -> Castelo:
        """Dado um Jogador obtem o castelo associado a ele.

        Parameters
        ----------
        jogador : Jogador
            O jogador para buscar o Castelo.

        Returns
        -------
        Castelo
            o castelo do jogador.
        """

        if jogador is self.__jogador_azul:
            return self.__castelo_azul
        return self.__castelo_vermelho

    def efetua_acao_da_carta(self, carta: Carta, castelo_jogador: Castelo):
        """Efetua a a????o de uma carta dependendo do tipo de a????o realizando uma
        mudan??a no castelo advers??rio ou no castelo do Jogador.

        Parameters
        ----------
        carta : Carta
            A carta para efetuar a a????o.
        castelo_jogador : Castelo
            O castelo do jogador realizando a a????o da carta.
        """

        castelo_adversario = self.__castelo_vermelho
        if castelo_jogador is self.__castelo_vermelho:
            castelo_adversario = self.__castelo_azul

        if carta.acao is AcaoCarta.TOWER:
            # Aumenta 10 n??veis do castelo.
            castelo_jogador.nivel += 10
        elif carta.acao is AcaoCarta.FIRE_ARCHER:
            # Causa 5 de dano ao advers??rio.
            if castelo_adversario.escudo_magico_buff:
                castelo_adversario.escudo_magico_buff = False
            else:
                castelo_adversario.nivel -= 5
        elif carta.acao is AcaoCarta.KNIGHT:
            # Causa 12 de dano ao advers??rio.
            if castelo_adversario.escudo_magico_buff:
                castelo_adversario.escudo_magico_buff = False
            else:
                castelo_adversario.nivel -= 12
        elif carta.acao is AcaoCarta.RECRUIT:
            # Aumenta 1 soldado.
            castelo_jogador.soldados += 1
        elif carta.acao is AcaoCarta.BUILDER:
            # Aumenta 1 construtor.
            castelo_jogador.construtores += 1
        elif carta.acao is AcaoCarta.TAVERN:
            # Aumenta 15 n??veis do castelo.
            castelo_jogador.nivel += 15
        elif carta.acao is AcaoCarta.MAGE:
            # Adiciona 1 mago.
            castelo_jogador.magos += 1
        elif carta.acao is AcaoCarta.ADD_BRICK:
            # Gera 8 tijolos.
            castelo_jogador.tijolos += 8
        elif carta.acao is AcaoCarta.ADD_WEAPON:
            # Gera 8 espadas.
            castelo_jogador.espadas += 8
        elif carta.acao is AcaoCarta.MAGIC_DEFENSE:
            # Ativa o buff de magic defense, ativa uma barreira que protege o
            # pr??ximo ataque.
            castelo_jogador.escudo_magico_buff = True

    def passa_turno_atual_jogador(self):
        """Passa o turno do atual jogador em turno."""

        encerrar_partida = self.avalia_encerramento_partida()
        if encerrar_partida:
            self.anuncia_vencedor()
            self.finaliza_partida()
        else:
            jogador_em_turno_eh_vermelho = (
                self.__jogador_em_turno is self.__jogador_vermelho
            )
            if jogador_em_turno_eh_vermelho:
                self.__jogador_em_turno = self.__jogador_azul
                self.__jogador_vermelho.em_turno = False
                self.__jogador_azul.em_turno = True
                self.__castelo_vermelho.adicionar_recursos()
            else:
                self.__jogador_em_turno = self.__jogador_vermelho
                self.__jogador_azul.em_turno = False
                self.__jogador_vermelho.em_turno = True
                self.__castelo_azul.adicionar_recursos()
            self.__jogador_em_turno_pronto = False

    def anuncia_vencedor(self):
        if self.__jogador_azul.vencedor:
            vencedor = "Azul"
        else:
            vencedor = "Vermelho"
        self.__jogador_azul.vencedor = False
        self.__jogador_vermelho.vencedor = False
        messagebox(
                            f"Jogador {vencedor} vencedor",
                            f"Jogador {vencedor} venceu a partida!",
                        )

    def finaliza_partida(self):
        """Finaliza a partida permitindo iniciar uma nova partida."""

        self.__jogador_azul.reset()
        self.__jogador_vermelho.reset()
        self.__castelo_azul.reset()
        self.__castelo_vermelho.reset()

        self.__partida_em_andamento = False
        self.__jogador_em_turno = None
        self.__jogador_em_turno_pronto = False

    def iniciar_jogo(self):
        """Inicia o jogo se os jogadores estiverem prontos."""
        jogadores_prontos = self.jogadores_estao_prontos()
        if jogadores_prontos:
            self.__castelo_azul.aplica_configuracao_inicial()
            self.__castelo_vermelho.aplica_configuracao_inicial()
            self.jogador_em_turno = self.__jogador_azul
            self.__jogador_azul.obtem_mao_jogador()
            self.__jogador_vermelho.obtem_mao_jogador()
            self.__partida_em_andamento = True

    def jogadores_estao_prontos(self) -> bool:
        """Verifica se ambos jogadores est??o prontos para come??ar partida."""
        return self.__jogador_azul.pronto and self.__jogador_vermelho.pronto

    def avalia_encerramento_partida(self) -> bool:
        """Avalia o encerramento da partida verificando se existe um castelo
        e jogador vencedor.
        """

        nivel_vermelho = self.__castelo_vermelho.nivel
        nivel_azul = self.__castelo_azul.nivel
        if nivel_vermelho >= 100 or nivel_azul <= 0:
            self.__jogador_vermelho.vencedor = True
            return True
        elif nivel_azul >= 100 or nivel_vermelho <= 0:
            self.__jogador_azul.vencedor = True
            return True
        return False
