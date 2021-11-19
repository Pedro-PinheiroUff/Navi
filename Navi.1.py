# Definir a função mmc(mínimo múltiplo comum)
def mmc(lista):
    lista = sorted(lista)
    flag = False
    i = 0
    while flag is not True:
        flag = True
        i += 1
        for el in lista[:-1]:
            if (i * lista[-1]) % el != 0:
                flag = False
    return i*lista[-1]

# Números utilizados
numeros= [37,49,2]

# Criar uma váriavel com o resultado do mmc dos numeros utilizados
Mmcnumeros = mmc(numeros)
limite= 5000000
mult= 0
num=1
# Para fazer a contagem de quantos múltiplos existem, vemos quantos numeros existem menores que o limite, quando multiplicados pelo mmc
while num<limite:
    mult += 1
    num = Mmcnumeros * mult
# Como a contagem vem com uma contagem a mais, faz-se a diminuição de 1 unidade
print(mult-1)














