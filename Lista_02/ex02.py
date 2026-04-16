class viagem:
    def __init__(self):
        self._d = 0
        self._t = 0

    def set_distancia(self, distancia):
        self._d = distancia

    def set_tempo(self, tempo):
        self._t = tempo

    def get_ditancia(self):
        return self._d
    
    def get_tempo(self):
        return self._t
    
    def velocidade_media(self):
        return self._d // self._t