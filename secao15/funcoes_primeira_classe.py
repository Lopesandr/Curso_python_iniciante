def dobro(x):
    return x * 2 

def quadrado(x):
    return x**2

def executa_fuction(func, x):
    return f'{func.__name__} - {func(x)}'

if __name__ == '__main__':
    #Armazenando as funções em uma lista
    print(executa_fuction(dobro, 2))