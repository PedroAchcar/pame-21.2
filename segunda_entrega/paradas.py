class Parada():
    def __init__(self, codigo, nome):
        self.codigo_parada = codigo
        self.nome = nome

    def __str__(self):
        return f'{self.codigo_parada} - {self.nome}'


class Rota():
    def __init__(self, paradas: list, codigo_rota):
        self.paradas = paradas
        self.codigo_rota = codigo_rota

    def __str__(self):
        return f'{self.codigo_rota}'

    def adicionarPonto(self, ponto):
        self.paradas.append(ponto)
