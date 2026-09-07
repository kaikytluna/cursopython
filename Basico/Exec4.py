nome= input("Insira seu nome: ")
idade= input("Insira sua idade: ")
qnt_de_letras= len(nome)

if not nome and not idade:
    print("Desculpe, você deixou campos vazios")
else:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome [::-1]}")
    if " " in nome:
        print(f"Seu nome contém espaços")
    else:
        print("Seu nome não contém espaços")
    print(f"Seu nome tem {qnt_de_letras} letras")
    print(f"A primeira letra do seu nome é {nome [0]}")
    print(f"A ultima letra do seu nome é {nome [-1]}")
    print(f"Você tem {idade} anos.")