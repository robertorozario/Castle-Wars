import pygame

from enum import Enum

from constants import CARD_HEIGHT, CARD_WIDTH


class AcaoCarta(Enum):
    TOWER = 1
    FIRE_ARCHER = 2
    KNIGHT = 3
    RECRUIT = 4
    BUILDER = 5
    TAVERN = 6
    MAGE = 7
    ADD_BRICK = 8
    ADD_WEAPON = 9
    MAGIC_DEFENSE = 10


class Carta(pygame.Rect):
    """
    Representação das cartas do jogo que realizam ações.

    Attributes
    ----------
    acao : AcaoCarta
        Tipo de ação que a carta deve efetuar.
    cristais : int
        Quantidade de cristais necessárias para jogar a carta.
    espadas : int
        Quantidade de espadas necessárias para jogar a carta.
    tijolos : int
        Quantidade de tijolos necessários para jogar a carta.
    """

    def __init__(
        self,
        acao: AcaoCarta,
        cristais: int,
        tijolos: int,
        espadas: int,
        descricao: str,
    ):
        super().__init__(0, 0, 0, 0)
        self._acao = acao
        self._cristais = cristais
        self._espadas = espadas
        self._tijolos = tijolos
        self._descricao = descricao
        self._posicao_inicial = None

    @property
    def espadas(self) -> int:
        return self._espadas

    @property
    def cristais(self) -> int:
        return self._cristais

    @property
    def tijolos(self) -> int:
        return self._tijolos

    @property
    def acao(self) -> AcaoCarta:
        return self._acao

    @property
    def descricao(self) -> str:
        return self._descricao

    @property
    def posicao_inicial(self):
        return self._posicao_inicial

    def draw(self, screen: pygame.Surface, top: int, left: int):
        """Draws the card into the pygame screen."""
        # TODO: allow dinamically choose the color from self._tipo
        if self._posicao_inicial is None:
            self._posicao_inicial = (left, top)
        self.top = top
        self.left = left
        self.height = CARD_HEIGHT
        self.width = CARD_WIDTH
        pygame.draw.rect(
            screen,
            125,
            self,
        )


class CartaTower(Carta):
    """
    Carta que efetua a ação de aumentar 10 níveis do castelo do Jogador.
    """

    def __init__(self):
        super().__init__(
            acao=AcaoCarta.TOWER,
            cristais=0,
            tijolos=10,
            espadas=0,
            descricao="Aumenta 10 níveis de seu castelo.",
        )


class CartaFireArcher(Carta):
    """
    Carta que efetua a ação de diminuir 5 níveis do castelo do Jogador
    adversário.
    """

    def __init__(self):
        super().__init__(
            acao=AcaoCarta.FIRE_ARCHER,
            cristais=0,
            tijolos=0,
            espadas=3,
            descricao="Diminui 5 níveis do castelo adversário.",
        )


class CartaKnight(Carta):
    """
    Carta que efetua a ação de atacar o castelo do Jogador adversário causando
    12 de dano, ou seja, diminuindo 12 níveis.
    """

    def __init__(self):
        super().__init__(
            acao=AcaoCarta.KNIGHT,
            cristais=0,
            tijolos=0,
            espadas=10,
            descricao="Ataca o castelo adversário diminuindo 12 níveis dele.",
        )


class CartaRecruit(Carta):
    """
    Carta que efetua a ação de acrescentar 1 soldado ao castelo do Jogador.
    """

    def __init__(self):
        super().__init__(
            acao=AcaoCarta.RECRUIT,
            cristais=0,
            espadas=8,
            tijolos=0,
            descricao="Acrescenta um soldado ao seu castelo.",
        )


class CartaBuilder(Carta):
    """
    Carta que efetua a ação de acrescentar 1 construtor ao castelo do Jogador.
    """

    def __init__(self):
        super().__init__(
            acao=AcaoCarta.BUILDER,
            cristais=0,
            espadas=0,
            tijolos=8,
            descricao="Acrescenta 1 construtor ao seu castelo.",
        )


class CartaTavern(Carta):
    """
    Carta que efetua a ação de acrescentar 15 níveis ao castelo do Jogador.
    """

    def __init__(self):
        super().__init__(
            acao=AcaoCarta.TAVERN,
            cristais=0,
            espadas=0,
            tijolos=12,
            descricao="Acrescenta 15 níveis ao seu castelo.",
        )


class CartaMage(Carta):
    """
    Carta que efetua a ação de acrescentar 1 mago ao castelo do Jogador.
    """

    def __init__(self):
        super().__init__(
            acao=AcaoCarta.MAGE,
            cristais=8,
            espadas=0,
            tijolos=0,
            descricao="Acrescenta 1 mago ao seu castelo.",
        )


class CartaAddBrick(Carta):
    """
    Carta que efetua a ação de acrescentar 8 tijolos ao castelo do Jogador.
    """

    def __init__(self):
        super().__init__(
            acao=AcaoCarta.ADD_BRICK,
            cristais=5,
            espadas=0,
            tijolos=0,
            descricao="Acrescenta 8 tijolos ao seu castelo.",
        )


class CartaAddWeapon(Carta):
    """
    Carta que efetua a ação de acrescentar 8 espadas ao castelo do Jogador.
    """

    def __init__(self):
        super().__init__(
            acao=AcaoCarta.ADD_WEAPON,
            cristais=5,
            espadas=0,
            tijolos=0,
            descricao="Acrescenta 8 espadas ao seu castelo.",
        )


class CartaMagicDefense(Carta):
    """
    Carta que efetua a ação de ativar o BUFF de escudo mágico no castelo do
    Jogador.
    """

    def __init__(self):
        super().__init__(
            acao=AcaoCarta.MAGIC_DEFENSE,
            cristais=15,
            espadas=0,
            tijolos=0,
            descricao="Ativa o buff escudo mágico, impedindo o próximo ataque.",
        )
