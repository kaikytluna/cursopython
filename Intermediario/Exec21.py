from copy import deepcopy

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def inflação(preco):
    acrescimo=(10/100)*preco
    return preco+acrescimo

for produto in produtos:
    preco=float(produto['preco'])
    preco_novo=inflação(preco)
    produto['preco']=round(preco_novo,2)
    # print(preco)



novos_produtos=deepcopy(produtos)
produtos_ordenados_por_nome=sorted(deepcopy(novos_produtos), key= lambda item: item['nome'] , reverse=True)
produtos_ordenados_por_preco=sorted(deepcopy(novos_produtos), key= lambda item: item['preco'])


print("Novos produtos:")
print(*novos_produtos, sep="\n")
print("")

print("Produtos ordenados por nome decrescente:")
print(*produtos_ordenados_por_nome, sep="\n")
print("")

print("Produtos ordenados por preço:")
print(*produtos_ordenados_por_preco, sep="\n")
# novos_produtos=deepcopy(sorted(*produtos))
# print(*novos_produtos)

# for dic in novos_produtos:
#     print(*novos_produtos)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)