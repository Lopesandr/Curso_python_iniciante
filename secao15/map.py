lista_nomes = [
                {'nome': 'João', 'idade': 30},
                {'nome': 'Maria', 'idade': 37},
                {'nome': 'José', 'idade': 26}
              ]

so_nome = map(lambda n: n['nome'], lista_nomes)
print(list(so_nome))

so_idade = map(lambda p : p['idade'], lista_nomes)
print(list(so_idade))


nome_idade = map(lambda n: f'{n['nome']} tem {n['idade']} anos', lista_nomes)

print(list(nome_idade))