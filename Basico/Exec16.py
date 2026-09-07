"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os
lista=["Açai"]

while True:
    print("Lista de compras")
    comando=input("O que você deseja fazer? [i]nserir [a]pagar [l]istar: ")
    comandos="ial"
    item_removido=""
    if comando in comandos and len(comando)==1:

        if comando=="i":
            os.system("cls")
            item_novo=input("Digite seu item: ")
            lista.append(item_novo)
            print(f"O item {item_novo} foi adicionado a lista.")

        if comando=="a":
            for indice, item in enumerate(lista):
                print(indice, item)
            try:
                indice_removido=(input("Digite o indice do item que deseja remover: "))
                indice_item=int(indice_removido)

                if indice_item>len(lista):
                    print("Indice inválido.")
                    continue

                item_removido=lista[indice_removido]
                lista.remove(item_removido)
                print(f"O item {item_removido} foi removido da lista.")

            except:
                print("Você não digitou um indice.")
                continue

        if comando=='l':
            if len(lista)>=1:
                for indice, item in enumerate(lista):
                    print(indice, item)
            else:
                print("A lista está vazia")
                print()

    else:
        os.system('cls')
        print("Insira um dos comandos!")
        print()