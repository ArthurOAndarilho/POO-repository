import math

class Circulo:
    def __init__(self):
        self.__r = 0

    def set_raio(self, raio):
        self._r = raio

    def get_raio(self):
        return self._r

    def calc_area(self):
        return math.pi * self._r ** 2
    
    def calc_circunferencia(self):
        return 2 * math.pi * self._r