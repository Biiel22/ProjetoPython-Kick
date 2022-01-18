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

        datas=(estadosCovid['Data'])
        CasosDia=(estadosCovid['Casos por dia'])
        ObitosDia=(estadosCovid['Óbitos por dia'])
        TotalCasos=(estadosCovid['Total de casos'])

        plt.style.use('ggplot')

        plt.ylabel("Total de Casos")
        plt.plot(TotalCasos)
        plt.savefig("TotaldeCasosNosEstados.png")
        plt.close()
        
        relatorio.multi_cell(w=0, h=8, txt="Total de Casos nos Estados", ln=1, align='C')
        relatorio.image(x=20, y=30, w=180, h=80, name='TotaldeCasosNosEstados.png')

    elif opc1 == "2":
        CasosDia=(estadosCovid['Casos por dia'])

        plt.plot(CasosDia)
        plt.ylabel("Casos por Dia")
        plt.savefig("CasosDia.png")
        plt.close()
        
        relatorio.multi_cell(w=0, h=230, txt="Total de Casos por Dia nos Estados", ln=1, align='C')
        relatorio.image(x=20, y=140, w=180, h=80, name='CasosDia.png')

    elif opc1 == "3":
        ObitosDia=(estadosCovid['Óbitos por dia'])

        plt.ylabel("Óbitos por Dia")
        plt.plot(ObitosDia)
        plt.savefig("ObitosDia.png")
        plt.close()
        
        relatorio.multi_cell(w=0, h=30, txt="Total de Óbitos por Dia nos Estados", ln=1, align='C')
        relatorio.image(x=20, y=50, w=180, h=80, name='ObitosDia.png')
        
    elif opc1 == "4":
        continuar = False
        print("Certo. Até mais!")

    else:
        continuar = True
        print("Desculpe. Não consegui te entender. Tente novamente!")

    print("\n")
    print("============================================================")
    print("1. Maior número de casos")
    print("2. Maior número de casos Por Dia")
    print("3. Maior número de óbitos por dia")
    print("4. Maiores números (1, 2, 3)")
    print("5. Sair e gerar Relatório")
    print("============================================================")
    print("\n")

    pergunta_maior_nmr = input("Escolha acima, qual opção incluir em seu relatório: ")
    # Maior número: Total de Casos
    if pergunta_maior_nmr == '1':
        maior = 0
        b = 0
        for a in range(20, len(list(TotalCasos))):
            nmr = list(TotalCasos)[a]
            try:
                nmr = int(list(TotalCasos)[a])
            except:
                nmr = 0
            if(nmr > maior):
                maior = nmr
                b = a
        print("Maior número: Total de Casos")
        print(datas[b])
        print(maior)
    # Maior número: Casos por dia
    elif pergunta_maior_nmr == '2':
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
        print("Maior número: Total de Casos Por Dia")
        print(datas[b])
        print(maior)
    # Maior número: Óbitos por dia
    elif pergunta_maior_nmr == '3':
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
        print("Maior número: Óbitos Por Dia")
        print(datas[b])
        print(maior)

    elif pergunta_maior_nmr == '4':
        # Maior número: Total de Casos
        maiorTotalCasos = 0
        b = 0
        for a in range(20, len(list(TotalCasos))):
            nmr = list(TotalCasos)[a]
            try:
                nmr = int(list(TotalCasos)[a])
            except:
                nmr = 0
            if(nmr > maiorTotalCasos):
                maiorTotalCasos = nmr
                b = a
        print("Maior número: Total de Casos")
        print(datas[b])
        print(maiorTotalCasos)

        # Maior número: Total de Casos por Dia
        maiorCasosDia = 0
        b = 0
        for a in range(20, len(list(CasosDia))):
            nmr = list(CasosDia)[a]
            try:
                nmr = int(list(CasosDia)[a])
            except:
                nmr = 0
            if(nmr > maiorCasosDia):
                maiorCasosDia = nmr
                b = a
        print("Maior número: Total de Casos Por Dia")
        print(datas[b])
        print(maiorCasosDia)

        # Maior número: Óbitos por Dia
        maiorObitosDia = 0
        b = 0
        for a in range(20, len(list(ObitosDia))):
            nmr = list(ObitosDia)[a]
            try:
                nmr = int(list(ObitosDia)[a])
            except:
                nmr = 0
            if(nmr > maiorObitosDia):
                maiorObitosDia = nmr
                b = a
        print("Maior número: Óbitos Por Dia")
        print(datas[b])
        print(maiorObitosDia)


    elif pergunta_maior_nmr == '5':
        continar = False

        # relatorio.output('Relatório COVID-19.pdf')

        # print("\n")
        # print("==============================================")
        # print("Maravilha, PDF gerado. Vamos ver como ficou?")
        # print("==============================================")
        # print("\n")

    else:
        continuar = False
        print("\n")
        print("Reinicie o programa e tente novamente!")
        print("\n")

os.system("pause")