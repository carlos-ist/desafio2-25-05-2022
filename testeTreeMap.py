from limpaLista import *
from graficos import treemapGraph


fileBuffer = open("pesquisa_eleitoral_2022_RJ.csv", "r")
appFileBuffer = fileBuffer.read()
planilha = appFileBuffer.splitlines()
planilha = [i.replace('"', '') for i in planilha] # remove quote from each element
fileBuffer.close()

print("----- 1 ----- Criação Planilha ---- CONVERSÃO EM LISTA")
for i in range(0, len(planilha)):  # 6 itens
    planilha[i] = planilha[i].split(";")


novaPlanilha = planilha.copy()

print("----- 2 ----- Impressão Planilha")
print()
imprimiLista(planilha)
print()

print("----- 3 ----- Impressão Primeira Linha")
print()

for i in range(0,len(planilha[0])):
    print(f'Linha 0 - Coluna {i}: {planilha[0][i]}')

print()
print("----- 4 ----- Exclusão colunas desnecessárias da lista")
print()

print("------------------------------------------")
print(f'Quantidade de colunas: {len(planilha[0])}')
print(f'Quantidade de linhas: {len(planilha)}')
print("------------------------------------------")

# Deletando todas as Colunas, exceto às que serão usadas para plotar o gráfico.
quantidadeColunas = len(planilha[0])
for i in range(quantidadeColunas-1, -1, -1):
    if i == 11 or i == 19: # Mantendo Colunas
        pass
    else:
        deletaColuna(planilha, i, len(planilha))

imprimiLista(planilha)

print()
print("----- 5 ----- Dados para Plotagem")
print()

nomeEmpresas = colunaEmLista(planilha, 0)
valorPagoPelaPesquisa = colunaEmLista(planilha, 1)

print(valorPagoPelaPesquisa)
#intValorPagoPelaPesquisa = []
#for valor in valorPagoPelaPesquisa:
#    intValorPagoPelaPesquisa.append(int(valor))


#Preparando para o Treemap
nomeEmpresas.insert(0, "NM_EMPRESA")
#valorPagoPelaPesquisa.insert(0, "VR_PESQUISA")


print(valorPagoPelaPesquisa)
print(nomeEmpresas)

print()
print("----- 6 ----- Plot ----- Gráfico bar")
print()

treemapGraph(nomeEmpresas, valorPagoPelaPesquisa)
