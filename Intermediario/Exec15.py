# produtos = [
#     {'nome': 'p1', 'preco': 20, },
#     {'nome': 'p2', 'preco': 10, },
#     {'nome': 'p3', 'preco': 30, },
# ]

# novos_produtos=[
#     produto
#     if produto['preco'] > 20
#     # if produtos['preco'] > 20 else...
#     for produto in produtos
# ]

# print(*novos_produtos, sep="\n")

# numeros=[1,2,3,4,5]
# novos_numeros=[
#     numero 
#     if numero!=2 else 200
#     for numero in numeros
# ]

# print(novos_numeros)


# for x in range(1, 11):
#     for y in range(1, 6):
#         print(x, y)

nomes=['carol', 'nanda', 'isabelle', 'sarah', 'sandrielly']
nomes_up=[nome for nome in nomes]
print(nomes_up)