"""
Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras ou menos escreva " Seu nome é curto"
se tiver 5 e 6 letras , escreva " Seu nome é normal" maior que 6 " Seu nome é muito grande"
"""

nome=input("Insira seu nome: ")
qntnome=len(nome)

if qntnome >=1:
    if qntnome<=4:
        print("Seu nome é curto")
    elif qntnome==5 or qntnome==6:
        print("Seu nome é normal")
    elif qntnome>6:
        print("Seu nome é muito grande")

if qntnome==0:
    print("Digite alguma coisa")
