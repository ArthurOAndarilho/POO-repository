class Viagem:
    def __init__(self):
        self._d = ""
        self._di = 0
        self._l = 0

    def set_destino(self, destino):
        self._d = destino

    def set_distancia(self, distância):
        self._di = distância

    def set_litros(self, litros):
        self._l = litros

    def get_destino(self):
        return self._d
    
    def get_distancia(self):
        return self._di
    
    def get_litros(self):
        return self._l
    
    def calc_consumo(self):
        return self._di // self._l
    
    def __str__(self):
        return (f"Destino {self._d}\n"
                f"Distância {self._di} km\n"
                f"Combustivel {self._l} L")

class ViagemUI:
    @staticmethod
    def main():
        print("\n--MENU--")
        print("1 - Calcular consumo")
        print("2 - Fim")
        
    @staticmethod
    def menu():
        return int(input("Escolha uma opção: "))
    
    @staticmethod
    def calculo():
        destino = input("Informe o destino: ")
        distancia = float(input("Informe a distância (km): "))
        litros = float(input("Informe o combustível gasto(L): "))

        viagem = Viagem(destino, distancia, litros)

        print("\n --- Dados da viagem ---")
        print(Viagem)

        consumo = Viagem.calc_consumo