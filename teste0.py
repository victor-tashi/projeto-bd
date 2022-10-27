# teste interface
# pip install PySimpleGUI // para instalar a biblioteca
import sqlite3
from PySimpleGUI import PySimpleGUI as sg

# designe da tela
#
sg.theme('Dark Grey 13')
layout = [
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
janela = sg.Window('login').layout(layout)
button, values = janela.read()

# variaveis
#
nome = values['nome']
numero = values['numero']
A1 = values['A1']
A2 = values['A2']
A3 = values['A3']
port = bool(values['port'])
mat = values['mat']

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

# banco de dados
#

db = sqlite3.connect('DataBase.db')

cursor = db.cursor()
# cursor.execute("CREATE TABLE alunos (idAlunos integer primary key autoincrement, Numero integer not null,"
#                " nome text not null, serie text not null)")

# cursor.execute("CREATE TABLE "+nome+" (idAlunos integer foreign key, Numero interger not null, nome text, "
#            " nota3 real, nota4 real, media real )")
cursor.execute("INSERT INTO alunos (Numero, nome, serie) VALUES(" + str(numero) + ", '" + nome + "','" + serie + "')")
# cursor.execute("INSERT INTO "+nome+" (nome) VALUES('"+nome+"',)")

db.commit()

cursor.execute("SELECT * FROM alunos")
print(cursor.fetchall())
