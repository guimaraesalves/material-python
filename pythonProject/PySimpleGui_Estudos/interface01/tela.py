import PySimpleGUI as sg 



class TelaPython:
    def __init__(self):
        #Layout
        layout = [
            [sg.Text('Nome'), sg.Input()],
            [sg.Text('Idade'), sg.Input()],
            [sg.Button('Enviar')]
        ]
        # Janela
        janela = sg.Window("Dados do Usuário").layout(layout)
        # Extrair dados da tela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        print(self.values)

tela = TelaPython()
tela.Iniciar()



