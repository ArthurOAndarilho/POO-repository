from dao_sql.dao import DAO
from models.atendimento import Atendimento
from datetime import datetime

class AtendimentoDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO atendimento (data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        cls.execute(sql, (
            obj.get_data().strftime("%d/%m/%Y %H:%M"),
            obj.get_queixa_principal(),
            obj.get_historico_saude(),
            obj.get_avaliacao(),
            obj.get_prescricao(),
            obj.get_id_horario()
        ))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM atendimento"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        cls.fechar()
        
        atendimentos = []
        for reg in rows:
            a = Atendimento(reg[0], datetime.strptime(reg[1], "%d/%m/%Y %H:%M"), reg[2], reg[3], reg[4], reg[5], reg[6])
            atendimentos.append(a)
        return atendimentos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM atendimento WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        reg = cursor.fetchone()
        cls.fechar()
        
        if reg:
            return Atendimento(reg[0], datetime.strptime(reg[1], "%d/%m/%Y %H:%M"), reg[2], reg[3], reg[4], reg[5], reg[6])
        return None

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE atendimento SET data=?, queixa_principal=?, historico_saude=?, avaliacao=?, prescricao=?, id_horario=?
            WHERE id=?
        """
        cls.execute(sql, (
            obj.get_data().strftime("%d/%m/%Y %H:%M"),
            obj.get_queixa_principal(),
            obj.get_historico_saude(),
            obj.get_avaliacao(),
            obj.get_prescricao(),
            obj.get_id_horario(),
            obj.get_id()
        ))
        cls.fechar()

    @classmethod
    def excluir(cls, id):
        cls.abrir()
        sql = "DELETE FROM atendimento WHERE id=?"
        cls.execute(sql, (id,))
        cls.fechar()