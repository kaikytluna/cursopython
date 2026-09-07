"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']
# while True:

#     i=0
#     for nome in lista:
#         print(i, nome)
#         i+=1

#     nome_amais=input("Adicionar nome:")
#     lista.append(nome_amais)

indices=range(len(lista))

for indice in indices:
    print(indice)