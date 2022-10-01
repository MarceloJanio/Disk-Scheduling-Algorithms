import queue
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

def zeraBitref(lista):
    for i in range(0, len(lista)):
        lista[i][1] = 0

def verificaNaLista(number, lista):
    for i in range(0, len(lista)):
        if(lista[i][0] == number):
            return True
    return False

def atualizaBitref(number, lista):
    for i in range(0, len(lista)):
        if(lista[i][0] == number):
            lista[i][1] = 1

def attnrotlist(number, lista):
    count = 0
    while(True):
        if(lista[count][1] == 0):
            lista.pop(count)
            lista.append([number, 1])
            return 0
        else:
            lista.append(lista.pop(count))
            lista[-1][1] = 0
        if(count == len(lista)):
            count = 0

def atualizainstante():
    pass



def segundaChance():
    nfaltapagina = 0
    quadro = []
    nquadros = save.pop(0)
    iteracoes = 0
    for i in range(0, nquadros):
        quadro.append([save[i], 1])
        nfaltapagina += 1
        iteracoes += 1
        if(iteracoes == 4):
            zeraBitref(quadro)
            iteracoes = 0
    queue = save[nquadros:]
    proxQueue = 0
    while(proxQueue!=len(queue)-1):
        if(verificaNaLista(queue[proxQueue], quadro)):
            atualizaBitref(queue[proxQueue], quadro)
            iteracoes += 1
            proxQueue += 1
        else:
            attnrotlist(queue[proxQueue], quadro)
            iteracoes+=1
            proxQueue += 1
            nfaltapagina +=1
        if(iteracoes == 3):
            zeraBitref(quadro)
            iteracoes = 0

    print(nfaltapagina)

def CT():
    nfaltapagina = 0
    quadro = []
    nquadros = save.pop(0)
    iteracoes = 0
    instante = 0
    for i in range(0, nquadros):
        quadro.append([save[i], 1, instante])
        nfaltapagina += 1
        iteracoes += 1
        instante += 1
        if(iteracoes == 4):
            zeraBitref(quadro)
            iteracoes = 0
    queue = save[nquadros:]
    while(proxQueue!=len(queue)-1):
        if(verificaNaLista(queue[proxQueue], quadro)):
            atualizaBitref(queue[proxQueue], quadro)
            iteracoes += 1
            proxQueue += 1
        else:
            attnrotlist(queue[proxQueue], quadro)
            iteracoes+=1
            proxQueue += 1
            nfaltapagina +=1
        if(iteracoes == 3):
            zeraBitref(quadro)
            iteracoes = 0

CT()