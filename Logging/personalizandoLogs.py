# personalizando retorno do logging
import logging

dados = {"pessoa":"Davi"}

#Crie uma outra função para rodar o log
def outra_funcao():
    logging.info("Esta é uma mensagem de informação",extra=dados)





def main():
    #Defina o nivel de log para debug e um arquivo para salvar
    #o retorno. Use uma formatação personalizada

    #Criar uma string de formatação para personalizar
    formato = "%(asctime)s:%(levelname)s: %(funcName)s:Pessoa:%(pessoa)s"
    #ascitime mostra data e hora.. levelname mostra o level do logging e funcName mostra qual foi a função utilzada
    logging.basicConfig(
        filename="output.log",
        level=logging.DEBUG,
        format=formato
    )

    #como passar informaçoes extra pro loggin.. com um dicionario
    #todo nivel de loggin tem um parametro extra


    logging.info("Esta é uma mensagem de informação",extra=dados)
    logging.warning("Esta é uma mensagem de aviso",extra=dados)
    outra_funcao()

if __name__ == "__main__":
    main()