# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# region exec1

# def multi(*args):
#     total=1
#     for numero in args:
#         total *= numero
#     return total

# resultado=multi(1,2,3,4,5)
# print(resultado)

# endregion

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

# region exec2

x=(int(input("Insira um valor: ")))
# x=7
def par(x):
    par=None
    if x % 2 == 0:
        par=True
        return par
    
    par=False
    return par

resultado=par(x)

if resultado:
    print(f"O valor de {x} é par")
else:
    print(f"O valor de {x} é impar")

# endregion