#PROGRAMA VAI SIMULAR UM CAIXA ELETRONICO
#INSERIR NUMERO DA CONTA
#INSERIR NUMERO DA AGENCIA
#INSERIR SENHA
#SE SENHA CORRETA ESCREVER SENHA CORRETA
#SOLICITAR VALOR A SACAR
#SE SALDO DISPONIVEL > SACAR COM SUCESSO
#MOSTRAR SALDO RESTANTE
#SE SAQUE FOR MAIOR QUE SALDO PROIBIR SAQUE

conta_var = int(input("Digite o numero da sua conta: "))
print("Sua conta é: ",conta_var)
agencia_var = int(input("Digite o numero da sua agência: "))
print("Sua agência é: ",agencia_var)
senha_var = int(input("Digite sua senha: "))

if senha_var==1234:
    print ("Senha correta!")
    saldo = 1000
    while saldo > 0:
        saque = int(input("Qual valor deseja sacar? "))
        if saque > saldo:
            print("Você não tem saldo o bastante.")
        else:
            print("Saque realizado com sucesso! ")
            saldo = saldo - saque
            print("Seu saldo agora é: {}".format(saldo))
    else:
        print("Acabou seu saldo")
else:
    print ("Senha inválida!")
    print ("Refaça a operação!")



