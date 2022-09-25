from collections import Counter

#usando a classe counter

def main():
    #lista turma a
    turma_a = ["Barbara","João","Carlos","Dário","Priscila","Davi","Jose","Fran","Larissa","João Paulo","João","Joao"]

    #lusta turma b
    turma_b = ["Hiro","Bruno","Claudia","Debora","Fernanda","Gabriela","Let","Adamastopitaco","Joao","Joao vitor"]

    #Crie um counter para as turma A e B
    a = Counter(turma_a)
    b = Counter(turma_b)

    #Counter é uma subclasse discionario

    #Quantos estudantes na turma A se chamam joao?
    print(a["João"])
    #//2

    #Quantos estudantes estão na turma A?
    print(sum(a.values()))
    #//12

    #Combinar duas turmas
    a.update(turma_b)
    print(sum(a.values()))

   #Quais os 3 nomes mais comuns
    print(a.most_common(3))

    #Separe as 2 turmas e mostre o nome mais comum da turma A
    a.subtract(turma_b)  #subtract é = subtrair
    print(a.most_common(3))

    #Qual a intersecção de nomes entre as duas turmas  //ve oq tem de comum nas 2
    print( a & b)


main()