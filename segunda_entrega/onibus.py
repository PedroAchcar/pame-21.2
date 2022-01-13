class Onibus():
    def __init__(self, codigo_onibus, descricao, motorista=None, fiscal=None, rota=None):
        self.codigo_onibus = codigo_onibus
        self.descricao = descricao
        self.motorista = motorista
        self.fiscal = fiscal
        self.rota = rota

    def __str__(self):
        return f'{self.codigo_onibus}'

    def assignarMotorista(self, motorista):
        self.motorista = motorista

    def assignarFiscal(self, fiscal):
        self.fiscal = fiscal

    def assignarRota(self, rota):
        self.rota = rota
