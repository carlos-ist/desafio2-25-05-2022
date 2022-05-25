from limpaLista import *
from graficos import barGraph

#https://dadosabertos.tse.jus.br/pt_BR/dataset/pesquisas-eleitorais-atual/resource/3c0e4df8-1e6f-4468-bae1-65aed8c0eac3

fileBuffer = open("pesquisa_eleitoral_2022_RJ.csv", "r")
appFileBuffer = fileBuffer.read()
planilha = appFileBuffer.splitlines()
planilha = [i.replace('"', '') for i in planilha] # remove quote from each element
fileBuffer.close()

print("----- 1 ----- Criação Planilha ---- CONVERSÃO - ARQUIVO EM LISTA")
for i in range(0, len(planilha)):  # 6 itens
    planilha[i] = planilha[i].split(";")

print("----- 2 ----- Impressão Planilha")

imprimiLista(planilha)

print("----- 3 ----- Impressão Primeira Linha")

print()
for i in range(0,len(planilha[0])):
    print(f'Linha 0 - Coluna {i}: {planilha[0][i]}')

print()
print("----- 4 ----- Exclusão colunas desnecessárias da lista")
print()

print(f'Quantidade de colunas: {len(planilha[0])}')
print(f'Quantidade de linhas: {len(planilha)}')

# Deletando todas as Colunas, exceto às que serão usadas para plotar o gráfico.
quantidadeColunas = len(planilha[0])
for i in range(quantidadeColunas-1, -1, -1):
    if i == 11 or i == 16: # Mantendo Colunas 11 - NM_EMPRESA e 19 - QT_ENTREVISTADOS
        pass
    else:
        deletaColuna(planilha, i, len(planilha))

print()
print("----- 5 ----- Dados para Plotagem")
print()

quantidadeEntrevistados = colunaEmLista(planilha, 1)
nomeEmpresas = colunaEmLista(planilha, 0)

print(quantidadeEntrevistados)
print(nomeEmpresas)

print()
print("----- 6 ----- Plot ----- Gráfico bar")
print()


barGraph(
        nomeEmpresas,
        quantidadeEntrevistados,
        "Quantidade de Entrevistados",
        "Nome Empresas",
        "Quantidade de Pessoas Entrevistadas (Amostras) Por Empresas de Pesquisa"
        )












