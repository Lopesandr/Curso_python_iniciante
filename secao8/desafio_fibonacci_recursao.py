def fibonacci(elemento):
    lista = [0,1]
    lista.append(sum(lista[-2:]))
    
    if elemento < len(lista):
        fibonacci(elemento)
    
    print(lista)


if __name__ == '__main__':
    fibonacci(10)
     