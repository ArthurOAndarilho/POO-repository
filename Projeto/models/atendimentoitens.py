from datetime import datetime

class AtendimentoItens:
    def __init__(self, id, id_atendimento, id_servico, qtd, valor):
        self.set_id(id)
        self.set_id_atendimento(id_atendimento)
        self.set_id_servico(id_servico)
        self.set_qtd(qtd)
        self.set_valor(valor)

    def get_id(self): return self.__id
    def get_id_atendimento(self): return self.__id_atendimento
    def get_id_servico(self): return self.__id_servico
    def get_qtd(self): return self.__qtd
    def get_valor(self): return self._valor