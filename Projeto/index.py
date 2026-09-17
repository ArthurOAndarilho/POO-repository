from templates.manterclienteui import ManterClienteUI
from templates.manterservicoui import ManterServicoUI
from templates.manterhorarioui import ManterHorarioUI
from templates.manterconvenioui import ManterConvenioUI
from templates.manterprofissionalui import ManterProfissionalUI
import streamlit as st

class IndexUI:
    def main():
        op = st.sidebar.selectbox("Menu", ["Clientes", "Serviços", "Horários", "Convênios", "Profissionais"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Serviços": ManterServicoUI.main()
        if op == "Horários": ManterHorarioUI.main()
        if op == "Convênios": ManterConvenioUI.main()
        if op == "Profissionais": ManterProfissionalUI.main()

IndexUI.main()