from browser import document, html
import random
import datetime
lista_alunos = []
lista_equipes = []
lista_numero_alunos = []
cabecas = []
contador_alunos = 0
contador_equipes = 0
contador_equipes_2 = 1
data = str(datetime.datetime.today())
segundo = str(data[17:19])
hora = str(data[11:13])
minuto = str(data[14:16])
ano = str(data[0:4])
mes = str(data[5:7])
dia = str(data[8:10])
tempo = f'''Dia {dia}/{mes}/{ano}, às {hora}:{minuto}:{segundo}'''
disciplina = str(input('Disciplina: '))
conteudo = str(input('Conteúdo: '))
turma = str(input('Turma: '))
numero_alunos = int(input('Número de alunos: '))
numero_equipes = int(input('Número de equipes: '))
document <= html.B(f'''Hora: {tempo}''')
document <= html.B('<br>')
document <= html.B(f'''Disciplina: {disciplina}''')
document <= html.B('<br>')
document <= html.B(f'''Conteúdo: {conteudo}''')
document <= html.B('<br>')
document <= html.B(f'''Turma: {turma}''')
document <= html.B('<br>')
document <= html.B('<br>')
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
    lista_numero_alunos.append(len(lista_alunos_que_vai_aparecer))
if lista_numero_alunos[0] != lista_numero_alunos[-1]:
    document <= html.B(f'{lista_numero_alunos.count(lista_numero_alunos[0])} equipes de {lista_numero_alunos[0]} alunos')
    document <= html.B('<br>')
    document <= html.B(f'{lista_numero_alunos.count(lista_numero_alunos[-1])} equipes de {lista_numero_alunos[-1]} alunos')
else:
    document <= html.B(f'{numero_equipes} equipes de {alunos_por_equipe} alunos')
