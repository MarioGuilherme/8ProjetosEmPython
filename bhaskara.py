# Projeto Próprio - Calculadora básica de bhaskara
# objetivo:  Calcular o valor de x1, x2 e delta com os valores de A, B e C

import PySimpleGUI as sg
import math

class TelaPython:
    def __init__(self):
        
        layout = [
            [sg.Text('Valor de A', size=(10,0)),sg.Input(size=(15,0),key='a')],
            [sg.Text('Valor de B', size=(10,0)),sg.Input(size=(15,0),key='b')],
            [sg.Text('Valor de C', size=(10,0)),sg.Input(size=(15,0),key='c')],
            [sg.Button('Calcular')],
            [sg.Output(size=(50,10))]
        ]

        self.janela = sg.Window('Calculadora Simples de Bhaskara').layout(layout)

    def Iniciar(self):
       while True:
            self.button, self.values = self.janela.Read()
            if self.values['a'] == '' or self.values['b'] == '' or self.values['c'] == '' or self.values['a'] == '0' or self.values['b'] == '0' or self.values['c'] == '0':
                print('Insira valores válidos, por favor!')
            else:
                a = int(self.values['a'])
                b = int(self.values['b'])
                c = int(self.values['c'])
                delta = (b*b) + (-4 * a * c)
                x1 = ((b * -1) + math.sqrt(delta)) / (2 * a)
                x2 = ((b * -1) - math.sqrt(delta)) / (2 * a)
                print(f'Valor de Delta = {delta}')
                print(f'Valor de x1 = {x1}')
                print(f'Valor de x2 = {x2}')

tela = TelaPython()
tela.Iniciar()