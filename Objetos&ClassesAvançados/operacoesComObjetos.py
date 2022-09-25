# Imitando o comportamento de numeros de uma classe

class Cordenada():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Coordenada x:{0},y:{1}".format(self.x,self.y)

    #implemente adição
    def __add__(self, other):
        return Cordenada(self.x + other.x, self.y + other.y)

    #Implemetando subtracao
    def __sub__(self, other):
        return Cordenada(self.x - other.x, self.y - other.y)

    #Implemente adição in-place
    def __iadd__(self,other):
        self.x += other.x
        self.y += other.y
        return self

def main():
    #Declare some coordenadas
    c1 = Cordenada(10,20)
    c2 = Cordenada(30,30)
    print(c1,c2)

    #Adicionar duas coordenadas
    c3 = c1 + c2
    print(c3)

    #Subtrair duas coordenadas
    c4 = c2 - c1
    print(c4)

    #Executar uma adição in-place
    c1 += c2
    print(c1)

if __name__ == "__main__":
    main()