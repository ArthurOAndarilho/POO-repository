import datetime
class Treino:
    def __init__(self, id, dt, di, t):
        self.set_id(id)
        self.set_data(dt)
        self.set_distancia(di)
        self.set_tempo(t)
    def set_id(self, id):
        if id < 0: raise ValueError("Id não pode ser negativo")
        self.__id = id
    def set_data(self, dt):
        if dt > datetime.datetime.now(): raise ValueError("Data não pode estar no futuro")
        self.__data = dt
    def set_distancia(self, di):
        if di <= 0.0: raise ValueError("Distância presiva ser maior que 0")
        self.__distancia = di
    def set_tempo(self, t):
        if t == "": raise ValueError("O tempo não pode ser vazio")
        self.__tempo = t
    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_distancia(self): return self.__distancia
    def get_tempo(self): return self.__tempo

    def Pace(self):
        p = self.__tempo.total_seconds() / self.__distancia
    
x = Treino()