"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou impar.
Caso o usuario não digite um número interio, informe que não é um número interio.
"""

numero=(input("Digite um número inteiro: "))

if numero.isdigit():
    numero_int=int(numero)
    par_impar="impar"
    num_par= numero_int % 2 == 0
    if num_par:
        par_impar= "par"
    print(f"O número {numero} é {par_impar}")
else:
    print("Você não digitou um número inteiro")




