#orderedDict é uma subclasse do dicionario
#usando objetos orderedDict

from collections import OrderedDict

def main():
    #Lista de times com numeros de partidas vitorias e derrotas
    times_fut = [("Cruzeiro",(18,12)),("Vasco",(24, 6)),("Avai",(20,10)),("Flamengo",(22,8)),("Palmeiras",(15,15)),("Santos",(20,10)),("Botafogo",(16,14)),("Fluminense",(25,5))]

    #ordenando times pela quantidade de vitorias
    times_ord = sorted(times_fut, key=lambda t: t[1][0], reverse=True)

    #crie um dicionario ordenado
    times = OrderedDict(times_ord)
    print(times)

    #usar popitem para remover o item do topo
    nome, estatistica =  times.popitem(False)
    print("Time mais vitorioso: ", nome, estatistica)

    #faça um teste de igualdade
    a = OrderedDict({"a":1,"b":2,"c":3})
    b = OrderedDict({"a": 1, "b": 2, "c": 3})
    print("Teste de igualdade", a==b )


main()