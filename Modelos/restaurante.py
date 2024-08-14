class Restaurante:
    restaurantes = [] 

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._status = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Nome: {self._nome} | Categoria: {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print('Nome do Restaurante'.ljust(24), 'Categoria'.ljust(24), 'Status', sep = '|')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(24)}|{restaurante._categoria.ljust(24)}|{restaurante.status}')

    @property
    def status(self):
         return '⌧' if self._status else '☐'

    def ativar(self):
        self._status = not self._status;


careca = Restaurante('Careca', 'chinesa')
spoleto = Restaurante('Spoleto', 'italiana')

spoleto.ativar()
Restaurante.listar_restaurantes()