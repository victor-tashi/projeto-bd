# teste interface
# pip install PySimpleGUI // para instalar a biblioteca
import sqlite3
from PySimpleGUI import PySimpleGUI as sg

# designe da tela
#
sg.theme('Dark Grey 13')
layout1 = [
    [sg.Text('Aluno:   '), sg.Input(size=(25, 0), key='nome')],
    [sg.Text('Numero:'), sg.Input(size=(25, 0), key='numero')],
    [sg.Text('Qual sua serie?')],
    [sg.Radio('1A', 'serie', key='A1'), sg.Radio('2A', 'serie', key='A2'), sg.Radio('3A', 'serie', key='A3')],
    [sg.Text('Qual a materia?')],
    [sg.Radio('portugues', 'materia', key='port'), sg.Radio('matematica', 'materia', key='mat')],
    [sg.Button('entrar')]
]

# Iniciação da janela
#
janela1 = sg.Window('login').layout(layout1)
button, values1 = janela1.read()

# variaveis
#
nome = values1['nome']
numero = values1['numero']
A1 = values1['A1']
A2 = values1['A2']
A3 = values1['A3']
port = bool(values1['port'])
mat = values1['mat']

if port:
    materia = 'portugues'
else:
    materia = 'matematica'

if A1:
    serie = '1A'

elif A2:
    serie = str('2A')

else:
    serie = str('3A')

# tela 2

layout2 = [
    [sg.Text('nota 1: '), sg.Input(size=(25, 0), key="n1")],
    [sg.Text('nota 2: '), sg.Input(size=(25, 0), key="n2")],
    [sg.Text('nota 3: '), sg.Input(size=(25, 0), key="n3")],
    [sg.Text('nota 4: '), sg.Input(size=(25, 0), key="n4")],
    [sg.Button('entra')]
]

janela2 = sg.Window('notas').layout(layout2)
button, values2 = janela2.read()

# variaveis notas

n1 = values2['n1']
n2 = values2['n2']
n3 = values2['n3']
n4 = values2['n4']

# banco de dados
#

db = sqlite3.connect('DataBase.db')

# tela 1
cursor = db.cursor()
# cursor.execute("CREATE TABLE alunos (idAlunos integer primary key autoincrement, Numero integer not null,"
#                " nome text not null, serie text not null)")

# cursor.execute("CREATE TABLE "+nome+" (idAlunos integer foreign key, Numero interger not null, nome text, "
#            " nota3 real, nota4 real, media real )")
cursor.execute("INSERT INTO alunos (Numero, nome, serie) VALUES(" + str(numero) + ", '" + nome + "','" + serie + "')")
# cursor.execute("INSERT INTO "+nome+" (nome) VALUES('"+nome+"',)")


# tela 2

cursor.execute("CREATE TABLE notas (n1 interger not null, n2 interger not null, n3 interger not null,"
               " n4 interger not null)")

cursor.execute("INSERT INTO notas (n1, n2, n3, n4) VALUES (" + str(n1) + ", " + str(n2) + ", " + str(n3) + ", "
               + str(n4) + ")")

db.commit()

cursor.execute("SELECT * FROM alunos")
print(cursor.fetchall())
