#Essa lógica foi feita por https://github.com/thiagomel0
from csv import DictReader
from preenchedorDeSQL import preencher

def formataTexto(arquivo,text):
  file1 = open(arquivo,'a',encoding='utf-8')
  file1.write(text)
  file1.close



with open('vinhos.csv', encoding='utf-8') as vinhos:
  reader = DictReader(vinhos)

  colunas = []
  dados = []
  linhas = []
  for linha in reader:
    for coluna in linha.keys():
      colunas.append(coluna)

    for dado in linha.values():
      if dado == None:
        dado = 'null'

      dados.append(dado)

    insert = preencher('vinhos',colunas,dados)
    formataTexto('test.sql',insert + '\n')
    colunas.clear()
    dados.clear()
  
        
      


  
  
  
    


