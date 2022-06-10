def calculadora():
  x=float(input('Digite um valor: '))
  operador=input('Digite um operador matématico: ')
  
  # FUNÇAO SOMAR
  if operador=='+':
     y=float(input('Digite um valor: '))
     somar(x,y)
     encerrar()
  # FUNÇÃO DIMINUIR
  elif operador =='-':
     y=float(input('Digite um valor: '))
     subtracao(x,y)
     encerrar()
  # FUNÇÃO MULTIPLICAR  
  elif operador =='*':
     y=float(input('Digite um valor: '))
     multiplicar(x,y)
     encerrar()
  # FUNÇÃO DIVIDIR
  elif operador == '/' or o==':':
     y=float(input('Digite um valor: '))
     dividir(x,y)
     encerrar()
  # FUNÇÃO PORCENTAGEM
  elif operador=='%':
    porcentagem(x)
    encerrar()
  elif operador=='fim':
    print('fim')
  else:
    print('Operador invalido')
    encerrar()

# fim da funçao calculadora

def somar(x,y):
  print('SOMA',x+y)

def subtracao(x,y):
  print('SUBTRAÇÃO', x-y)

def multiplicar(x,y):
  print('MULTIPLICAÇÃO', x*y)

def dividir(x,y):
  print('DIVIDIR', x/y)

def porcentagem(x):
  print('PORCENTAGEM',x/100,'%')

def encerrar():
  continuar = input('Deseja fazer outra operação? 1- SIM 2-NÃO: ')
  if(continuar == '1'):
    calculadora()
  elif(continuar == '2'):
    print('Calculadora desligada')
  else:
    print('Comando inválido')
    encerrar()

calculadora()
