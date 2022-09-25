# map(fahrenheit_para_celsius, [32,65,104,212])
# é tao comum usar map retornando uma lista 
# que foi criado uma compreensao de lista que ja retorna igual a cima

#[(t*9/5)+32 for t in [32,65,104,212]]


def main():
    #Definindo duas lista de numeros impares e pares
    pares = [2,4,6,8,10,12,14,16,18,20]
    impares = [1,3,5,7,9,11,13,15,17,19]

    #use map() e list() para calcular numeros ao quadrado
    pares_quadrado = list(map(lambda n: n**2,pares))
    print(pares_quadrado)

    #cria uma lista nova a partir de uma lista preexistente
    #forma mais simples mesmo resultado de acima
    pares_quadrado2 = [n ** 2 for n in pares]
    print(pares_quadrado2)

    #Use o predicado para limitar os itens com filtro
    impares_quadrado = [n**2 for n in impares if n > 7 and n < 15]
    print(impares_quadrado)


if __name__ == "__main__":
    main()