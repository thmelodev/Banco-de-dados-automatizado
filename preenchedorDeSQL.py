
#Esse arquivo foi feito por https://github.com/luismiguwl

def tratarDados(dados: list):
	for indice, dado in enumerate(dados):
		if dado == 'null':
			dados[indice] = dado
		elif dado.isdigit():
			dados[indice] = str(dado)
		else:
			dados[indice] = f'"{dado}"'

	return dados


def preencher(tabela: str, colunas: list, dados: list) -> str:
	colunas = ', '.join(colunas)		
	dados = ', '.join(tratarDados(dados))


	return f'INSERT INTO {tabela} ({colunas}) VALUES ({dados});'
