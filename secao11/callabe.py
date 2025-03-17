#Informa o nome da função e os parâmetros, realizando o empacotamento.
def retorna_funcao(funcao, *parametros):

    #Verifica se a função é um callabe, ou seja, se é uma função que esta sendo passa e não uma variavél qualquer. 
    if callable(funcao):
          #Retorna o que a funçao chamada for retornar, e é passado os parâmetros realizando o desempacotamento. 
          return funcao(*parametros)
    else:
          return 'Não existe função passada'

def soma(numero1, numero2):
	return numero1 + numero2


print(retorna_funcao(soma, 1, 2))
print(retorna_funcao(1))

