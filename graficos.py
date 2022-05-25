import matplotlib.pyplot as plt
import pandas as pd
import squarify

def timeSerieGraph(listaDatas,listaValores):

    plt.plot(listaDatas, listaValores)

    plt.ylabel('Valor das Pesquisas')
    plt.xlabel('Datas')

    plt.title('Investimentos(R$) em Pesquisas Eleitorais Por Período de Tempo')

    plt.show()


def barGraph(
            nomeEmpresas,
            quantidadeEntrevistados,
            nomeY,
            nomeX,
            titulo
            ):

    y = quantidadeEntrevistados
    x = nomeEmpresas
    plt.bar(nomeEmpresas,quantidadeEntrevistados)
    plt.xlabel(nomeX)
    plt.ylabel(nomeY)
    plt.title(titulo)
    plt.show()


def treemapGraph(colunaNomes,colunaValores):

    colunaNomes = {colunaNomes[0]: colunaNomes[1::1]}
#    colunaValores = {colunaValores[0]: colunaValores[1::1]}

    print("from function TREEMAP", colunaValores)  # VR_PESQUISA
    print("from function TREEMAP", colunaNomes)  # NM_EMPRESA

    v = {'nb_people': [20000, 15000, 21500, 176912, 338200, 338200, 88000, 123500, 12000, 123500]}

    squarify.plot(sizes=v['nb_people'], label=colunaNomes['NM_EMPRESA'], alpha=.8)

    plt.axis('off')
    plt.show()
