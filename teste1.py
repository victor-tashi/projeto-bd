# teste => este é um banco de dados quase concluido // proxima vez que alterar anotas coisas que faltam
# pip install db-sqlite3 // para instalar a biblioteca

import sqlite3
import PySimpleGUI as sg


# variaveis

nome = str()
numero = int()
materia = str()
A1 = bool()
A2 = bool()
A3 = bool()


# n1 = float(input('digite a 1° nota: '))
# n2 = float(input('digite a 2° nota: '))
# n3 = float(input('digite a 3° nota: '))
# n4 = float(input('digite a 4° nota: '))
# media = float((n1 + n2 + n3 + n4)/4)

# interface

# Layout
class Inter:
    def __init__(self):
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

        # janela
        janela = sg.Window('login').layout(layout)
        self.button, self.values = janela.read()

    def iniciar(self):
        nome = self.values['nome']


# extrair os dados


if A1 == 'true':
    serie = '1A'
elif A2 == 'true':
    serie = str('2A')
else:
    serie = str('3A')
tela = Inter()
tela.iniciar()

# banco de dados

db = sqlite3.connect('segundo_banco.db')

cursor = db.cursor()
# cursor.execute("CREATE TABLE alunos (idAlunos integer primary key autoincrement, Numero integer not null,"
#               " nome text not null, serie text not null)")

# cursor.execute("CREATE TABLE "+nome+" (idAlunos integer foreign key, Numero interger not null, nome text, "
#            " nota3 real, nota4 real, media real )")
cursor.execute("INSERT INTO alunos (Numero, nome, serie) VALUES(" + str(numero) + ", '" + nome + "','" + serie + "')")
# cursor.execute("INSERT INTO "+nome+" (nome) VALUES('"+nome+"',)")

db.commit()

cursor.execute("SELECT nota1 FROM alunos")
print(cursor.fetchall())
