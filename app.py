import os

restaurantes = ['Sabor & Sabor', 'Salada no pote!']

def exibir_banner():
  print('''

█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
      ''')

def exibir_titulo_da_opcao(texto):
  os.system('clear')
  print(texto)

def voltar_ao_menu():
  input('Pressione ENTER para voltar ao menu...')
  main()


def exibir_opcoes_de_menu():
  print('1 - Cadastrar Restaurante')
  print('2 - Listar Restaurantes')
  print('3 - Ativar Restaurante')
  print('0 - Sair\n')
  
def fechar_aplicacao():
   exibir_titulo_da_opcao('Volte sempre ao Sabor Express! ')
   
def opcao_invalida():
  print('Opção inválida!')

def adicionar_restaurante():
  exibir_titulo_da_opcao('Adicionar Restaurante')
  nome_do_restaurante = input('Digite o nome do restaurante: ')
  restaurantes.append(nome_do_restaurante)
  print('Restaurante cadastrado com sucesso!')
  voltar_ao_menu()

def listar_restaurantes():
  exibir_titulo_da_opcao('Opções de restaurantes')
  for restaurante in restaurantes:
    print(f'-> {restaurante}')
  voltar_ao_menu()

def selecionar_opcao():
  try:
    opcao_escolhida = int(input('Digite a opção desejada: ')) 
    match opcao_escolhida:
          case 1: 
            adicionar_restaurante()
          case 2:
            listar_restaurantes()
          case 3: 
            print('Ativar Restaurante')
          case 0:
            fechar_aplicacao()
          case _:
            opcao_invalida()
  except:
    opcao_invalida()

def main():
  exibir_banner()
  exibir_opcoes_de_menu()
  selecionar_opcao()

if __name__ == '__main__':
  main()