import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.theme('DarkAmber')
        # Layout
        layout = [
            [sg.Text('Nome', size=(5,0)),sg.Input(size=(15,0),key='nome')],
            [sg.Text('Idade', size=(5,0)),sg.Input(size=(15,0),key='idade')],
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail',key='gmail'),sg.Checkbox('Outlook',key='outlook'),sg.Checkbox('Yahoo',key='yahoo')],
            [sg.Text('Aceita cartão?')],
            [sg.Radio('Sim', 'cartoes', key='aceitaCartao'),sg.Radio('Não', 'cartoes', key='naoAceitaCartao')],
            [sg.Button('Enviar Dados')],
            [sg.Slider(range=(0, 255), default_value=0,orientation='h',size=(15,20),key='sliderVelocidade')],
            [sg.Output(size=(30,20))]
        ]

        # Janela
        self.janela = sg.Window('Dados do Uusário').layout(layout)

        # Extrair dados da tela
        # self.button, self.values = self.janela.Read()

    def Iniciar(self):
       while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceitaGmail = self.values['gmail']
            aceitaOutlook = self.values['outlook']
            aceitaYahoo = self.values['yahoo']
            aceitaCartao = self.values['aceitaCartao']
            naoAceitaCartao = self.values['naoAceitaCartao']
            velScript = self.values['sliderVelocidade']
            print(f'Nome: {nome} ')
            print(f'idade: {idade} ')
            print(f'aceita gmail: {aceitaGmail} ')
            print(f'aceita outlook: {aceitaOutlook} ')
            print(f'aceita yahoo: {aceitaYahoo} ')
            print(f'aceita cartao: {aceitaCartao} ')
            print(f'aceita cartao: {naoAceitaCartao} ')
            print(f'Velocidade {velScript} ')

tela = TelaPython()
tela.Iniciar()