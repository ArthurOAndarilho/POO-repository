class Retangulo:
    def __init__(self):
        self._b = 0
        self._h = 0
    
    def set_base(self, base):
        self._b = base

    def set_altura(self, altura):
        self._h = altura

    def get_base(self):
        return self._b

    def get_altura(self):
        return self._h
    
    def calc_area(self):
        return self._b * self._h
    
    def calc_diagonal(self):
        self._b ** 2 + self._h ** 2 == x ** 2
        y = x ** 0.5
        return y
    
p = Retangulo()
p.base = int(input())
p.altura = int(input())
print(p.calc_area())
print(p.calc_diagonal())