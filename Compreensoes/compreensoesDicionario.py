#Usando dict comprehensions


def main():
    #Definindo uma lista de temperaturas
    ctemps = [0,12,34,100]

    #use a comprehension para buildar o dicionario
    #dica: formula para converter para Fahrenheit -> (t * 9/5)+32
    dicio_temp = {t:(t * 9/5)+32 for t in ctemps if t < 100}
    print(dicio_temp)

    #acessar um valor especifico
    print(dicio_temp[12])

if __name__ == "__main__":
    main()