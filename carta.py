import pygame

from enum import Enum


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


class Carta(pygame.sprite.Sprite):
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
        x_pos: int,
        y_pos: int,
        path: str,
    ):
        super().__init__()
        self._acao = acao
        self._cristais = cristais
        self._espadas = espadas
        self._tijolos = tijolos
        self._descricao = descricao
        self._posicao_inicial = None
        self._image: pygame.Surface = pygame.image.load(path)
        self._rect: pygame.Rect = self.image.get_rect(center=(x_pos, y_pos))

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

    @property
    def image(self) -> pygame.Surface:
        return self._image

    @image.setter
    def image(self, image: pygame.Surface):
        self._image = image

    @property
    def rect(self) -> pygame.Rect:
        return self._rect

    @rect.setter
    def rect(self, rect: pygame.Rect):
        self._rect = rect


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
            x_pos=0,
            y_pos=0,
            path="Carta_Template.png",
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
            x_pos=0,
            y_pos=0,
            path="Carta_Template.png",
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
            x_pos=0,
            y_pos=0,
            path="Carta_Template.png",
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
            x_pos=0,
            y_pos=0,
            path="Carta_Template.png",
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
            x_pos=0,
            y_pos=0,
            path="Carta_Template.png",
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
            x_pos=0,
            y_pos=0,
            path="Carta_Template.png",
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
            x_pos=0,
            y_pos=0,
            path="Carta_Template.png",
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
            x_pos=0,
            y_pos=0,
            path="Carta_Template.png",
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
            x_pos=0,
            y_pos=0,
            path="Carta_Template.png",
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
            x_pos=0,
            y_pos=0,
            path="Carta_Template.png",
        )
