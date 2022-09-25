#lista encadeada ou lista duplamente terminada
#Deques sao filas duplamente terminadas

import collections
import string

def main():
    #Inicialize um deque com letras minusculas
    letrinhas = collections.deque(string.ascii_lowercase)

    #Deques suportam metodo len(), mostre o tamanho da deque
    print(len(letrinhas))

    #Itere sobre a deque criada separando por ","
    for letra in letrinhas:
        print(letra.upper(),end=",")

    #manipule os itens em qualquer um dos terminais
    letrinhas.pop() #removeu o ultimo item do array
    letrinhas.popleft() #removeu o primeiro item do array
    letrinhas.append(2)  #acrescenta um 2 no final do array
    letrinhas.appendleft(1) #acrescentou um 1 no começo do array
    print(letrinhas)

    #rotacione a deque
    letrinhas.rotate(10)
    print(letrinhas)

main()