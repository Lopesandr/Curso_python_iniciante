lista_nomes = [
                {'nome': 'João', 'idade': 30},
                {'nome': 'Maria', 'idade': 37},
                {'nome': 'José', 'idade': 26},              
                {'nome': 'Isa', 'idade': 2},
                {'nome': 'Gabriela', 'idade': 8},


              ]



menores_idade = filter(lambda n: n['idade'] < 18, lista_nomes)

print(list(menores_idade))

nomes_com_6_carac = filter(lambda n: len(n['nome']) >= 7, lista_nomes)

print(list(nomes_com_6_carac))