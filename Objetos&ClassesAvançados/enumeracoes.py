#classes avançadas
#define enumerations using the Enum base class
#podemos criar enumerações automaticamente com import de auto

from enum import Enum, auto

#defina a classe fruta que herda de Enum
class Fruta(Enum):
    UVA = 1
    BANANA = 2
    LARANJA = 3
    TOMATE = 4
    PERA = auto()

def main():
    #Objetos enum possuem valores e tipos de facil leitura
    print(Fruta.UVA)
    print(type(Fruta.UVA))
    print(repr(Fruta.UVA))

    #Objetos enum possuem propriedades "name" (nome) e "value" (valor)
    print(Fruta.UVA.name, Fruta.UVA.value)

    #Mostrar o valor gerado automaticamente para PERA
    print(Fruta.PERA.value)

    #E possivel usar objetos enum como chaves
    frutas = dict()
    frutas[Fruta.BANANA] = "Casca amarela"
    print(frutas[Fruta.BANANA])

main()