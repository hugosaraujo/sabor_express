import os

def exibir_banner():
  print('''

█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
      ''')

def exibir_opcoes_de_menu():
  print('1 - Cadastrar Restaurante')
  print('2 - Listar Restaurantes')
  print('3 - Ativar Restaurante')
  print('0 - Sair')

def fechar_aplicacao():
   os.system('clear')
   print('Fechando a aplicação!')
   print('Tchau Tchau')

def selecionar_opcoes():
  opcao_escolhida = int(input('Digite a opção desejada: ')) 
  match opcao_escolhida:
        case 1: 
          print('Adicionar Restaurante')
        case 2:
          print('Listar Restaurantes')
        case 3: 
          print('Ativar Restaurante')
        case 0:
          fechar_aplicacao()
        case _:
          print('Opção inválida!')

def main():
  exibir_banner()
  exibir_opcoes_de_menu()
  selecionar_opcoes()

if __name__ == '__main__':
  main()