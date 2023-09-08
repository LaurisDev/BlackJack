class Blackjack:
    def registrar_jugador(self, nombre: str):
        pass

    def iniciar_juego(self, apuesta:int):
        pass

    def finalizar_juego(self):
        pass


class Carta:
    def __init__(self, pinta: str, valor: str):
        self.pinta: str = pinta
        self.valor: str = valor
        self.tapada: bool = False


class Baraja:
    def __init__(self):
        self.pinta: list[str] = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        self.valor: list[str] = ["CORAZÓN", "TRÉBOL", "DIAMANTE", "ESPADA"]
        pass


    def revolver(self):
        pass

    def repartir_carta(self, tapada: bool) -> Carta:
        pass


class Mano:
    def __init__(self):
        self.cartas = []

    def es_blackjack(self) -> bool:
        pass

    def calcular_mano(self, cartas):
        pass

    def comparar_manos(self, jugador, casa):
        pass

    def empate(self, jugador, casa, mano):
        pass


class Jugador:
    def __init__(self, fichas: int):
        self.fichas: int = fichas

    def inicializar_mano(self, cartas):
        pass

    def pedir_carta(self, cartas) -> Carta:
        pass

    def detener_jugador(self):
        pass

    def cantidad_fichas(self, fichas):
        pass

    def verificar_jugador(self, jugador, mano):
        pass


class Casa:
    def __init__(self, nombre: str, fichas: int):
        self.nombre: str = nombre
        self.fichas: int = fichas

    def inicializar_mano(self, cartas):
        pass

    def destapar_carta_oculta(self, destapada: bool) -> Carta:
        pass

    def verificar_casa(self, casa, mano):
        pass





