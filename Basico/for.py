# # frase="Isabelle"
# # nova_frase=""
# # for letra in frase:
# #     nova_frase+=(f"*{letra}")
# #     print(letra)
# # print(nova_frase+"*")

# # numeros=range(-1,-26,-2)

# # for numero in numeros:
# #     print(numero)

# numeros=range(0, 52, 2)

# for numero in numeros:
#     print(numero)

for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')