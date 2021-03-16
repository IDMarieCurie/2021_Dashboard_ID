import pandas as pd

        # Tratamento dos dados 

def trata_id (df):

    ddc = {
                    # Hora
    "Carimbo de data/hora"                   : "data/hora",
# ---------------------------------------------------------------------------------------

                    # identificação 
    "Endereço de e-mail"                     : "email",
    "Nome completo:"                         : "nome",
    "Data de Nascimento:"                    : "nascimento",
    "Registro Geral (RG)"                    : "rg",
    "Órgão expedidor - UF"                   : "uf",
    "CPF:"                                   : "cpf",
    "Celular: "                              : "cell",
# ---------------------------------------------------------------------------------------

                    # cursinhos                                                         
    "Selecione o cursinho inscrito:"                                : "curso",
    "Já prestou outro vestibular da Marie Curie? Se sim, qual?"     : "ex_candidato",
    "Já prestou outro vestibular de cursinhos? Se sim, qual?"       : "preparatorios",
# ---------------------------------------------------------------------------------------

                    # sobre você        
    "Estado civil:"                            : "estado_civil",
    "Naturalidade:"                            : "naturalidade",
    "Orientação Sexual:"                       : "orientacao_sexual",
    "Cor/Raça:"                                : "cor/raca",
    "Possui alguma deficiência? Se sim, qual?" : "name_deficiencia",
# ---------------------------------------------------------------------------------------

                    # Filiação  
    "Nome do responsável 1:"        : "name_respo1",
    "Idade do responsável 1:"       : "idade_respo1",
    "Profissão do responsável 1:"   : "prof_respo1",
    "Nome do responsável 2:"        : "name_respo2",
    "Idade do responsável 2:"       : "idade_respo2",
    "Profissão do responsável 2:"   : "prof_respo2",
    "Nome do responsável 3:"        : "name_respo3",
    "Idade do responsável 3:"       : "idade_respo3",
    "Profissão do responsável 3:"   : "prof_respo3",
    "Nome do responsável 4:"        : "name_respo4",
    "Idade do responsável 4:"       : "idade_respo4",
    "Profissão do responsável 4:"   : "prof_respo4",
    "Nome do responsável 5:"        : "name_respo5",
    "Idade do responsável 5:"       : "idade_respo5",
    "Profissão do responsável 5:"   : "prof_respo5",
    "Nome do responsável 6:"        : "name_respo6",
    "Idade do responsável 6:"       : "idade_respo6",
    "Profissão do responsável 6:"   : "prof_respo6",
    "Nome do responsável 7:"        : "name_respo7",
    "Idade do responsável 7:"       : "idade_respo7",
    "Profissão do responsável 7:"   : "prof_respo7",
    "Nome do responsável 8:"        : "name_respo8",
    "Idade do responsável 8:"       : "idade_respo8",
    "Profissão do responsável 8:"   : "prof_respo8",
    "Nome do responsável 9:"        : "name_respo9",
    "Idade do responsável 9:"       : "idade_respo9",
    "Profissão do responsável 9:"   : "prof_respo9",
    "Nome do responsável 10:"       : "name_respo10",
    "Idade do responsável 10:"      : "idade_respo10",
    "Profissão do responsável 10:"  : "prof_respo10",
# ---------------------------------------------------------------------------------------

                    # Renda total da filiação
    "Renda mensal salarial total dos responsáveis:" : "renda_respo",
# ---------------------------------------------------------------------------------------

                    # Moradia
    "Selecione sua cidade:"         : "cidade",
    "Bairro:"                       : "bairro",
    "Endereço:"                     : "endereco",
    "Complemento:"                  : "complemento",
# ---------------------------------------------------------------------------------------

                    # Profissional e academico

            # profissional
    "Trabalha? Se sim, qual seu trabalho?"      : "trabalho",
    "Qual sua jornada de trabalho?"             : "jornada_trabalho",
    "Deslocamento até o trabalho:"              : "deslocamento",
    "Valor do salário recebido: "               : "salario",

            # academico
    "Ano em que concluiu a escola? "                                    : "fim_escola",
    "Está cursando a escola ? Se sim, qual série?"                      : "serie_escola",
    "Categoria da escola cursada:"                                      : "tipo_escola",
    "Recebe bolsa estudantil ? Se sim, qual?"                           : "bolsa_escola",
    "Nome da escola:"                                                   : "nome_escola",
    'Área  de interesse acadêmico: '                                    : "area_estudo",
    "Qual curso pretende fazer? (Ex: Matemática, Física, História)"     : "curso_estudo",
# ---------------------------------------------------------------------------------------

                    # Programa de renda
    "Quantos moradores há na sua casa?"                                 : "qta_morador",
    "Quantos trabalham?"                                                : "qta_trabalha",
    "Recebe algum programa de transferência de renda? Se sim, quais?"   : "renda_programa",
    "Qual valor total recebido pelos programas?"                        : "valor_programa",
# ---------------------------------------------------------------------------------------

                    # Acesso as aulas
    "Quantos dispositivos eletrônicos há na sua casa?"                  : "qta_dispositivos",
    "Qual seu tipo de acesso a internet:"                               : "tipo_internet",
# ---------------------------------------------------------------------------------------

                    # Entrega Docs
    "Deseja entregar os documentos agora ou presencialmente ?"          : "entrega_doc",
                                                
            # Online
    "Copia do Registro Geral (RG)"                                      : "link_rg",
    "Histórico escolar ou comprovante de matricula:"                    : "link_historico",
    "Comprovante de renda:"                                             : "link_renda",
    "Comprovante de endereço:"                                          : "link_endereco",
    "Carteira de trabalho:"                                             : "link_trabalho",

        # presencial                                        
    "Selecione o período em que irá comparecer:"                        : "periodo_doc",
# ---------------------------------------------------------------------------------------

                    # Confirma
    "Concorda com a declaração de veracidade?"                          : "termo_juridico"
    }

    data = df.rename(columns = ddc)
    
    l = []
    ll = []
    lll = []

    for i in data["rg"]:
        t0 = str(i)
        t1 = t0.replace(".","")
        t2 = t1.replace("-","")
        t3 = t2.replace(" ","")
        l.append(t3)
    for i in data["cpf"]:
        t0 = str(i)
        t1 = t0.replace(".","")
        t2 = t1.replace("-","")
        t3 = t2.replace(" ","")
        ll.append(t3)
    for i in data["cell"]:
        t0 = str(i)
        t1 = t0.replace("(", "")
        t2 = t1.replace(")", "")
        t3 = t2.replace(" ", "")
        t4 = t3.replace("-", "")
        lll.append(t4)

    rg   = pd.DataFrame(l,   columns = ["rg"]  )
    cpf  = pd.DataFrame(ll,  columns = ["cpf"] )
    cell = pd.DataFrame(lll, columns = ["cell"])

    data = data.drop(columns = ["rg","cpf","cell"])
    data = pd.concat([rg,cpf,cell,data], ignore_index= False, axis = 1)


        # Definição do codigo do aluno
    data.index = data['rg']
    data.index.name = "id"

    # data = data.drop_duplicates(subset = ["id"], keep = 'first')
    return data

def mc_mm(data):
    Mcc = data[(data['curso'] == "Macvest")].index
    Mmm = data[(data["curso"] == "Macvestinho")].index

    Mc = pd.DataFrame(data.drop(Mmm))
    Mm = pd.DataFrame(data.drop(Mcc))
    return Mc, Mm




# Estatistica de renda e lista de aprovados

# nota = pd.read_excel("./notas.xlsx")

def list_renda(data):
    renda_respo = data["renda_respo"]
    salario = data["salario"]
    program = data["valor_programa"]

    renda_total = renda_respo + salario + program
    renda_total = pd.DataFrame(renda_total, columns = ["renda_total"])

    mm = data['qta_morador']

    percap = pd.concat([renda_total,mm], axis = 1, ignore_index= False)
    percap["renda/morador"] = percap["renda_total"] / mm
    
    percap['class_economica(%)'] = (1 - percap["renda/morador"]/1650.0)*100
    
    percap = percap.sort_values(by = ["class_economica(%)"], ascending = False)
    
    l = []
    name = data["nome"].to_dict()

    for i in percap.index:
        if i in data["nome"].index:
            l.append(name[i])
    percap["nome"] = pd.DataFrame(l,index = percap.index, columns = ["Nome"])

    return percap

def list_aprov(nota,percap):
    # 0.65 -> percap
    # 0.25 -> nota
    ddn = {
    "Registro Geral(RG)"     : "rg",
    "Nota da prova"          : "nota"
    }

    nota = nota.rename(columns = ddn)


    l = []
    for i in nota["rg"]:
        t0 = str(i)
        t1 = t0.replace(".","")
        t2 = t1.replace("-","")
        t3 = t2.replace(" ","")
        l.append(t3)

    nt = pd.DataFrame(nota["nota"], columns = ["nota"])
    nt.index = l
    nt.index.name = "id"

    
    quadro = pd.concat([percap,nt], axis = 1, ignore_index= False)
    quadro['aprov'] = quadro["class_economica(%)"]*0.65 + quadro["nota"]*0.25
    quadro = quadro.sort_values(by = ["aprov"], ascending = False)

    return quadro

                # Avaliações # 

#  Ficha de identificação

ficha = ["nome","email","nascimento","rg","uf","cpf","cell"]

# antecedentes de cursinhos
curso = ["curso","ex_candidato","preparatorios"]

# Caracteristicas pessoais
pessoal = ["estado_civil","naturalidade","orientacao_sexual","cor/raca","name_deficiencia"]


# Filiações
fila_nome  = ["name_respo1","name_respo2","name_respo3","name_respo4","name_respo5","name_respo6","name_respo7","name_respo8","name_respo9","name_respo10"]
fila_idade = ["idade_respo1","idade_respo2","idade_respo3","idade_respo4","idade_respo5","idade_respo6","idade_respo7","idade_respo8","idade_respo9","idade_respo10"]
fila_prof  = ["prof_respo1","prof_respo2","prof_respo3","prof_respo4","prof_respo5","prof_respo6","prof_respo7","prof_respo8","prof_respo9","prof_respo10"]
fila_renda = ["renda_respo"]

# Moradia
moradia = ["cidade","bairro","endereco","complemento"]

# academico
acad    = ["fim_escola","serie_escola","bolsa_escola","nome_escola","area_estudo","curso_estudo"]

# profissional
trampo  =  ['trabalho',"jornada_trabalho","deslocamento","salario"]

# Programa de renda
program_renda = ["qta_morador","qta_trabalha","renda_programa","valor_programa"]

# acesso as aulas
internet = ["qta_dispositivos","tipo_internet"]

# Documentação
doc_entrega = ["entrega_doc"]

# entrega online
link_doc = ["link_rg","link_historico","link_renda","link_endereco","link_trabalho"]

# entrega pessoal
periodo_doc = ["periodo_doc"]

# termo juridico
term_juri = ["termo_juridico"]

def colect_plan (Data, lista):
    l  = []
    for i in lista:
        l.append(Data[i])

    t0 = pd.concat(l, axis = 1, ignore_index= False)
    return t0

# Ficha           = colect_plan(data,ficha)
# Curso           = colect_plan(data,curso)
# Pessoal         = colect_plan(data,pessoal)
# Fila_nome       = colect_plan(data,fila_nome)
# Fila_idade      = colect_plan(data,fila_idade)
# Fila_renda      = colect_plan(data,fila_renda)
# Moradia         = colect_plan(data,moradia)
# Academico       = colect_plan(data,acad)
# Profissional    = colect_plan(data,trampo)
# Programa_renda  = colect_plan(data,program_renda)
# Internet        = colect_plan(data,internet)
# Doc_entrega     = colect_plan(data,doc_entrega)
# Link_doc        = colect_plan(data,link_doc)
# Periodo_doc     = colect_plan(data,periodo_doc)
# Termo_juri      = colect_plan(data,term_juri)



#  Contabilizações
def count_value(data, colum):
    value = data[colum].value_counts(dropna = False)
    return value
