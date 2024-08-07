import os

restaurantes = [{'nome': 'Sabor & Sabor', 'categoria': 'mineira', 'status': True},
                {'nome': 'Salada no pote!', 'categoria': 'fitness', 'status': False},
                {'nome': 'Apetit Natural', 'categoria': 'vegano', 'status': False}]

def exibir_banner():
  print('''

█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
      ''')

def exibir_titulo_da_opcao(texto):
  os.system('clear')
  linha_de_asteriscos = '*' * (len(texto) + 4 ) 
  print(f'{linha_de_asteriscos}')
  print(f'* {texto} *')
  print(f'{linha_de_asteriscos}\n')

def voltar_ao_menu():
  input('Pressione ENTER para voltar ao menu...')
  main()


def exibir_opcoes_de_menu():
  print('1 - Cadastrar Restaurante')
  print('2 - Listar Restaurantes')
  print('3 - Ativar Status Restaurante')
  print('0 - Sair\n')
  
def fechar_aplicacao():
   exibir_titulo_da_opcao('Volte sempre ao Sabor Express! ')
   
def opcao_invalida():
  print('Opção inválida!')

def adicionar_restaurante():
  exibir_titulo_da_opcao('Adicionar Restaurante')
  nome_restaurante = input('Digite o nome do restaurante: ')
  categoria_restaurante = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
  dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria_restaurante, 'status': True}
  restaurantes.append(dados_restaurante)
  print('Restaurante cadastrado com sucesso!')
  voltar_ao_menu()

def listar_restaurantes():
  exibir_titulo_da_opcao('Opções de restaurantes')
  print('  Nome'.ljust(24), 'Categoria'.ljust(33), 'Status', sep = '|')
  for restaurante in restaurantes:
    nome_restaurante = restaurante['nome']
    categoria_restaurante = restaurante['categoria']
    status_restaurante = 'Ativo' if restaurante['status'] else 'Inativo'
    print(f'-> {nome_restaurante.ljust(20)} | Categoria: {categoria_restaurante.ljust(20)} | Status: {status_restaurante}')
  voltar_ao_menu()

def modificar_status_restaurante():
  exibir_titulo_da_opcao('Modificar Status de um Restaurante')
  nome_restaurante = input('Digite o nome do restaurante que deseja modificar o status: ')
  resturante_encontrado = False
  
  for restaurante in restaurantes:
    if nome_restaurante == restaurante['nome']:
      resturante_encontrado = True
      restaurante['status'] = not restaurante['status']
      mensagem = f'{nome_restaurante} ativado com sucesso' if restaurante['status'] else f'{nome_restaurante} desativado com sucesso'
      print(mensagem)

  if not resturante_encontrado:
    print(f'O Restaurante {nome_restaurante} não foi encontrado')
  
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
            modificar_status_restaurante()
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