import itertools

def primeiro_filtro(x):
    if x %2 == 0:
        return False
    else:
        return True

def segundo_filtro(x):
    if x.isupper():
        return False
    return True

def quadrado(numero):
    return numero ** 2

def nota_para_conceito(x):
    if x >= 90:
        return "A"
    elif ( x >= 80 and x < 90):
        return"B"
    elif (x >= 70 and x < 80):
        return "C"
    elif (x >= 65 and x < 70):
        return "D"
    return "F"

def condicao(x):
    return x < 40

def main():
    #definindo sequencia para usarmos nesta tarefa
    numeros=(1,8,4,3,5,13,11, 133, 121, 26,493,200,210,32,44)
    letras ="abcDeFGhiJkLmnOp"
    notas =(81,89,94,78,61,66,99,74)


    #usar filter para remover itens de uma lista
    impares = list(filter(primeiro_filtro,numeros))
    print(impares)

    # usar filter para remover itens de uma lista
    minusculas = list(filter(segundo_filtro,letras))
    print(minusculas)

    # usar map para criar uma nova sequencia de valores

    quadrados = list(map(quadrado,numeros))
    print("aqui é os quadrado {0}".format(quadrados))

    # Usar sorted e map para mudar as notas para conceitos
    notas = sorted(notas)
    conceitos = list(map(nota_para_conceito,notas))
    print(conceitos)

    #Iteradores do módulo itertools

    pessoas = ["Jessica","Leticia","Gustavo"]
    ciclo = itertools.cycle(pessoas)
    print(next(ciclo))
    print(next(ciclo))
    print(next(ciclo))
    print(next(ciclo))

    #contador com itertools
    contador = itertools.count(100,10)
    print(next(contador))
    print(next(contador))
    print(next(contador))
    print(next(contador))

    #Função accumulate cria um iterador que acumula valores
    valores = [10,20,30,40,50,40,30]
    acumulado = itertools.accumulate(valores)
    print(list(acumulado))

    #Função accumulate cria um iterador que acumula valores com Max

    acumuladoMax = itertools.accumulate(valores,max)
    print(list(acumuladoMax))

    #função chain para conectar listas //lista com todos os valores em uma lista

    x = itertools.chain("ABCD","1234")
    print(list(x))

    #as funçoes dropwhile e takewhile vai retornar valores ate que
    #uma condicao seja atingida

    print(list(itertools.dropwhile(condicao,valores)))
    print(list(itertools.takewhile(condicao, valores)))


main()