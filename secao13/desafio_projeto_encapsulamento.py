from datetime import datetime, timedelta

class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()
    
    def __iadd__(self, tarefa):
        tarefa.dono = self
        self._add_tarefa(tarefa)
        return self

    def _add_tarefa(self, tarefa, **kwargs):
        self.tarefas.append(tarefa)
    
    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))

    def add(self, tarefa, vencimento=None, **kwargs):
        if isinstance(tarefa, Tarefa):
            funcao_escolhida = self._add_tarefa
        else: 
            funcao_escolhida = self._add_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)

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
        self.dono = None
    
    def concluir(self):
         super().concluir()
         novo_vencimento = datetime.now() + timedelta(days=self.dias)
         nova_tarefa =  TarefaRecorrente(self.descricao, novo_vencimento, self.dias)

         if self.dono:
             self.dono += nova_tarefa

         return nova_tarefa

def main():
    casa = Projeto('Tarefas de casa')
    casa.add('Passar roupa', datetime.now() + timedelta(days=3, minutes=12))
    casa.add('Lavar prato', datetime.now())
    casa.add('Arrumar a cama')
    casa += (TarefaRecorrente('Trocar Lençois', datetime.now()) )
    casa.procurar('Trocar Lençois').concluir()

    print(casa)

    casa.procurar('Arrumar a cama').concluir()

    for i in casa:
        print(f'- {i}')

    print(casa)
    
if __name__ == '__main__':
    main()