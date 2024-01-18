import random
import PySimpleGUI as sg
import os

class PassGenerator:
  
  def __init__(self):
    sg.theme('Black')
    layout = [
      [sg.Text('Site/Software', size=(10,1)), sg.Input(key='site', size=(20,1))],
      [sg.Text('E-mail/Usuário', size=(10,1)),sg.Input(key='usuario', size=(20,1))],
      [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(range(30)), key='total_chars', default_value=1, size=(3,1))],
      [sg.Output(size=(32,5))],
      [sg.Button('Gerar senha')]
    ]
      
    self.janela = sg.Window('Password Generator', layout)
    
  def Iniciar(self):
    while True:
      event, value = self.janela.read()
      if event == sg.WINDOW_CLOSED:
        break
      if event == 'Gerar senha':
        nova_senha = self.gerar_senha(value)
        print(nova_senha)
        self.salvar_senha(nova_senha, value)
        
  def gerar_senha(self, values):
    char_list='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!@#$%&*()"'
    chars = random.choices(char_list, k=int(values['total_chars']))
    new_pass = ''.join(chars)
    return new_pass
    
  def salvar_senha(self, new_pass, values):
    with open('senhas.txt', 'a', newline='') as file:
      file.write(f'site: {values['site']}, usuário: {values['usuario']}, nova senha: {new_pass}\n')

gen = PassGenerator()
gen.Iniciar() 