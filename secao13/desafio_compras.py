class Pessoa: 

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'Nome: {self.nome} \nIdade: {self.idade}'
    
    def is_adulto(self):
        if self.idade >= 18:
            return 'É adulto'
        else: 
            return 'Não é adulto'
        

class Vendedor(Pessoa):

    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario


class Cliente(Pessoa):

    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    def registrar_compras(self, compra):
        self.compras.append(compra)

    def get_data_ultima_compra(self): 
        datas = []

        for compra in self.compras:
            if isinstance(compra, Compra):
                datas.append(compra.data)

        return f'A ultima compra é {min(datas)}'

    def total_compras(self):
        return f'O total de compras é: {len(self.compras)}'
    

class Compra():

    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor 
        self.data = data
        self.valor = valor


if __name__ == '__main__':
    vendedor = Vendedor('Andressa', 23, 1.800)
    cliente = Cliente('Maria', 18)
    cp1 = Compra(vendedor, '2025-01-01', 18)
    cp2 = Compra(vendedor, '2024-01-01', 18)

    cliente.registrar_compras(cp1)
    cliente.registrar_compras(cp2)


    print(f'Vendedor: {vendedor}')
    print(f'Cliente: {cliente}')
    print(cliente.total_compras())
    print(cliente.get_data_ultima_compra())