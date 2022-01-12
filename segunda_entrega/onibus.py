class Onibus():
    def __init__(self, codigo_onibus, descricao, motorista=None, fiscal=None, pontos=None):
        self.codigo_onibus = codigo_onibus
        self.descricao = descricao
        self.motorista = motorista
        self.fiscal = fiscal
        self.pontos = pontos

    def __str__(self):
        return f'{self.codigo_onibus}'

    def assignarMotorista(self, motorista):
        self.motorista = motorista

    def assignarFiscal(self, fiscal):
        self.fiscal = fiscal

    def adicionarPontoOnibus(self, parada):
        if parada not in self.pontos:
            self.pontos.append(parada)
        else:
            return f'Esta parada já esta na rota do onibus {self.codigo_onibus}'
