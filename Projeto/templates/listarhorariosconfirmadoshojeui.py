import streamlit as st
import pandas as pd
from service import Service
from datetime import datetime, date
import time

class ListarHorariosConfirmadosHojeUI:
    @staticmethod
    def main():
        st.header("Horários de hoje: ")
        horas = Service.horario_confirmado_hoje()
        if len(horas) == 0:
            st.write("Nenhum horário salvo de hoje")

        else:
            dic = []
            for obj in horas:
                cliente = Service.cliente_listar_id(obj.get_id_cliente())
                servico = Service.servico_listar_id(obj.get_id_servico())
                profissional = Service.profissional_listar_id(obj.get_id_profissional())
                nome_cliente = cliente.get_name() if cliente else "None"
                desc_servico = servico.get_descricao() if servico else "None"
                nome_profissional = profissional.get_name() if profissional else "None"

                dic.append({"id": obj.get_id(), "data": obj.get_data().strftime("%d/%m/%Y %H/%M"), "cliente": nome_cliente, "servico": desc_servico, "profissional": nome_profissional})
            df = pd.DataFrame(dic)
            st.dataframe(df)