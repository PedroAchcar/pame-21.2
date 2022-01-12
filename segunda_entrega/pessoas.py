class Motorista():
    def __init__(self, nome, codigo_motorista, onibus=None):
        self.nome = nome
        self.codigo_motorista = codigo_motorista
        self.onibus = onibus

    def __str__(self):
        return f'{self.codigo_motorista} - {self.nome} - Linha: {self.onibus}'

    def assignarOnibus(self, onibus):
        self.onibus = onibus


class Fiscal():
    def __init__(self, nome, codigo_fiscal, onibus=None):
        self.nome = nome
        self.codigo_fiscal = codigo_fiscal
        self.onibus = onibus

    def __str__(self):
        return f'{self.codigo_fiscal} - {self.nome} - Linha: {self.onibus}'

    def assignarOnibus(self, onibus):
        self.onibus = onibus


# teste = Fiscal('Pedro', 125)
# print(teste)
