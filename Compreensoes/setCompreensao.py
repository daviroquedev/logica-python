#usando set comprehensions

def main():
    #definindo uma lista de temperaturas
    ctemps = [5,10,12,14,10,23,41,30,12,24,12,18,29]

    #crie um set com as temperaturas em Fahrenheit
    #dica formula para converter para fahrenheit -> (t *9/5)+32

    #compreensao lista
    ftemp_lista = [(t *9/5)+32 for t in ctemps]
    print(ftemp_lista)
    #//apresenta repetições
    #comprensao sets
    ftemp_set = {(t *9/5)+32 for t in ctemps}
    print(ftemp_set)
    #//sem repetições

    #crie um set a partir de uma string
    frase = "O primeiro podcast brasileiro sobre ciencias de dados"
    letras = {l.upper() for l in frase if not l.isspace()}
    #tirando os espaço em branco "if not l.isspace()"
    print(letras)
 

if __name__ == "__main__":
    main()