class agua:
    def __init__(self, mes, ano, consumo):
        self.mes = mes
        self.ano = ano
        self.consumo = consumo

    def conta(self):
        if self.consumo <= 10:
            return 38
        
        elif 11 <= self.consumo <= 20:
            return 38 + (self.consumo - 10) * 5

        else:
            return 88 + (self.consumo - 20) * 6
        

