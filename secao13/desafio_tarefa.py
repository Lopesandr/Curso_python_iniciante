from datetime import datetime

class Tarefa: 
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' (Concluida)' if self.feito else ' ')
    

def main():
    casa = []
    casa.append(Tarefa('Passar Roupa'))
    casa.append(Tarefa('Lavar Prato'))

    [i.concluir() for i in casa if i.descricao == 'Lavar Prato']

    for i in casa:
        print(f'- {i}')

if __name__ == '__main__':
    main()