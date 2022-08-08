lista = [12, 19, 27, 30, 38, 44, 56, 65]
achou = False



valor = int(input("digite: "))
tam = len(lista)

for i in range(tam):
    if lista[i] == valor:
        achou = True;
        lindex = i;

if achou == True:
    print(f'Dado achado na posiÃ§Ã£o {lindex}')
elif achou == False:
    print('Dado nÃ£o achado!')
