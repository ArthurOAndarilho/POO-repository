class Time:
    def __init__(self, id, nome, estado):
        self.set_id(id)
        self.set_nome(nome)
        self.set_estado(estado)
    
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")  
        self.id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome não pode ser vazio")  
        self.nome = nome
    def set_estado(self, estado):
        if estado == "": raise ValueError("O estado de federação não poode ser vazio")
        self.estado = estado
    def get_id(self): return self.id    
    def get_nome(self): return self.nome    
    def get_estado(self): return self.estado
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.estado}"
    
class Jogador:
    def __init__(self, id, nome, camisa, idTime):
        self.set_id(id)
        self.set_nome(nome)
        self.set_camisa(camisa)
        self.set_idTime(idTime)
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")  
        self.id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome não pode ser vazio")  
        self.nome = nome
    def set_camisa(self, camisa):
        if camisa == 0: raise ValueError("O número da camisa não pode ser 0")
        self.camisa = camisa
    def set_idTime(self, idTime):
        if idTime == 0: raise ValueError("O ID do time não pode ser 0")
        self.idTime = idTime

    def get_id(self): return self.id    
    def get_nome(self): return self.nome    
    def get_camisa(self): return self.camisa
    def get_idTime(self): return self.idTime
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.camisa} - {self.idTime}"
    
class UI:
    Times = []
    Jogadores = []

    @staticmethod
    def main():
        op = 0
        while op != 12:
            op = UI.menu()
            if op == 1: UI.inserir_time()
            if op == 2: UI.listar_time()
            if op == 3: UI.atualizar_time()
            if op == 4: UI.excluir_time()
            if op == 5: UI.pesquisar_time()
            if op == 6: UI.inserir_jogador()
            if op == 7: UI.listar_jogador()
            if op == 8: UI.atualizar_jogador()
            if op == 9: UI.excluir_jogador()
            if op == 10: UI.pesquisar_jogador()
            if op == 11: UI.Transferir_jogador()
            if op == 12: return exit
    @staticmethod
    def menu():
        print(" -- MENU --\n 1-Inserir time\n 2-Listar times\n 3-Atualizar times\n 4-Excluir time\n 5-Pesquisar time\n 6-Inserir jogador\n 7-Listar jogador\n 8-Atualizar jogadores\n 9-Excluir jogador\n 10-Pesquisar jogador\n 11-Transferir Jogador\n 12-Sair")
        return int(input("Escolha uma opção: "))
    
    @classmethod
    def inserir_time(cls):
        print(" -- Inserir_Time --")
        id = int(input("Informe o id do Time: "))
        nome = input("Informe o nome do time: ")
        estado = input("Informe o estado: ")
        x = Time(id, nome, estado)
        cls.Times.append(x)
        print("Time inserido com sucesso")
    @classmethod
    def Transferir_jogador(cls):
        print(" -- Transferir_Jogador --")
        if len(cls.Jogadores) == 0: print("Nenhum jogador na lista")
    @classmethod
    def inserir_jogador(cls):
        print(" -- Inserir_Jogador --")
        id = int(input("Informe o id do jogador: "))
        nome = input("Informe o nome do jogador: ")
        camisa = int(input("Informe a camisa do jogador: "))
        idTime = int(input("Informe o id do time desse jogador: "))
        x = Jogador(id, nome, camisa, idTime)
        cls.Jogadores.append(x)
        print("Jogador inserido com sucesso")
    
    @classmethod
    def listar_time(cls):
        print(" -- Listar_Time --")
        if len(cls.Times) == 0: print("Nenhum time na lista")
        else:
            for x in cls.Times: print(x)
    @classmethod
    def listar_jogador(cls):
        print(" -- Listar_Jogadores --")
        if len(cls.Jogadores) == 0: print("Nenhum jogador na lista")
        else:
            for x in cls.Jogadores: print(x)
            
    @classmethod
    def Time_listarID(cls, id):
        for x in cls.Times:
            if x.get_id() == id: return x
        return None
    @classmethod
    def Jogador_listarID(cls, id):
        for x in cls.Jogadores:
            if x.get_id() == id: return x
        return None

    @classmethod
    def atualizar_time(cls):
        print(" -- Atualizar_Time --")
        UI.listar_time()
        id = int(input("Informe o id do time a ser alterado: "))
        x = UI.Time_listarID(id)
        if x != None:
            cls.Times.remove(x)
            nome = input("Informe o novo nome: ")
            estado = input("Informe o novo estado: ")
            x = Time(id, nome, estado)
            cls.Times.append(x)
    @classmethod
    def atualizar_jogador(cls):
        print(" -- Atualizar_Jogador --")
        UI.listar_jogador()
        id = int(input("Informe o id do jogador a ser alterado: "))
        x = UI.Jogador_listarID(id)
        if x != None:
            cls.Jogadores.remove(x)
            nome = input("Informe o novo nome: ")
            camisa = input("Informe o nova camisa: ")
            x = Time(id, nome, camisa)
            cls.Jogadores.append(x)

    @classmethod
    def excluir_time(cls):
        print(" -- Excluir_Time --")
        UI.listar_time()
        id = int(input("Informe o id do time a ser excluído: "))
        x = UI.Time_listarID(id)
        if x != None:
            cls.Times.remove(x)
    @classmethod
    def excluir_jogador(cls):
        print(" -- Excluir_Jogador --")
        UI.listar_jogador()
        id = int(input("Informe o id do time a ser excluído: "))
        x = UI.Jogador_listarID(id)
        if x != None:
            cls.Jogadores.remove(x)

    @classmethod
    def pesquisar_time(cls):
        print(" -- Pesquisar_Time --")
        iniciais = input("Informe as iniciais do time: ")
        for x in cls.Times:
            if x.get_nome().startswith(iniciais): print(x)
    @classmethod
    def pesquisar_jogador(cls):
        print(" --Pesquisar_Jogador --")
        iniciais = input("Informe as iniciais do jogador: ")
        for x in cls.Jogadores:
            if x.get_nome().startswith(iniciais): print(x)
UI.main()