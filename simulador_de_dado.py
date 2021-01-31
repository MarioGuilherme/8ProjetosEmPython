# Simulador de Dado
# Simular o uso de um dado, aleatorizando um valor de 1 até 6

import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_monimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de jogar o dado novamente? '
        # Layout
        self.layout = [
            [sg.Text('Jogar o dado? ')],
            [sg.Button('sim'),sg.Button('Não')]
        ]
      
    def Iniciar(self):
         # Criar uma janela
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        # Ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # Fazer alguma coisa com esses valores
        while True:
            try:
                if self.eventos == 'sim' or self.eventos == 's':
                    self.GerarValorDoDado()
                elif self.eventos == 'Não' or self.eventos == 'n' or self.eventos == 'nao':
                    print('Agradeço pela sua participação')
                else:
                    print('Por favor digitar Sim ou não')
            except:
                print('Ocorreu um erro ao receber sua resposta')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_monimo, self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()