#Packing
def retorna_lista(*args):
    print(args)
    for i in args:
        print(i)

def retonra_dicionario(**kwargs):
    print(kwargs)

retorna_lista(1,2,3, 'Packing')
retonra_dicionario(numero = 1,
                   numero_extenso = 'um')
 
#Unpacking

args = [1, 2, 3, 4, 5]
print(*args)

def retorna_dict (numero, numero_extenso): 
    print(f'Numero: {numero} \nNumero por extenso {numero_extenso}')

kwars = {'numero': 1, 
         'numero_extenso': 'um'}

retorna_dict(**kwars)
