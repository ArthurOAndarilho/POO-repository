class Pais:
    def __init__(self):
        self.nome = ""
        self.populacao = 1
        self.area = 1

    def calc_DD(self):
        return self.populacao / self.area
    
p = Pais()
p.nome = input("Nome: ")
p.populacao = int(input("População: "))
p.area = float(input("Área: "))
print(p.calc_DD())