import os
import pandas as pd
import openpyxl as plt
import matplotlib.pyplot as plt
import subprocess
from fpdf import FPDF

# Config pdf
relatorio = FPDF('p', 'mm', 'A4')
relatorio.add_page()
relatorio.set_font('times', '', 16)

print("===================================================")
print("Dados extraídos do site: https://www.seade.gov.br/")
print("===================================================")

print("=============================================================")
print("Não altere o nome do arquivo!")
print("Por precaução, verifique se o arquivo .xlsx está nomeado: ")
print("covid_estado.xlsx")
print("=============================================================")

imagem = 'passo_a_passo_diretorio.pdf'
subprocess.Popen([imagem], shell=True)

diretorio=input("Insira o diretório do arquivo conforme exemplo: ")

print("==============================================================")

estadosCovid = pd.read_excel(diretorio+str("\covid_estado.xlsx"))

datas=(estadosCovid['Data'])
CasosDia=(estadosCovid['Casos por dia'])
ObitosDia=(estadosCovid['Óbitos por dia'])
TotalCasos=(estadosCovid['Total de casos'])

def TotalCasosPorDia():
    plt.ylabel("Casos por Dia")
    plt.plot(CasosDia)
    plt.savefig("CasosDia.png")
    plt.close()

def TotalDeCasos():
    plt.ylabel("Total de Casos")
    plt.plot(TotalCasos)
    plt.savefig("TotaldeCasosNosEstados.png")
    plt.close()

def TotalDeObitos():
    plt.ylabel("Óbitos por Dia")
    plt.plot(ObitosDia)
    plt.savefig("ObitosDia.png")
    plt.close()

# Dia com maior número
def MaiorNCasos():
    maior = 0
    b = 0
    for a in range(20, len(list(TotalCasos))):
        nmr = list(TotalCasos)[a]
        try:
            nmr = int(list(TotalCasos)[a])
        except:
            nmr = 0
        if(int(nmr) > int(maior)):
            maior = nmr
            b = a
        maiorNcasos = str(maior) + ' - ' +str(datas[b])
    relatorio.multi_cell(w=190, h=8, txt="Dia que houve o maior números de casos", ln=1, align='C')
    relatorio.multi_cell(w=190, h=8, txt=maiorNcasos, ln=1, align='C')

def MaiorNCasosPorDia():
    maior = 0
    b = 0
    for a in range(20, len(list(CasosDia))):
        nmr = list(CasosDia)[a]
        try:
            nmr = int(list(CasosDia)[a])
        except:
            nmr = 0
        if(nmr > maior):
            maior = nmr
            b = a
        maiorNcasosDia = str(maior) + ' - ' +str(datas[b])
    relatorio.multi_cell(w=190, h=8, txt="Dia que houve o maior números de casos Por Dia", ln=1, align='C')
    relatorio.multi_cell(w=190, h=8, txt=maiorNcasosDia, ln=1, align='C')

def MaiorNObitosPorDia():
    maior = 0
    b = 0
    for a in range(20, len(list(ObitosDia))):
        nmr = list(ObitosDia)[a]
        try:
            nmr = int(list(ObitosDia)[a])
        except:
            nmr = 0
        if(nmr > maior):
            maior = nmr
            b = a
        maiorNobitosDia = str(maior) + ' - ' +str(datas[b])
    relatorio.multi_cell(w=190, h=8, txt="Dia que houve o maior números de Óbitos Por Dia", ln=1, align='C')
    relatorio.multi_cell(w=190, h=8, txt=maiorNobitosDia, ln=1, align='C')

print("==========Sobre a COVID-19==========")
print("1. Total de Casos nos Estados")
print("2. Casos por dia")
print("3. Óbitos por dia")
print("4. Dados gerais")
print("5. Sair")
print("====================================")

opc1 = str(input("Deseja visualizar o gráfico de qual opção acima: "))
if opc1 == "1":
    TotalDeCasos()
    
    relatorio.multi_cell(w=0, h=8, txt="Total de Casos nos Estados", ln=1, align='C')
    relatorio.image(x=20, y=30, w=180, h=80, name='TotaldeCasosNosEstados.png')
    relatorio.multi_cell(w=0, h=8, txt='\n\n\n\n\n\n\n\n\n\n\n\n', ln=1, align='C')

    MaiorNCasos()

elif opc1 == "2":
    TotalCasosPorDia()
    
    relatorio.multi_cell(w=0, h=8, txt="Total de Casos por Dia nos Estados", ln=1, align='C')
    relatorio.image(x=20, y=30, w=180, h=80, name='CasosDia.png')
    relatorio.multi_cell(w=0, h=8, txt='\n\n\n\n\n\n\n\n\n\n\n\n', ln=1, align='C')

    MaiorNCasosPorDia()

elif opc1 == "3":
    TotalDeObitos()
    
    relatorio.multi_cell(w=0, h=8, txt="Total de Óbitos por Dia nos Estados", ln=1, align='C')
    relatorio.image(x=20, y=30, w=180, h=80, name='ObitosDia.png')
    relatorio.multi_cell(w=0, h=8, txt='\n\n\n\n\n\n\n\n\n\n\n\n', ln=1, align='C')

    MaiorNObitosPorDia()
    
elif opc1 == "4":
    # Total de casos em geral
    TotalDeCasos()
    
    relatorio.multi_cell(w=0, h=8, txt="Total de Casos nos Estados", ln=1, align='C')
    relatorio.image(x=20, y=30, w=180, h=80, name='TotaldeCasosNosEstados.png')
    relatorio.multi_cell(w=0, h=8, txt='\n\n\n\n\n\n\n\n\n\n\n\n', ln=1, align='C')

    MaiorNCasos()

    # Total de casos por dia
    TotalCasosPorDia()
    
    relatorio.multi_cell(w=0, h=8, txt="Total de Casos por Dia nos Estados", ln=1, align='C')
    relatorio.image(x=20, y=140, w=180, h=80, name='CasosDia.png')
    relatorio.multi_cell(w=0, h=8, txt='\n\n\n\n\n\n\n\n\n\n', ln=1, align='C')

    MaiorNCasosPorDia()

    # Total de obitos por dia
    TotalDeObitos()
    
    relatorio.add_page()
    relatorio.multi_cell(w=0, h=8, txt="Total de Óbitos por Dia nos Estados", ln=1, align='C')
    relatorio.image(x=20, y=30, w=180, h=80, name='ObitosDia.png')
    relatorio.multi_cell(w=0, h=8, txt='\n\n\n\n\n\n\n\n\n\n\n\n', ln=1, align='C')

    MaiorNObitosPorDia()

    relatorio.output('Relatório COVID-19.pdf')

    print("\n")
    print("===============================================")
    print("1. Link do relatório")
    print("2. Abrir relatório")
    print("===============================================")
    rel_finalizado = input("Maravilha, PDF gerado. Escolha uma opção acima: ")
    print("===============================================")
    print("\n")

    if rel_finalizado == '1':
        print(diretorio+r'\Relatório COVID-19.pdf')
        
        print("\n")
        print("===========================================")
        print("Ótimo!")
        print("Copie selecionando o diretório")
        print("Em seguida clique com o Botão Direito")
        print("Cole em seu navegador.")
        print("===========================================")
        print("\n")

    elif rel_finalizado == '2':
        relat = 'Relatório COVID-19.pdf'
        subprocess.Popen([relat], shell=True)

        print("Relatório aberto! Até mais :)")
        print("\n")

elif opc1 == "5":
    print("Certo. Até mais!")

else:
    print("Desculpe. Não consegui te entender. Tente novamente!")



os.system("pause")