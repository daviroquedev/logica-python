#Personalizando a representação de string de uma classe


#permitir que alguem ajuste uma cor usando a classe

class MinhasCores():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100
    #Use getattr para retornar um valor de forma dinâmica
    def __getattr__(self, attr):
        if attr == "rgb":
            return (self.red, self.green,self.blue)
        else:
            raise AttributeError
    #use setattr para retornar um valor de forma dinamica
    def __setattr__(self, attr, val):
        if attr == "rgb:":
            self.red= val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr,val)

    #Use dir para listar os atributos disponiveis
    def __dir__(self):
        return("red","green","blue","rgb")

def main():
    #criando uma istancia de minhasCores
    cores = MinhasCores()

    #Mostre o valor de um atributo
    print(cores.rgb)

    #Defina o valor de um atributo
    cores.rgb = (125,200,86)
    print(cores.rgb)

    #Acesse a atributos especifico
    print(cores.red)

    #Liste os atributos disponiveis
    print(dir(cores))

main()