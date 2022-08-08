lista = [12, 19, 27, 30, 38, 44, 56, 65]
achou = False
tam = len(lista)
j = 1
valor = int(input("digite: "))
#lista[tam] = valor



while lista[j] != valor:
    j = j + 1

achou = j != lista[j]

if achou == True:
    print(f'Dado achado na posiÃ§Ã£o {j}')
elif achou == False:
    print('Dado nÃ£o achado!')
