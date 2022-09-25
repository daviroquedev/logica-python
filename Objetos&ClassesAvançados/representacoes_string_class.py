#Personalizando representações de string de classes
#controlando como o objeto é representado

class Pessoa():
    def __init__(self):
        self.nome="Davi"
        self.sobrenome="Roque"
        self.idade=28

    #Use __repr__ para  criar uma string que seja útil para debug
    def __repr__(self):
        texto ="<Classe Pessoa - nome: {0}, sobrenome: {1}, idade{2}>"
        return texto.format(self.nome,self.sobrenome,self.idade)

    #Use __str__ para criar uma string amigável para humanos
    def __str__(self):
        texto = "Pessoa {0} {1} tem {2} anos"
        return texto.format(self.nome,self.sobrenome,self.idade)
    #Use bytes para converter a string em um objeto bytes
    def __bytes__(self):
        dados = [self.nome,self.sobrenome,self.idade]
        para_bytes = "Pessoa:{0}:{1}:{2}".format(*dados)
        return para_bytes.encode('utf-8')

def main():
    #Criando uma istancia pessoa
    pessoa = Pessoa()
    print(repr(pessoa))
    print(str(pessoa))
    print("Formatado: {0}".format(pessoa))
    print(bytes(pessoa))

main()