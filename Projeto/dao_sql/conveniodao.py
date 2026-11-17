from dao_sql.dao import DAO
from models.convenio import Convenio

class ConvenioDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO convenio (nome, contato, fone)
            VALUES (?, ?, ?)
        """
        cls.execute(sql, (obj.get_nome(), obj.get_contato(), obj.get_fone()))
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM convenio"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [Convenio(id, nome, contato, fone) for (id, nome, contato, fone) in rows]
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM convenio WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Convenio(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE convenio SET nome=?, contato=?, fone=?
            WHERE id=?
        """
        cls.execute(sql, (obj.get_nome(), obj.get_contato(), obj.get_fone(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, id):
        cls.abrir()
        sql = "DELETE FROM convenio WHERE id=?"
        cls.execute(sql, (id,))
        cls.fechar()