class Pai:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __str__(self):
        return f'Nome: {self.nome} - Idade: {self.idade}'

class Filho(Pai): 

    def __init__(self, nome, idade, pai):
        super().__init__(nome, idade)
        self.pai = pai

    def __str__(self):
        super().__str__
        return f'Filho: {self.nome} \nPai: {pai}'



if __name__ == '__main__': 

    pai = Pai('Alvando', 64)
    print(pai)
    
    filho = Filho('Andressa', 23, pai)
    print(filho)


