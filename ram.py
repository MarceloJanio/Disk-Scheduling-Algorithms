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
    try:
        i = i.replace('\n',"")
    except:
        pass
    try:
        i = i.replace('\r',"")
    except:
        pass
    save.append(int(i))

save2 = save.copy()
save3 = save.copy()


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
    print("OTM {}".format(nfaltapagina))

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


def segundaChance():
    nfaltapagina = 0
    quadro = []
    nquadros = save2.pop(0)
    iteracoes = 0
    for i in range(0, nquadros):
        quadro.append([save2[i], 1])
        nfaltapagina += 1
        iteracoes += 1
        if(iteracoes == 4):
            zeraBitref(quadro)
            iteracoes = 0
    queue = save2[nquadros:]
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

    print("SC {}".format(nfaltapagina))

def atualizatime(lista, bol, number):
    if(bol):
        for i in range(0, len(lista)):
            lista[i][-1] = lista[i][-1]+1
    else:
        for i in range(0, len(lista)):
            if(lista[i][0] == number):
                lista[i][2] = 0
                return 0
    
def attlista(number, lista, limiar):
    for i in range(0, len(lista)):
        if(lista[i][2] > limiar and lista[i][1] == 0):
            lista[i][0] = number
            lista[i][1] = 1
            lista[i][2] = 0
            return 0
        else:   
            id = 0
            maioridade = lista[0][2]
            for j in range(1, len(lista)):
                if(lista[i][1]>maioridade):
                    maioridade = lista[j][2]
                    id = j
        lista[id] = [number, 1, 0]

def CT():
    nfaltapagina = 0
    quadro = []
    nquadros = save3.pop(0)
    iteracoes = 0
    limiar = (nquadros//2) + 1
    for i in range(0, nquadros):
        atualizatime(quadro, True, 0)
        quadro.append([save3[i], 1, 0])
        nfaltapagina += 1
        iteracoes += 1
        if(iteracoes == 4):
            zeraBitref(quadro)
            iteracoes = 0
    queue = save3[nquadros:]
    proxQueue = 0
    while(proxQueue!=len(queue)-1):
        if(verificaNaLista(queue[proxQueue], quadro)):
            atualizaBitref(queue[proxQueue], quadro)
            atualizatime(quadro, True, 0)
            atualizatime(quadro, False, queue[proxQueue])
            iteracoes += 1
            proxQueue += 1
        else:
            attlista(queue[proxQueue], quadro, limiar)
            iteracoes+=1
            proxQueue += 1
            nfaltapagina +=1
        if(iteracoes == 3):
            zeraBitref(quadro)
            iteracoes = 0
    print("CT {}".format(nfaltapagina))

segundaChance()
otimo()
CT()