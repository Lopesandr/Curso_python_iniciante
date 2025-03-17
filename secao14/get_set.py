class Pessoa: 

    def __init__(self, nome, idade): 
        self.nome = nome
        self._idade = idade
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade ):
        self._idade = idade

 
if __name__ == '__main__':
   p1 = Pessoa('Andressa', 23)

   print(p1.idade)
   p1.idade = 33
   print(p1.idade)