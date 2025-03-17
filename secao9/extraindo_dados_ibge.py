from urllib import request
import csv 

def read(url):
    #Baixando o csv direto do site de origem dele
    with request.urlopen(url) as entrada:
        print('Baixando csv...\n')

        #Decotificando para o tipo latin1
        dados = entrada.read().decode('latin1')
        print('Download completo!\n')

        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')

read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv') 