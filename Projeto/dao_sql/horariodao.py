from dao_sql.dao import DAO
from models.horario import Horario
from datetime import datetime

class HorarioDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO horario (data, confirmado, id_cliente, id_servico, id_profissional)
            VALUES (?, ?, ?, ?, ?)
        """
        cls.execute(sql, (
            obj.get_data().strftime("%d/%m/%Y %H:%M"),
            1 if obj.get_confirmado() else 0,
            obj.get_id_cliente(),
            obj.get_id_servico(),
            obj.get_id_profissional()
        ))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM horario"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        cls.fechar()
        
        horarios = []
        for reg in rows:
            h = Horario(reg[0], datetime.strptime(reg[1], "%d/%m/%Y %H:%M"))
            h.set_confirmado(bool(reg[2]))
            h.set_id_cliente(reg[3])
            h.set_id_servico(reg[4])
            h.set_id_profissional(reg[5])
            horarios.append(h)
        return horarios

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM horario WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        reg = cursor.fetchone()
        cls.fechar()
        
        if reg:
            h = Horario(reg[0], datetime.strptime(reg[1], "%d/%m/%Y %H:%M"))
            h.set_confirmado(bool(reg[2]))
            h.set_id_cliente(reg[3])
            h.set_id_servico(reg[4])
            h.set_id_profissional(reg[5])
            return h
        return None

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE horario SET data=?, confirmado=?, id_cliente=?, id_servico=?, id_profissional=?
            WHERE id=?
        """
        cls.execute(sql, (
            obj.get_data().strftime("%d/%m/%Y %H:%M"),
            1 if obj.get_confirmado() else 0,
            obj.get_id_cliente(),
            obj.get_id_servico(),
            obj.get_id_profissional(),
            obj.get_id()
        ))
        cls.fechar()

    @classmethod
    def excluir(cls, id):
        cls.abrir()
        sql = "DELETE FROM horario WHERE id=?"
        cls.execute(sql, (id,))
        cls.fechar()