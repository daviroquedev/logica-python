#Usando metodos mágicos para comparar objetos entre si

class Pessoa():
    def __init__(self, nome, sobrenome, nivel, anos_trabalhados):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nivel = nivel
        self.senioridade = anos_trabalhados

    # Implemente as comporações usando o nivel de cada pessoa
    def __ge__(self,other):
        if self.nivel == other.nivel:
            return self.senioridade >= other.senioridade
        return self.nivel >= other.nivel

    def __gt__(self, other):
        if self.nivel == other.nivel:
            return self.senioridade > other.senioridade
        return self.nivel > other.nivel

    def __lt__(self, other):
        if self.nivel == other.nivel:
            return self.senioridade < other.senioridade
        return self.nivel < other.nivel

    def __le__(self, other):
        if self.nivel == other.nivel:
            return self.senioridade <= other.senioridade
        return self.nivel <= other.nivel






def main():
    #Definindo pessoas
    #append = acrescentar
    dpto = []
    dpto.append(Pessoa("Tulio","Toledo", 5,9))
    dpto.append(Pessoa("João","Junior", 4,12))
    dpto.append(Pessoa("Jessica","Temporal", 6, 6))
    dpto.append(Pessoa("Rebeca","Robison", 5, 13))
    dpto.append(Pessoa("Davi","Roque", 6,10))

    #descobrindo quem é mais senior
    print(dpto[0] > dpto[4])
    print(dpto[3] > dpto[1])

    #organizando as pessoas  por senioridade
    pessoas = sorted(dpto)
    for pessoa in pessoas:
        print(pessoa.nome)

if __name__ == "__main__":
    main()