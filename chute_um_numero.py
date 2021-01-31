# Projeto 3 - Chute o número
# objetivo: Criar um algoratimo que gera um valor aleatório e eu tenho que ficar tentando o número até acertar
import random
import PySimpleGUI as sg

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentarNovamente = True
            
    def Iniciar(self):
        # Layout
        layout = [
            [sg.Text('Seu chute', size=(30,0))],
            [sg.Input(size=(10,0), key='ValorChute')],
            [sg.Button('Chutar')],
            [sg.Output(size=(30,10))]
        ]
        # Criar a janela
        self.janela = sg.Window('Chute o Número', layout=layout)
        self.GerarNumero()
        try:
            while True:
                # Receber os valores 
                self.evento, self.valores = self.janela.Read()
                # Fazer alguma coisa com os valores
                if self.evento == 'Chutar':
                    self.valorChutado = self.valores['ValorChute']
                    while self.tentarNovamente == True:
                        if int(self.valorChutado) > self.valor_aleatorio:
                            print('Chute um valor mais baixo!')
                            break
                        elif int(self.valorChutado) < self.valor_aleatorio:
                            print('Chute um valor mais alto!')
                            break
                        if int(self.valorChutado) == self.valor_aleatorio:
                            self.tentarNovamente = False
                            print('PARABÉNS, VOCÊ ACERTOU!!!')
                            break
        except:
            print('Por favor, digite apenas número!')
            self.Iniciar()

    def GerarNumero(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()