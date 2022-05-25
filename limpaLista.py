import datetime

def deletaColuna(lista,indiceColuna,quantidadeLinhas):

    print()
    print(f"Quantidade de colunas:{len(lista[0])}")
    print(f'Coluna informada: {indiceColuna} - {lista[0][indiceColuna]}')

#    for i in range(0,quantidadeLinhas):
#        lista[i][indiceColuna]=None

    for i in range(0,quantidadeLinhas):
        lista[i].pop(indiceColuna)

def imprimiLista(lista):

    print()
    i = 0
    for linha in lista:
        print(f' Linha {i}: {linha}')
        i = i + 1

def imprimiColuna(lista, indiceColuna):

    try:
        for linha in lista:
            print(linha[indiceColuna])

    except IndexError: #IndexError: list index out of range
        print("O indice da coluna informado não consta na planilha, tente novamente.")

def colunaEmLista(lista,indiceColuna):

    listaCopia = lista.copy()
    ColunaLista = []

    #Removendo Título da Coluna
    listaCopia.pop(0)

    #print(listaCopia[0])

    for linha in listaCopia:
        ColunaLista.append(linha[indiceColuna])

    return ColunaLista


def formantandoDatas(listaDatas):

    data = []

    for item in listaDatas:
        data.append(datetime.datetime.strptime(item, "%d/%m/%Y").strftime("%d-%b-%Y"))

    return data



'''
deletaColuna(planilha,28,len(planilha))
deletaColuna(planilha,27,len(planilha))
deletaColuna(planilha,26,len(planilha))

deletaColuna(planilha,25,len(planilha))
deletaColuna(planilha,24,len(planilha))
deletaColuna(planilha,23,len(planilha))
deletaColuna(planilha,22,len(planilha))
deletaColuna(planilha,21,len(planilha))

deletaColuna(planilha,20,len(planilha))
#deletaColuna(planilha,19,len(planilha))
deletaColuna(planilha,18,len(planilha))
deletaColuna(planilha,17,len(planilha))
deletaColuna(planilha,16,len(planilha))

#deletaColuna(planilha,15,len(planilha))
deletaColuna(planilha,14,len(planilha))
deletaColuna(planilha,13,len(planilha))
deletaColuna(planilha,12,len(planilha))
deletaColuna(planilha,11,len(planilha))

deletaColuna(planilha,10,len(planilha))
deletaColuna(planilha,9,len(planilha))
deletaColuna(planilha,8,len(planilha))
deletaColuna(planilha,7,len(planilha))
deletaColuna(planilha,6,len(planilha))

deletaColuna(planilha,5,len(planilha))
deletaColuna(planilha,4,len(planilha))
deletaColuna(planilha,3,len(planilha))
deletaColuna(planilha,2,len(planilha))
deletaColuna(planilha,1,len(planilha))
deletaColuna(planilha,0,len(planilha))
'''