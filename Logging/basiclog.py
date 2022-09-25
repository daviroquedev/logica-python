import logging
#5 niveis de logging

#logging.debug("Esta é uma mensagem de debug") -> informação util para debug
#logging.info("Esta é uma mensagem de informação") -> informações gerais sobre o funcionamento do programa
#logging.warning("Esta é uma mensagem de aviso") -> algo inesperado, ou possivel problema a caminho
#logging.error("Esta é uma mensagem de erro") -> impossivel executar uma operação especifica
#logging.critical("Esta é uma mensagem critica") -> algo que provavelmente impactara na execução do programa.

#por padrao logging sao feito dos niveis warning ou mais alto

#pode ser alterado usando basicConfig alterando o nivel

#use o modulo embutido logging


def main():
    #use basicConfig para configurar seu logging
    logging.basicConfig(level=logging.DEBUG, filename="output.log")
    #criou o arquivo output.log com os loggings

    #testando cada um dos niveis de log
    logging.debug("Esta é uma mensagem de debug")
    logging.info("Esta é uma mensagem de informação")
    logging.warning("Esta é uma mensagem de aviso")
    logging.error("Esta é uma mensagem de erro") 
    logging.critical("Esta é uma mensagem critica")


if  __name__ == "__main__":
    main()