from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = [] 

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._avaliacoes = []
        self._status = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Nome: {self._nome} | Categoria: {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print('Nome do Restaurante'.ljust(24), 'Categoria'.ljust(24), 'Avaliações'.ljust(24) , 'Status', sep = '|')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(24)}|{restaurante._categoria.ljust(24)}|{str(restaurante.calcular_media_avaliacoes).ljust(24)}|{restaurante.status}')

    @property
    def status(self):
         return '⌧' if self._status else '☐' 

    def ativar(self):
        self._status = not self._status;

    def adicionar_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacoes.append(avaliacao)

    @property
    def calcular_media_avaliacoes(self):
        if not self._avaliacoes:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        quantidade_de_avaliacoes = len(self._avaliacoes)
        media = round(soma_das_notas / quantidade_de_avaliacoes, 1)
        return media