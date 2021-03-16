import streamlit as st
import pandas as pd
import importlib
import os
import datetime
import base64

from PIL import Image
from gcp_dados import bank
# from os.path import "./Data/", join


def surp(dp):
    if dp == "Ensino-Pedagogico" or dp == "Pedagogico-Social":
        dp_mm = st.sidebar.selectbox("Selecione um curso:",("Cursinho:","Macvest", "Macvestinho"))
        
        if dp_mm == "Macvest":
        
            image = Image.open('./image/M.png')
            st.sidebar.image(image)
            dp = dp + ": " + dp_mm
            st.title(dp)
            fun(dp)
        elif dp_mm =="Macvestinho":
            image = Image.open('./image/m.png')
            st.sidebar.image(image)
            dp = dp + ": " + dp_mm
            st.title(dp)    
            fun(dp)
        else:
            st.write("Cursinho não selecionado!")
    
    elif dp == "Departamentos:":
        
        image = Image.open("./image/logos.png")
        st.image(image, use_column_width= False)
        st.title("SERVIÇO INDISPONIVEL NO MOMENTO: Manutenção")
        st.subheader("---------------------------------------------------------------------------------------")
        st.title("Gestão de conhecimentos")
        st.header("Eixos do conhecimento")
        st.write("Para uma visão mais ampla dos processos empregados nas tarefas da instituição. A gestão de conhecimento traz uma nova perspectiva de acompanhar seus maiores aprendizados e dificuldades no decorrer do voluntariado. Os eixos do conhecimento nos dá a oportunidade de mapear toda uma persona da instituição, verificando oportunidades e gargalos de uma educação de qualidade.")
        st.subheader("Etapas do processo:")
        st.write("O passo a passo de um tarefa do dia a dia pode ser um trabalho repetitivo ou até mesmo árduo. Tabela-lo de uma forma mais visível e objetiva pode vir a calhar quando o assunto é dificuldades na aplicação de certos conhecimentos.  Deste modo, especificar as **etapas** de um processo do início ao fim desperta uma visão mais ampla de toda uma cadeia de habilidades e dificuldades.")
        st.subheader("Habilidades do processo:")
        st.write("Habilidades vão desde movimentos mecânicos simples, como levantar um copo, a voar como um trapezista de um circo. Há também habilidades cognitivas de diversos espectros como um ouvido absoluto ou uma lógica matemática abismal. Todas as formas de desenvolvimento aplicado são potenciais a serem explorado.  Dessa forma, a categoria **Habilidades** visa identificar suas habilidades que estão em constante aplicação. Para que dessa forma possamos gerar oportunidades de aperfeiçoamento. ")
        st.subheader("Materiais do processo:")
        st.write("Seja uma máquina de teletransporte ou chinelos, todos são ferramentas úteis a alguma tarefa. Ao caminhar sobre o vale dos conhecimentos, chinelos podem vir a calhar. Sendo assim, todo **material**, seja ele essencial ou não, mas utilizado no decorrer do processo, é uma fonte em potencial para descobrir oportunidades e gargalos.Lista-los de forma objetiva é uma estratégia para uma gestão pessoal.")
        st.subheader("Dificuldades do processo:")
        st.write("As dificuldades são velhos conhecidos de diferentes alegrias e tristezas. Seja para abrir um rubro vinho ou se espetar em um velho espinho. Muitas dessas antíteses passamos na vida, de forma que listá-las é uma visão interessante de objetificar e externalizar aquilo que estamos trabalhando para superar. As **dificuldades** do processo visa um entendimento maior das barreiras enfrentadas para a resolução de uma tarefa.Desse modo, a criação de oportunidades para um desenvolvimento profissional e pessoal possa ser muito mais focalizado e objetivo.")
        st.header("")

    else:
        st.title(dp)        
        fun(dp)





def fun(dp):
    op = st.selectbox("Selecione a função desejada:",("Opções:","Enviar relatorio GCP","Verificação de processos"))
    if op == "Enviar relatorio GCP":
        armazena(dp)
    elif op == "Verificação de processos":
        verifica(dp)
     

def armazena(dp):
    st.set_option('deprecation.showfileUploaderEncoding', False)
    file = st.file_uploader('Arraste a planilha, ou clique em "browse files"', type="xlsx")
    
    if file is not None:
        gcp = pd.read_excel(file)
        # but = st.checkbox("Deseja verificar seus dados?")
        uni = bank(gcp,dp)
        st.table(uni[["Cabeçalho","Etapas","Materiais","Dificuldades"]])
        st.table(uni["Descrição e Notas"].dropna())
        st.write("Registrado! ID agradece!")
        file.close()
    else:
        st.write("Arquivo ou extensão não encontrados")




def verifica(dp):
    # mes = st.
    lista = os.listdir('./Data/')
    # st.title("Departamento: " + dp)
    nm = st.selectbox("Selecione o mês:",lista)
    
    if nm is not None:  
        lista1 = os.listdir('./Data/{}/{}'.format(nm,dp))
        arq = st.selectbox("Selecione o relatorio:", lista1) 
        p = pd.read_csv("./Data/{}/{}/{}".format(nm,dp,arq))
        

    if p is not None:
        data = p.iloc[3,0]
        Freq = p.iloc[4,0]
        met = p.iloc[5,0]
        datas = {"Data" : [str(data)],
                "Frequencia": [str(Freq)],
                "Metodo" : [str(met)]}  
        df = pd.DataFrame(datas, columns= ["Data","Frequencia","Metodo"])
        st.write(df)
    
    res = pd.DataFrame()

    ets = st.checkbox("Verificar : Etapas")
    if ets:
        ets = p["Etapas"]
        res = pd.concat([res, pd.DataFrame(ets).dropna()],axis = 1, ignore_index = False)

    mat = st.checkbox("Verificar : Materiais")
    if mat:
        mat = p["Materiais"]
        res = pd.concat([res,pd.DataFrame(mat).dropna()], axis = 1, ignore_index= False)

    hab = st.checkbox("Verificar : Habilidades")
    if hab:
        hab = p["Habilidades"]
        res = pd.concat([res, pd.DataFrame(hab).dropna()], axis = 1, ignore_index = False)

    dif = st.checkbox("Verificar : Dificuldades")
    if dif:
        dif = p["Dificuldades"]
        res = pd.concat([res,pd.DataFrame(dif).dropna()], axis = 1, ignore_index = False)

    nat = st.checkbox("Verificar : Notas")
    if nat:
        nats = p["Descrição e Notas"]
        nats = pd.DataFrame(nats).dropna()

    if st.button("Verificar"):
        st.write(res)
        if nat:
            st.table(nats)
            res = pd.concat([res,nats], axis= 1, ignore_index = False)
    st.markdown(downloader(p),unsafe_allow_html=True)

def downloader(df: pd.DataFrame):
    csv = df.to_csv(index=True)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f"<a href='data:file/csv;base64,{b64}'>Download file .csv</a>"
    return href