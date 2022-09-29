import sys

def OpenFile():
    arquivo = sys.stdin
    try:
        dados = arquivo.readlines()
        return dados
    except:
        print('Arquivo não encontrado!')
        exit(0)
dados = OpenFile()

save = []

for i in dados:
    save.append(int(i.split('\n')[0]))

def verificadistante(lista, listaConfere):
    index = 0
    listatemp = lista.copy()
    while(len(listatemp)>1 and index <= len(listaConfere)):
        try:
            listatemp.remove(listaConfere[index])
        except:
            pass
        index+=1
    return listatemp[0]


def otimo():
    nfaltapagina = 0
    quadro = []
    count = 0
    nquadros = save.pop(0)
    for i in range(0, nquadros):
        quadro.append(save[i])
        nfaltapagina += 1
    count = nquadros
    for i in save[nquadros:]:
        if(i in quadro):
            pass
        else:
            substituido = verificadistante(quadro, save[count:])
            quadro[quadro.index(substituido)] = i
            nfaltapagina += 1
        count+=1
    print("OTM", nfaltapagina)



otimo()