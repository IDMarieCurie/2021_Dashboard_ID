import streamlit as st
import pandas as pd
import Estatistic as Es
from io import BytesIO
import base64
from PIL import Image

def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    processed_data = output.getvalue()
    return processed_data

def get_table_download_link(df,name):

    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    val = to_excel(df)
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{name}.xlsx">Download xlsx file</a>' # decode b'abc' => abc

def select():
    mac_image = Image.open("./image/logo_marie_curie-01.png")
    st.image(mac_image,use_column_width=True)
    st.title("Vestibular Marie Curie")
    st.subheader("**Primeiro inserira a planilha de inscrição dos candidatos.**")
    st.set_option('deprecation.showfileUploaderEncoding', False)
    file = st.file_uploader('Arraste a planilha, ou clique em "browse files"', type="xlsx")
    if file is not None:
        file = pd.read_excel(file)
        data = Es.trata_id(file)
        Mc,Mm = Es.mc_mm(data)
        st.subheader("**Selecione o cursinho para as opções de tratamento**")
        curso = st.selectbox("Selecione o cursinho",("Cursos:","Macvest","Macvestinho"))

        if curso == "Macvest":
            image = Image.open('./image/M.png')
            st.image(image,use_column_width=False)
        elif curso == "Macvestinho":
            image = Image.open("./image/m.png")
            st.image(image, use_column_width= False)

        if curso != "Cursos:" and file is not None:
            st.header("Opções de tratamento:")

    #--------------- Verifica Dados MC E MM
            bx0 = st.checkbox("Deseja verificar os dados?",key = 0)
            if bx0 is True:
                st.title("Dados dos candidatos")
                # curso = st.selectbox("Selecione o cursinho",("Cursos:","Macvest","Macvestinho"), key = 00 )
                if curso == "Macvest":
                    st.subheader("Candidatos do Macvest")
                    st.write(Mc)
                    st.markdown(get_table_download_link(Mc,"Mc_database"), unsafe_allow_html=True)
                elif curso == "Macvestinho":
                    st.subheader("Candidatos do Macvestinho")
                    st.write(Mm)
                    st.markdown(get_table_download_link(Mm,"Mm_database"), unsafe_allow_html=True)

    #-----------------Donwload Lista Economica -----------------# 
            bx1 = st.checkbox("Deseja fazer o download da classificação economica?", key = 1)
            if bx1 is True:
                st.title("Classificação Economica")
                # curso = st.selectbox("Selecione o cursinho",("Cursos:","Macvest","Macvestinho"), key = 11)        
                if curso == "Macvest":
                    st.subheader("Classificação do Macvest")
                    mc_list = Es.list_renda(Mc)
                    st.write(mc_list)
                    st.markdown(get_table_download_link(mc_list,"Mc_economico"), unsafe_allow_html=True)
                elif curso == "Macvestinho":
                    st.subheader("Classificação do Macvestinho")
                    mm_list = Es.list_renda(Mm)
                    st.write(mm_list)
                    st.markdown(get_table_download_link(mm_list,"Mm_economico"), unsafe_allow_html=True)

    #---------------Download Lista de documentos ------------------#
            bx2 = st.checkbox("Deseja fazer o download dos links dos documentos?", key = 2)
            if bx2 is True:
                st.title("Entrega de documentos")
                # curso = st.selectbox("Selecione o cursinho",("Cursos:","Macvest","Macvestinho"), key = 22)        
                if curso == "Macvest":
                    st.header("Categoria de entrega")
                    on_pre = st.selectbox("Selecione a categoria:",("Categorias","Entrega online","Entrega presencial"), key = 222)
                    if on_pre == 'Entrega online':
                        st.subheader("Entrega online: Links")
                        entrega_mc = Es.entrega_doc(Mc,"online")
                        st.markdown(get_table_download_link(entrega_mc,"link_doc_mc"), unsafe_allow_html=True)
                    elif on_pre == "Entrega presencial":
                        st.subheader("Entrega presencial: Periodo")
                        entrega_mc = Es.entrega_doc(Mc,"presencial")
                        st.markdown(get_table_download_link(entrega_mc,"periodo_doc_mc"), unsafe_allow_html=True)
                elif curso == "Macvestinho":
                    st.header("Categoria de entrega")
                    on_pre = st.selectbox("Selecione a categoria:",("Entrega online","Entrega presencial"), key = 222)
                    if on_pre == 'Entrega online':
                        entrega_mm = Es.entrega_doc(Mm,"online")
                        st.markdown(get_table_download_link(entrega_mm,"link_doc_mm"), unsafe_allow_html=True)
                    elif on_pre == "Entrega presencial":
                        entrega_mm = Es.entrega_doc(Mm,"presencial")
                        st.markdown(get_table_download_link(entrega_mm,"periodo_doc_mm"), unsafe_allow_html=True)

    #---------------Download Lista Aprovados ------------------#
            bx3 = st.checkbox("Deseja fazer o download da lista de aprovados?", key = 3)
            if bx3 is True:
                st.title("Lista de aprovados")
                # curso = st.selectbox("Selecione o cursinho",("Cursos:","Macvest","Macvestinho"), key = 33)        
                if curso == "Macvest":
                    st.subheader("Basta inserir a planilha de notas dos candidatos Macvest.")
                    st.set_option('deprecation.showfileUploaderEncoding', False)
                    file_mc = st.file_uploader('Arraste a planilha, ou clique em "browse files"', type="xlsx",key = 1)
                    if file_mc is not None:
                        nota = pd.read_excel(file_mc)
                        mc_list = Es.list_renda(Mc)
                        aprov_mc = Es.list_aprov(nota, mc_list)
                        st.write(aprov_mc)
                        st.markdown(get_table_download_link(aprov_mc,"Mc_aprovados"), unsafe_allow_html=True)
                elif curso == "Macvestinho":
                    st.subheader("Basta inserir a planilha de notas dos candidatos Macvestinho.")
                    st.set_option('deprecation.showfileUploaderEncoding', False)
                    file_mm = st.file_uploader('Arraste a planilha, ou clique em "browse files"', type="xlsx",key = 2)
                    if file_mm is not None:
                        nota = pd.read_excel(file_mm)
                        mm_list = Es.list_renda(Mm)
                        aprov_mm = Es.list_aprov(nota, mm_list)
                        st.write(aprov_mm)
                        st.markdown(get_table_download_link(aprov_mm,"Mm_aprovados"), unsafe_allow_html=True)


