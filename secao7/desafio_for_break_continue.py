from random import randint

def sortear_dado():
    return randint(1,6)


for i in range(1,7):
    if (i % 2) != 0:
        continue
    else:
        valor = sortear_dado()
        
        if i == valor: 
            print('ACERTOU! {}'.format(i))
            break
else: 
    print('Não acertou')