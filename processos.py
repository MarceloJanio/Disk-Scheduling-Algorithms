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

print(save)

processos = {}

count = 0
for i in save:
    processos[count] = {'inicio': i[0], 'tempToExec': i[1], 'finish': False, 'inicioReal': -1, 'finishReal': -1}
    count +=1

countProc = len(processos)
instante = 0

#processos = sorted(processos, key = processos.get('inicio'))
procAtual = 0
def roundRobin():
    while(countProc!=0):
        for i in range
    pass

print(countProc!=0)