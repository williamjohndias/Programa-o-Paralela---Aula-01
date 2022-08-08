lista = [12, 19, 27, 30, 38, 44, 56, 65]
achou = False
procura = True
tam = len(lista)
j = 0
valor = int(input("digite: "))


while procura == True:
    j = j + 1
    if j >= tam:
        procura = False
    else:
        procura = lista[j] != valor

if j <= tam:
    achou = True


if achou == True:
    print(f'Dado achado na posiÃ§Ã£o {j}')
elif achou == False:
    print('Dado nÃ£o achado!')
