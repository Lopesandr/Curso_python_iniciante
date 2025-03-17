def dias_semana(dia):
    if dia in  range(6, 8):
        return "Final de semana"
    elif dia in range(1,6):
        return 'Dia da semana'
    else: 
        return 'Numero inválido'
    


if __name__ == '__main__': 
    print(dias_semana(8))