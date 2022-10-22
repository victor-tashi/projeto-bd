# teste interface
# pip install PySimpleGUI // para instalar a biblioteca

from PySimpleGUI import PySimpleGUI as sg

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