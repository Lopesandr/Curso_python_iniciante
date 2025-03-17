from datetime import datetime, timedelta

class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))

    def pendentes(self):
        return[tarefa for tarefa in self.tarefas if not tarefa.feito]
    
    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas 
                            if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefas pendentes)'
    

class Tarefa: 
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []

        if self.feito:
            status.append('(Concluida)')

        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em dias {dias})')

        return f'{self.descricao} '  + ' '.join(status)
    

class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento=None, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias
    
    def concluir(self):
         super().concluir()
         novo_vencimento = datetime.now() + timedelta(days=self.dias)
         return TarefaRecorrente(self.descricao, novo_vencimento, self.dias)

def main():
    casa = Projeto('Tarefas de casa')
    casa.add('Passar roupa', datetime.now() + timedelta(days=3, minutes=12))
    casa.add('Lavar prato', datetime.now())
    casa.add('Arrumar a cama')
    casa.add(TarefaRecorrente('Trocar Lençois', datetime.now()).concluir())

    print(casa)

    casa.procurar('Arrumar a cama').concluir()

    for i in casa:
        print(f'- {i}')

    print(casa)
    
if __name__ == '__main__':
    main()