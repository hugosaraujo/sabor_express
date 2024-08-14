from modelos.restaurante import Restaurante

careca = Restaurante('Careca', 'Chinesa')
careca.adicionar_avaliacao('João', 5)
careca.adicionar_avaliacao('Ciro', 10)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()