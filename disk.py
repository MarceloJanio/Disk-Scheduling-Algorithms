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

def fcfs():
    fcfsvar = 0
    limit = len(save3)-1
    for i in range(1, limit):
        a = abs(save3[i] - save3[i+1])
        fcfsvar += a
    print("FCFS {}".format(fcfsvar))

def findprox(lista, atual):
    esquerda = None
    direita = None
    try:
        esquerda = lista[atual-1]
    except:
        pass
    try:
        direita = lista[atual+1]
    except:
        pass

    if(esquerda != None and direita != None):
        val1 = abs(lista[atual] - esquerda)
        val2 = abs(lista[atual] - direita)
        if(val1 < val2):
            return lista[atual-1]
        else:
            return lista[atual+1]
    elif(esquerda == None):
        return lista[atual+1]
    else:
        return lista[atual-1]
        


def ssfs():
    tam = save.pop(0)
    first = save[0]
    diskvar = 0
    save.sort()
    index = save.index(first)
    while(len(save) > 1):
        indexprox = findprox(save, index)
        diskvar += abs(save[index]-indexprox)
        save.remove(save[index])
        index = save.index(indexprox)
    print("SSTF {}".format(diskvar))

def elevador():
    save = save2
    tam = save.pop(0)
    first = save[0]
    diskvar = 0
    save.sort()
    index = save.index(first)
    lastindex = len(save)-1

    if(index == 0):
        for i in range(0, len(save)-1):
            diskvar += abs(save[i]-save[i+1])
    elif(index == lastindex):
        for i in range(len(save)-1, 0, -1):
            diskvar += abs(save[i]-save[i-1])
    else:
        for i in range(index, lastindex):
            diskvar += abs(save[i]-save[i+1])
        diskvar += abs(save[lastindex]-save[index-1])
        for i in range(index-1, 0, -1):
            diskvar += abs(save[i]-save[i-1])

    print("ELEVADOR {}".format(diskvar))

fcfs()
ssfs()
elevador()