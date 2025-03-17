class Pessoa: 

    def __init__(self, nome, idade): 
        self.nome = nome
        self.idade = idade
    
    def maior_idade(self): 
        if self.idade >= 18: 
            return 'É de maior'
        else:
            return 'É de menor'
        

    @staticmethod
    def genero():
        return['Feminino', 'Masculino']


    @classmethod
    def verifica_sigla(cls, sigla):
        for genero in cls.genero(): 
            if sigla == genero[0]:
                return genero
            
    
if __name__ == '__main__':
    print(Pessoa('Vânia', 33).verifica_sigla('M'))