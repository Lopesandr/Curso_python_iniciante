
nota = input("Digite a nota do aluno: ")
nota = float(nota)

if nota < 0 or nota > 10:
    print("Nota inválida")

elif nota > 9.1 and nota <= 10:
    print('O conceito é A')

elif nota > 8.1 and  nota <= 9:
    print('O conceito é A-')

elif  nota >=  7.1 and nota <= 8:
    print('O conceito é B')

elif nota >= 6.1 and nota <= 7:
    print('O conceito é B-')

elif nota >= 5.1 and nota <= 6:
    print('O conceito é C')

elif nota >= 4.1 and nota <= 5:
    print('O conceito é C-')

elif nota >= 3.1 and nota <= 4:
    print('O conceito é D')

elif nota >= 2.1 and nota <= 3:
    print('O conceito é D-')

elif nota >= 1.1 and nota <= 2:
    print('O conceito é E')

elif nota >= 0 and nota <= 1:
    print('O conceito é E-')