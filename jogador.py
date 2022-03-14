from typing import List

from baralho import Baralho
from carta import Carta


class Jogador:
    """
    Classe de representação do Jogador no CastleWars.

    Attributes
    ----------
    vencedor : bool
        Flag indicando se é vencedor.
    baralho : Baralho
        Referência do baralho do Jogador.
    mao : []Carta
        Referência das cartas que o Jogador possui em sua mão.
    em_turno : bool
        Flag que indica se o Jogador está no seu turno.
    pronto : bool
        Flag que indica se o Jogador está pronto para jogar.
    cartas_descartadas_no_turno : int
        Quantidade de cartas que o Jogador já descartou neste turno.
    """

    def __init__(self):
        self.__vencedor: bool = False
        self.__baralho: Baralho = None
        self.__mao: List[Carta] = []
        self.__em_turno: bool = False
        self.__pronto: bool = False
        self.__cartas_descartadas_no_turno: int = 0

    @property
    def em_turno(self) -> bool:
        return self.__em_turno

    @em_turno.setter
    def em_turno(self, em_turno: bool):
        self.__em_turno = em_turno

    @property
    def vencedor(self) -> bool:
        return self.__vencedor

    @vencedor.setter
    def vencedor(self, vencedor: bool):
        self.__vencedor = vencedor

    @property
    def baralho(self) -> Baralho:
        return self.__baralho

    @baralho.setter
    def baralho(self, baralho: Baralho):
        self.__baralho = baralho
        if baralho is not None:
            self.__pronto = True

    @property
    def mao(self) -> List[Carta]:
        return self.__mao

    @mao.setter
    def mao(self, mao: List[Carta]):
        self.__mao = mao

    @property
    def pronto(self) -> bool:
        return self.__pronto

    @pronto.setter
    def pronto(self, pronto: bool):
        self.__pronto = pronto

    @property
    def cartas_descartadas_no_turno(self) -> int:
        return self.__cartas_descartadas_no_turno

    @cartas_descartadas_no_turno.setter
    def cartas_descartadas_no_turno(self, cartas_descartadas_no_turno: int):
        self.__cartas_descartadas_no_turno = cartas_descartadas_no_turno

    def descartar_carta(self, carta: Carta):
        """Descarta um carta da mão do usuário.

        Parameters
        ----------
        indice : int
            O índice da carta na mão a descartar.
        """
        self.__mao.remove(carta)
        self.baralho.adiciona_carta(carta, 1)
        self.__cartas_descartadas_no_turno += 1

    def obtem_carta_da_mao(self, indice: int) -> Carta:
        """Obtem informação de uma carta da mão do Jogador.

        Parameters
        ----------
        indice : int
            O índice da carta na mão a obter informação.

        Returns
        -------
        Carta
            a carta do índice encontrada na mão.
        """
        return self.__mao[indice]

    def descartou_max_cartas(self) -> bool:
        """Verificação se o usuário discartou máximo de cartas no turno, 3.

        Returns
        -------
        bool
            indicação se descartou o máximo de cartas.
        """
        return self.__cartas_descartadas_no_turno == 3

    def jogar_carta(self, indice: int):
        """Joga uma carta da mão do Jogador, mesmo que descartar, remove da mão.

        Parameters
        ----------
        indice : int
            O índice da carta na mão para jogar.
        """
        self.__mao.pop(indice)

    def obtem_mao_jogador(self):
        """Este método obtem cartas para completar o máximo de cartas na mão do
        jogador, que são 8."""
        while len(self.__mao) < 8:
            carta = self.__baralho.obtem_carta_aleatoria()
            self.__mao.append(carta)

    def reset(self):
        """Reinicia os atributos do Jogador para o mesmo estado de
        instanciação.
        """

        self.__vencedor = False
        self.__baralho = None
        self.__mao = []
        self.__em_turno = False
        self.__pronto = False
        self.__cartas_descartadas_no_turno = 0
