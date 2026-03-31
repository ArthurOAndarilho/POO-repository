class Pais:
    def __init__(self):
        self.nome = ""
        self.população = 1
        self.area = 1

    def calc_DD(self):
        return self.população / self.area
    
lista = []
for k in range[10]:

    p = Pais()
    p.nome = input("Nome: ")
    p.populacao = int(input("População: "))
    p.area = float(input("Área: "))

    lista.append(p)