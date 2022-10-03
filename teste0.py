# teste interface
# pip install PySimpleGUI // para instalar a biblioteca

from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuario:'), sg.Input(key='user')],
    [sg.Text('senha:  '), sg.Input(key='senha', password_char='#')],
    [sg.Checkbox('salvar login?')],
    [sg.Button('entrar')]
]

# janela
janela = sg.Window('login', layout)

# eventos
while True:
    eventos, valores = janela.read()

    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'entrar':
        if valores['user'] == 'victor' and valores['senha'] == 1234:
            print('bem vindo')
