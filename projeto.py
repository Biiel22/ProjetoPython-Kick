import os, openpyxl
print("===================================================")
print("Dados extraídos do site: http://covid.saude.gov.br/")
print("===================================================")
print("1. Feminino")
print("2. Masculino")
print("3. Outro")
g = input("Qual seu Gênero? \n")
print("======================")

if g == '1':
    print("=============================================================")
    print("Seja bem-vinda ao PythonD!")
    print("Aqui você poderá gerar um relatório do site informado acima")
    print("=============================================================")
elif g == '2':
    print("=============================================================")
    print("Seja bem-vindo ao PythonB!")
    print("Aqui você poderá gerar um relatório do site informado acima")
    print("=============================================================")
else:
    print("=============================================================")
    print("Seja bem-vindo(a) ao PythonB!")
    print("Aqui você poderá gerar um relatório do site informado acima")
    print("=============================================================")





os.system("pause")