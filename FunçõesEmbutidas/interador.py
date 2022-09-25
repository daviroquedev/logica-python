
dias = ["DOM","SEG","TER","QUA","QIN","SEX","SAB"]
dias_en = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]

#use a funçao inter para criar um iterador sobre a lista

iterador_dias = iter(dias)
print(next(iterador_dias))
print(next(iterador_dias))
print(next(iterador_dias))
print(next(iterador_dias))

with open('Pycaret/dados.txt','r') as fp:
    for linha in iter(fp.readline,''):
        print(linha)

# FUNCAO RANGE ENUMERA OS INDEX DOS ITENS DA LISTA ENUMERANDO-OS

for numero in range(len(dias)):
    print(numero,dias[numero])

# FUNCAO ENUMERATE INDEX OS ITENS DA LISTA

for i,dia in enumerate(dias):
    print(i,dia)


# FUNÇÃO ZIP JUNTA DUAS LISTAS

for d in zip(dias, dias_en):
    print(d)

# COMBINAR O ZIP COM O ENUMERATE PARA FORMATAR OS RESULTADOS

for i,d in enumerate(zip(dias,dias_en)):
    print(i, d[0],"=",d[1],"em ingles")