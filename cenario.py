import pygame

from typing import List

from carta import Carta, AcaoCarta
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
            self.__jogador_vermelho
        )
        self.__partida_em_andamento = False
        self.__baralhos_padrao: List[Baralho] = []
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
        return self.__jogador_em_turno_pronto

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
        """Efetua a ação de uma carta dependendo do tipo de ação realizando uma
        mudança no castelo adversário ou no castelo do Jogador.

        Parameters
        ----------
        carta : Carta
            A carta para efetuar a ação.
        castelo_jogador : Castelo
            O castelo do jogador realizando a ação da carta.
        """

        castelo_adversario = self.__castelo_vermelho
        if castelo_jogador is self.__castelo_vermelho:
            castelo_adversario = self.__castelo_azul

        if carta.acao is AcaoCarta.TOWER:
            # Aumenta 10 níveis do castelo.
            castelo_jogador.nivel += 10
        elif carta.acao is AcaoCarta.FIRE_ARCHER:
            # Causa 5 de dano ao adversário.
            castelo_adversario.nivel -= 5
        elif carta.acao is AcaoCarta.KNIGHT:
            # Causa 12 de dano ao adversário.
            castelo_adversario.nivel -= 12
        elif carta.acao is AcaoCarta.RECRUIT:
            # Aumenta 1 soldado.
            castelo_jogador.soldados += 1
        elif carta.acao is AcaoCarta.BUILDER:
            # Aumenta 1 construtor.
            castelo_jogador.construtores += 1
        elif carta.acao is AcaoCarta.TAVERN:
            # Aumenta 15 níveis do castelo.
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
            # próximo ataque.
            castelo_jogador.escudo_magico_buff = True

    def passa_turno_atual_jogador(self):
        """Passa o turno do atual jogador em turno."""

        jogador_em_turno_eh_vermelho = (
            self.__jogador_em_turno is self.__jogador_vermelho
        )
        if jogador_em_turno_eh_vermelho:
            self.__jogador_em_turno = self.__jogador_azul
            self.__jogador_vermelho.em_turno = False
            self.__castelo_vermelho.adicionar_recursos()
        else:
            self.__jogador_em_turno = self.__jogador_vermelho
            self.__jogador_azul.em_turno = False
            self.__castelo_azul.adicionar_recursos()
        self.__jogador_em_turno_pronto = False

    def anuncia_vencedor(self):
        pass

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

        if self.jogadores_estao_prontos():
            self.__partida_em_andamento = True

    def jogadores_estao_prontos(self) -> bool:
        """Verifica se ambos jogadores estão prontos para começar partida."""
        return self.__jogador_azul.pronto and self.__jogador_vermelho.pronto

    def avalia_encerramento_partida(self):
        """Avalia o encerramento da partida verificando se existe um castelo
        e jogador vencedor.
        """

        if (
            self.__castelo_vermelho.nivel == 100
            or self.__castelo_azul.nivel == 0
        ):
            self.__jogador_vermelho.vencedor = True
        elif (
            self.__castelo_azul.nivel == 100 or
            self.__castelo_vermelho.nivel == 0
        ):
            self.__jogador_azul.vencedor = True

    def notifica_vencedor(self):
        pass

    def draw(self, surface: pygame.Surface):
        pass

    def draw_initial_screen(self, surface: pygame.Surface):
        pass
