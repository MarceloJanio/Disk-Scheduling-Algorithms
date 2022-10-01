from concurrent.futures import process
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
    save.append(i.split(" "))

for i in range(0,len(save)):
    save[i][0] = int(save[i][0])
    save[i][1] = int(save[i][1])

processos = {}

count = 0
for i in save:
    processos[count] = {'inicio': i[0], 'tempToExec': i[1], 'finish': False, 'inicioReal': -1, 'finishReal': -1, 'momentosExec': [], 'tempRes': i[1]}
    count +=1


#processos = sorted(processos, key = processos.get('inicio'))

def calculaRetornoMedio(processos):
    sum = 0
    for i in range(0, len(processos)):
        sum += abs(processos[i]['inicio'] - processos[i]['finishReal'])
    return sum/len(processos)

def calculaRespostaMedio(processos):
    sum = 0
    for i in range(0, len(processos)):
        sum += abs(processos[i]['inicio'] - processos[i]['inicioReal'])
    return sum/len(processos)

def calculaProntoMedio(processos):
    sum = 0
    for i in range(0, len(processos)):
        tempoExecTotal =  processos[i]['finishReal'] - processos[i]['inicio']
        for j in processos[i]['momentosExec']:
            tempoExecTotal -= abs(j[0] - j[1])
        sum += tempoExecTotal
    return sum/len(processos)

print(processos)

def roundRobin():
    countProc = len(processos)
    procAtual = 0
    instante = 0
    while(countProc!=0):
        quantum = 0
        if(processos[procAtual]['inicio'] <= instante) and processos[procAtual]['tempRes'] > 0:
            initialinsta = instante
            if(processos[procAtual]['inicioReal'] == -1):
                processos[procAtual]['inicioReal'] = instante
            canexec = True
            while(quantum != 2 and canexec):
                processos[procAtual]['tempRes'] = processos[procAtual]['tempRes'] - 1
                if(processos[procAtual]['tempRes'] == 0):
                    instante += 1
                    canexec = False
                    processos[procAtual]['finish'] = True
                    processos[procAtual]['finishReal'] = instante
                    countProc -= 1
                else:
                    instante += 1
                quantum += 1
            finalinsta = instante
            processos[procAtual]['momentosExec'].append([initialinsta, finalinsta])
        #else:
         #   instante += 1
        procAtual += 1
        if(procAtual) > len(processos)-1:
            procAtual = 0
    print("RR %.2f %.2f %.2f" %(calculaRetornoMedio(processos), calculaRespostaMedio(processos), calculaProntoMedio(processos)))
roundRobin()