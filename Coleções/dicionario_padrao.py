#usando objetos defaultdict
import collections

#Dicionário em Python é uma coleção não ordenada de valores de dados que são usados
# para armazenar valores de dados como um mapa. Ao contrário de outros Tipos de Dados que contêm apenas um valor como elemento,
# o Dicionário contém um par chave-valor. No Dicionário, a chave deve ser exclusiva e imutável.

def main():
    #Definindo uma lista de itens para contar
    frutas = ['maçã','pera','laranja','banana','maça','uva','banana','banana']

    #Use um dicionário default para contar cada elemento
    contador_frutas = collections.defaultdict(int)

    #conte os elementos da lista
    for fruta in frutas:
        contador_frutas[fruta] += 1

    # Faça o print do resultado
    for (c,v) in contador_frutas.items():
        print(c + ":"+str(v))

main()