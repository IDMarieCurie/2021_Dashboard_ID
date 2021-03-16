import pandas as pd
import os
import streamlit as st
import datetime


#---------------Importando dados-----------------------------#
# 
#gcp = pd.read_excel("./gcp2.xlsx")

#-----Identificação----#
def concate_int(gcp):
    rp = gcp.iloc[10,2]
    dp = gcp.iloc[11,2]
    np = gcp.iloc[12,2]
    dt = gcp.iloc[10,6].strftime("%d/%m/%Y")
    fq = gcp.iloc[11,6]
    mt = gcp.iloc[12,6]

    

    I = [rp, dp, np, dt, fq, mt]

    I = pd.DataFrame(I)
    I = I.rename({0 : "Cabeçalho"}, axis = 1)
    
    return I

#-----------------------Dados-----------------#
def concate_mate(gcp):
    et  = gcp.iloc[16:36,1].dropna().str.lower()
    mat = gcp.iloc[16:36,3].dropna().str.lower()
    hab = gcp.iloc[16:36,5].dropna().str.lower()
    dif = gcp.iloc[16:36,6].dropna().str.lower()
    nat = gcp.iloc[40,1]

    et = pd.DataFrame(et)
    et.columns = ["Resultados"]
    et.index = pd.RangeIndex(start=0, stop= len(et), step=1)
    
    mat = pd.DataFrame(mat)
    mat.columns = ["Resultados"]
    mat.index = pd.RangeIndex(start=0, stop= len(mat), step=1)
    
    hab = pd.DataFrame(hab)
    hab.columns = ["Resultados"]
    hab.index = pd.RangeIndex(start=0, stop= len(hab), step=1)
    
    dif = pd.DataFrame(dif)
    dif.columns = ["Resultados"]
    dif.index = pd.RangeIndex(start=0, stop= len(dif), step=1)
    
    et  =  et.rename({"Resultados" : "Etapas"},         axis = 1)
    dif = dif.rename({"Resultados" : "Dificuldades"},   axis = 1)
    mat = mat.rename({"Resultados" : "Materiais"},      axis = 1)
    hab = hab.rename({'Resultados' : 'Habilidades'},    axis = 1)
    nat = pd.Series(nat)


    M = [et, mat, hab, dif, nat]
    M = pd.concat(M, ignore_index = False, axis = 1)
    M = pd.DataFrame(M)
    M = M.rename({0 : "Descrição e Notas"}, axis = 1)
    

    return M



#--------------------- Criando Diretorios---------------------#
#-------------------- Salvando Banco de Dados ---------#
def bank(gcp,dps):
    I = concate_int(gcp)
    M = concate_mate(gcp)

    uni = pd.concat([I,M], ignore_index = False, axis= 1)
    date = gcp.iloc[10,6]
    mes = date.strftime("%B")

    raiz = "./Data" 
    dire_dp = raiz + "/{}/{}".format(mes,dps)
    dire_arq = dire_dp + "/{}".format(str(I.iloc[2,0]) ) + "-" +str(I.iloc[0,0])
     #Identifica Macv Macvestinho

    if not os.path.exists(dire_dp):
        os.makedirs(dire_dp)
    if not os.path.exists(dire_arq):    
        uni.to_csv(dire_arq, index = False)
    return uni
# inte = concate_int(gcp)
# mate = concate_mate(gcp)
