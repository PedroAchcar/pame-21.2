class Parada():
    def __init__(self, paradas: list):
        self.paradas = paradas

    def __str__(self) -> str:
        return f'{self.paradas}'

    def criarParada(self, nova_parada):
        self.paradas.append(nova_parada)
