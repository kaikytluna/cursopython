"""
Exercício — Analisador de números

Faça um programa que peça ao usuário para digitar 10 números inteiros.

Depois que os 10 números forem informados, o programa deve mostrar:

A lista completa dos números.
O maior número.
O menor número.
A média dos números.
Quantos números são pares.
Quantos números são ímpares.
Uma nova lista contendo apenas os números maiores que a média.

Regras:

Use uma list para armazenar os números.
Use um for ou while para receber os números.
Não use max(), min() ou sum() — faça esses cálculos manualmente.
Não precisa usar funções (def) ainda, se você não quiser.
"""
numeros=[]
while len(numeros)<10:
    numero=(input("Insira um número: "))
    
    if numero.isdigit():
        print(f"total {len(numeros)+1}")
        print()
        numeros.append(int(numero))
        
    else:
        print("Você não inseriu um número")
        continue

# numeros=[num for num in range(1,11)]

maior_numero=numeros[0]
menor_numero=numeros[0]
pares=[num for num in numeros if num % 2==0]
impares=[num for num in numeros if num % 2!=0]
maior_que_media=[]
soma=0


for numero in numeros:

    if numero>maior_numero: # set de maior numero
        maior_numero=numero

    if numero<menor_numero: # set de menor numero
        menor_numero=numero

    soma=numero+soma

media=soma/len(numeros)

maior_que_media=[num for num in numeros if num>media]

"""
A lista completa dos números.
O maior número.
O menor número.
A média dos números.
Quantos números são pares.
Quantos números são ímpares.
Uma nova lista contendo apenas os números maiores que a média."""

print("Lista completa:", numeros)
print("Maior número:", maior_numero)
print("Menor número:", menor_numero)
print("Média:", media)
print("Pares:", pares, f"total de pares: {len(pares)}")
print("Ímpares", impares, f"total de impares: {len(impares)}")
print("Maiores que a media:", maior_que_media)