import streamlit as st
import pandas as pd
import importlib
import os

from PIL import Image
from gcp_service import surp
from Estatistic_service import select
import eduq as ed

def reset():
    imagem = Image.open("./image/mari.png")
    st.sidebar.image(imagem)
    dp = st.sidebar.selectbox('Selecione o serviço desejado:', ("Serviços:","Gestão de conhecimentos","Vestibular Marie Curie","Estatisticas da educo"))
    return dp

def corp(dp):
    if dp is not None and dp != "Serviços: ":
        # x = st.sidebar.selectbox('Selecione o serviço desejado:', ("Serviços:","Gestão de conhecimentos","Estatísticas Eduquo","Estatisticas"))
        if dp == "Gestão de conhecimentos":
            dv = st.sidebar.selectbox('Selecione o departamento:',("Departamentos:","Captação de Recursos","Ensino-Pedagogico", "Eventos", "Gestão de pessoas", "Inteligência de Dados", "Jurídico Financeiro", "Marketing", "Pedagogico-Social", "Presidencia", "Vice-Presidencia"))
            surp(dv)
        elif dp == "Vestibular Marie Curie":
            select()
        elif dp == "Estatisticas da educo":
            ed.dashboard()
        else:
            image = Image.open("./image/logo.png")
            st.image(image, use_column_width= False)
 
            st.title("Central de Serviços")
            st.subheader("Inteligência de Dados")
            st.write("A central de Serviços da instituição Marie Curie está aqui para prestar de forma flexível e rápida as suas maiores necessidade.")
            st.markdown("** Atualmente contamos com os serviços listados abaixo:**")
            st.write(pd.DataFrame({"Serviços ID": ["Gestão de processos", "Vestibular Marie Curie"]}))
            st.header("Gestão de Conhecimento:")
            st.write("Os serviços da gestão de conhecimentos atualmente são dois: A verificação dos dados GCP e A coleta dos mesmos. Tais serviços estão fortemente ligados ao fluxo de eventos da instituição, propondo uma dinâmica de conhecimentos envolvendo os principais aspectos positivos e negativos. Trazendo a tona o perfil de cada indivíduo e processo.")
            st.header("Vestibular Marie Curie:")
            st.write(" ")

corp(reset())
