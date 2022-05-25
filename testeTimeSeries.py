from limpaLista import *
from graficos import timeSerieGraph

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

print(f'Quantidade de colunas: {len(planilha[0])}')
print(f'Quantidade de linhas: {len(planilha)}')


# Deletando todas as Colunas, exceto às que serão usadas para plotar o gráfico.
quantidadeColunas = len(planilha[0])
for i in range(quantidadeColunas-1, -1, -1):
    if i == 15 or i == 19: # Mantendo Colunas 15 - DT_FIM_PESQUISA e 19 - VR_PESQUISA
        pass
    else:
        deletaColuna(planilha, i, len(planilha))

imprimiLista(planilha)

print()
print("----- 5 ----- Dados para Plotagem")
print()


colunaValor = colunaEmLista(planilha, 1)
colunaData = colunaEmLista(planilha, 0)

print()
print("----- 6 ----- Formatando Datas")
print()

colunaData = formantandoDatas(colunaData)

print(colunaData)

print()
print("----- 7 ----- Plot ----- Gráfico Série Temporal")
print()

timeSerieGraph(colunaData, colunaValor)



fileBuffer.close()


'''
# Giving title to the chart using plt.title
plt.title('Classes by Date')
 
# rotating the x-axis tick labels at 30degree
# towards right
plt.xticks(rotation=30, ha='right')
'''