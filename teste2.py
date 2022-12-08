from PySimpleGUI import PySimpleGUI as sg
import sqlite3

plinio = True
# banco de dados
db = sqlite3.connect('DataBase.db')
cursor = db.cursor()
# layout
sg.theme('Dark Grey 13')
login = [
    [sg.Text('email', size=(10, 0)), sg.Input(size=(25, 0), key='email')],
    [sg.Text('senha', size=(10, 0)), sg.Input(size=(25, 0), key='senha')],
    [sg.Button('entrar'), sg.Button('registra')]
]
singin = [
    [sg.Text('nome', size=(15, 0)), sg.Input(size=(25, 0), key='nome')],
    [sg.Text('numero:', size=(15, 0)), sg.Input(size=(25, 0), key='num')],
    [sg.Text('Qual sua serie?')],
    [sg.Radio('1A', 'serie', key='A1'), sg.Radio('2A', 'serie', key='A2'), sg.Radio('3A', 'serie', key='A3')],
    [sg.Text('Aluno ou prof??')],
    [sg.Radio('aluno', 'nivel', key='aluno'), sg.Radio('prof', 'nivel', key='prof')],
    [sg.Text('email', size=(15, 0)), sg.Input(size=(25, 0), key='email')],
    [sg.Text('senha', size=(15, 0)), sg.Input(size=(25, 0), key='senha')],
    [sg.Button('registra')]
]
menu = [
    [sg.Button('ver notas'), sg.Button('add notas')],
    [sg.Text('', size=(20, 0))]
]
while plinio:
    Login = sg.Window('login', login)
    eventoL, valorL = Login.read()

    if eventoL == sg.WIN_CLOSED:
        break

    if eventoL == 'registra':
        Login.close()
        Singin = sg.Window('Sing In', singin)
        eventoS, valorS = Singin.read()

        if eventoS == sg.WIN_CLOSED:
            break

        if eventoS == 'registra':
            nome = valorS['nome']
            num = str(valorS['num'])
            A1 = valorS['A1']
            A2 = valorS['A2']
            A3 = valorS['A3']
            aluno = valorS['aluno']
            prof = valorS['prof']
            Email = valorS['email']
            senha = valorS['senha']
            serie = ''
            nivel = ''

            if A1:
                serie = '1A'

            elif A2:
                serie = str('2A')

            elif A3:
                serie = str('3A')

            if aluno:
                nivel = str('aluno')

            if prof:
                nivel = str('prof')

            cursor.execute(f"INSERT INTO registros(nome, numero, classe, email, senha, nivel) VALUES('{nome}',{num},"
                           f"'{serie}','{Email}','{senha}', '{nivel}')")
            db.commit()
            Singin.close()

    if eventoL == 'entrar':
        Email = valorL['email']
        senha = valorL['senha']
        check = [(f'{Email}', f'{senha}')]
        cursor.execute(f"SELECT email, senha FROM registros WHERE email = '{Email}' AND senha = '{senha}'")
        test = cursor.fetchall()
        if check == test:
            Login.close()
            check = [(f'{senha}')]
            cursor.execute(f"SELECT nivel FROM registros WHERE nivel = 'prof'")
            test = cursor.fetchall()
            if check != test:
                Menu = sg.Window('Menu', menu)
                eventoM, valorM = Menu.read()
                if eventoM == sg.WIN_CLOSED:
                    break
            else:
                menu = [
                    [sg.Button('ver notas'), sg.Button('add notas')],
                    [sg.Text('', size=(20, 0))]
                ]
                Menu = sg.Window('Menu', menu)
                eventoM, valorM = Menu.read()
                if eventoM == sg.WIN_CLOSED:
                    break

        else:
            Login.close()
            login = [
                [sg.Text('Email ou senha invalido')],
                [sg.Text('email', size=(10, 0)), sg.Input(size=(25, 0), key='email')],
                [sg.Text('senha', size=(10, 0)), sg.Input(size=(25, 0), key='senha')],
                [sg.Button('entrar')]
            ]
