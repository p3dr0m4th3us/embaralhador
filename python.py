from browser import document, html
import random
lista_alunos = []
lista_equipes = []
cabecas = []
contador_alunos = 0
contador_equipes = 0
contador_equipes_2 = 1
numero_alunos = int(input('Número de alunos: '))
numero_equipes = int(input('Número de equipes: '))
alunos_por_equipe = numero_alunos // numero_equipes
calculo_alunos_que_sobraram = numero_alunos % numero_equipes
alunos_que_sobraram = []
contador_forcado_1 = 0
contador_forcado_2 = 1
while contador_alunos <= numero_alunos - 1:
    contador_alunos += 1
    lista_alunos.append(contador_alunos)
embaralhar = random.shuffle(lista_alunos)
if calculo_alunos_que_sobraram == 1: 
    alunos_que_sobraram = [lista_alunos[-1]]
if calculo_alunos_que_sobraram >= 1:
    alunos_que_sobraram = lista_alunos[calculo_alunos_que_sobraram * -1::]
if calculo_alunos_que_sobraram == 0:
    alunos_que_sobraram = []
while contador_equipes <= numero_equipes - 1:
    contador_equipes += 1
    lista_equipes.append(f'Equipe {contador_equipes}')
while contador_equipes_2 <= numero_equipes:
    lista_equipes_que_vai_aparecer = lista_equipes[contador_equipes_2 - 1]
    if len(alunos_que_sobraram) != 0:
        lista_alunos_que_vai_aparecer = lista_alunos[alunos_por_equipe * contador_forcado_1:alunos_por_equipe * contador_forcado_2] + [alunos_que_sobraram[-1]]
        contador_forcado_1 += 1
        contador_forcado_2 += 1
        alunos_que_sobraram.pop(-1)
    else:
        lista_alunos_que_vai_aparecer = lista_alunos[alunos_por_equipe * contador_forcado_1:alunos_por_equipe * contador_forcado_2]
        contador_forcado_1 += 1
        contador_forcado_2 += 1
    document <= html.B(f'''{lista_equipes_que_vai_aparecer}''')
    document <= html.B('<br>')
    document <= html.B(f'''{lista_alunos_que_vai_aparecer}''')
    document <= html.B('<br>')
    document <= html.B('<br>')
    contador_equipes_2 += 1
