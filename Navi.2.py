import math
from functools import reduce


# Definindo a função fatorial recursivamente

def fatorial(n):
    if n > 1:
        return n * fatorial(n - 1)
    else:
        return 1

# Definindo a função que ordenará o vetor

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        return quickSort([x for x in arr[1:] if x < arr[0]]) + [arr[0]] + quickSort([x for x in arr[1:] if x >= arr[0]])


if __name__ == "__main__":

    x = []

    # Criando o vetor com as posições pares e ímpares

    for i in range(10):
        if i % 2 == 0:
            x.append(3 ** i + 7 * fatorial(i))
        else:
            x.append(2 ** i + 4 * math.log(i))

    #  Para selecionar o maior elemento, iremos pegar o index do maior valor em relação ao vetor x

    x_ord = quickSort(x)
    posição_max= x.index(x_ord[-1])

    # Somando todos os termos e dividindo pelo tamanho do vetor

    media_x = round(reduce(lambda a, b: a + b, x) / len(x), 2)
    print(media_x)
    print(posição_max)
