import os
import pandas as pd
import openpyxl as plt
import matplotlib.pyplot as plt
from fpdf import FPDF

# Config pdf
relatorio = FPDF('p', 'mm', 'A4')
relatorio.add_page()
relatorio.set_font('times', '', 16)

print("===================================================")
print("Dados extraídos do site: https://www.seade.gov.br/")
print("===================================================")

print("=============================================================")
print("Seja bem-vindo(a) ao PythonB!")
print("Aqui você poderá gerar um relatório de dados sob uma planilha")
print("=============================================================")

continuar = True

while continuar == True:
    print("==========Sobre a COVID-19==========")
    print("1. Total de Casos nos Estados")
    print("2. Casos por dia")
    print("3. Óbitos por dia")
    print("4. Sair")
    print("====================================")

    opc1 = str(input("Deseja visualizar o gráfico de qual opção acima: "))
    if opc1 == "1":
        estadosCovid = pd.read_excel(r"C:\Users\gagav\Desktop\ATIVIDADES KICK\Phyton\PROJETO PYTHON\ProjetoPython-Kick\covid_estado.xlsx")

        TotalCasos=(estadosCovid['Total de casos'])

        plt.style.use('ggplot')

        plt.ylabel("Total de Casos")
        plt.plot(TotalCasos)
        plt.savefig("TotaldeCasosNosEstados.png")
        plt.close()
        
        relatorio.multi_cell(w=0, h=8, txt="Total de Casos nos Estados", ln=1, align='C')
        relatorio.image(x=20, y=30, w=180, h=80, name='TotaldeCasosNosEstados.png')
        print("\n")
        print("==============================================")
        print("Maravilha, PDF gerado. Vamos ver como ficou?")
        print("==============================================")
        print("\n")

    elif opc1 == "2":
        CasosDia=(estadosCovid['Casos por dia'])

        plt.plot(CasosDia)
        plt.ylabel("Casos por Dia")
        plt.savefig("CasosDia.png")
        plt.close()
        
        relatorio.multi_cell(w=0, h=230, txt="Total de Casos por Dia nos Estados", ln=1, align='C')
        relatorio.image(x=20, y=140, w=180, h=80, name='CasosDia.png')
        print("\n")
        print("==============================================")
        print("Maravilha, PDF gerado. Vamos ver como ficou?")
        print("==============================================")
        print("\n")

    elif opc1 == "3":
        ObitosDia=(estadosCovid['Óbitos por dia'])

        plt.ylabel("Óbitos por Dia")
        plt.plot(ObitosDia)
        plt.savefig("ObitosDia.png")
        plt.close()
        
        relatorio.multi_cell(w=0, h=30, txt="Total de Óbitos por Dia nos Estados", ln=1, align='C')
        relatorio.image(x=20, y=50, w=180, h=80, name='ObitosDia.png')
        print("\n")
        print("==============================================")
        print("Maravilha, PDF gerado. Vamos ver como ficou?")
        print("==============================================")
        print("\n")

    elif opc1 == "4":
        continuar = False
        print("Certo. Até mais!")

    else:
        continuar = True
        print("Desculpe. Não consegui te entender. Tente novamente!")

relatorio.output('Relatório COVID-19.pdf')

os.system("pause")