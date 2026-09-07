import os
import random

# lista_senhas=[
# 'caroline',
# 'suy'
# ]
# senha=random.choice(lista_senhas)
# senha="123"

# region Tirado do chat gpt, ainda não entendo

with open("senhas.txt", "r", encoding="utf-8") as arquivo:
    lista_senhas = arquivo.read().splitlines()

senha = random.choice(lista_senhas)

# endregion

tentativas=0
letras_acertadas=""
sair=""
vidas=5
tam_senha=len(senha)
sem_vida=None
letras_ja_digitadas=""
try_again=None

print("Esse é o jogo da senha, você precisa adivinhar uma palavra aleatória que possui" , tam_senha,
    "letras, e você possui 6 vidas.")

while True:

# region try_again
    while try_again:
        tentativas=0
        letras_acertadas=""
        sair=""
        vidas=5
        tam_senha=len(senha)
        sem_vida=None
        letras_ja_digitadas=""
        try_again=None
        outra_chance="..."
        senha = random.choice(lista_senhas)
        tam_senha=len(senha)
        print("Esse é o jogo da senha, você precisa adivinhar uma palavra aleatória que possui" , tam_senha,
                "letras, e você possui 6 vidas.")
# endregion

    letra_digitada=input("Insira uma única letra: ")

# verificação do algoritmo digitado

    if len(letra_digitada)>1:
        print("Insira apenas uma letra.")
        continue

    if letra_digitada=="":
        print("Você precisa digitar algo.")
        continue

    if letra_digitada in letras_ja_digitadas:
        print("Você ja digitou esta letra.")
        continue

# lógica da senha

    if letra_digitada not in senha:
        tentativas+=1

    if letra_digitada in senha:
        letras_acertadas+=letra_digitada

    senha_formada=""
    
    for letra in senha:
        if letra in letras_acertadas:
            senha_formada+=letra
            continue
        else:
            senha_formada+="*"
            continue
    print(senha_formada)

# Vidas restantes

    if letra_digitada not in senha:

        if vidas==1:
            print("Você errou, agora só te resta 1 vida.")
            vidas-=1
            sem_vida=True
            continue

        if 1<vidas<=5:
            print(f"Você errou, agora você possui somente {vidas} vidas")
            vidas-=1

    if sem_vida:
        print("As suas vidas acabaram.")
        print("A palavra era", senha)
        outra_chance=input("Você deseja tentar novamente? [s]im ou [n]ão:").lower()
        if outra_chance=='sim' or outra_chance=='s':
            os.system('cls')
            try_again=True
            continue
        elif outra_chance=="não" or outra_chance=="nao" or outra_chance=="n":
            print("Encerrando o programa.")
            break
    letras_ja_digitadas+=letra_digitada

# Senha correta e reset

    while senha_formada==senha:
        resposta=['sim', 's', 'não', 'nao', 'n']
        if senha_formada==senha:
            os.system('cls')
            print(f"Parabéns, você conseguiu acertar a senha")
            if tentativas==1:
                print(f'A senha era "{senha}", e você errou apenas {tentativas} vez.')
            elif tentativas>1:
                print(f'A senha era "{senha}", e você errou {tentativas} vezes.')
            else:
                print(f'A senha era "{senha}", e você não errou nenhuma vez.')
            sair=input("Você deseja tentar novamente? [s]im ou [n]ão:").lower()
            if sair=="não" or sair=="nao" or sair=="n":
                break
            elif sair=="sim" or sair=="s":
                break
            while sair not in resposta:
                print("Insira apenas sim ou não!")
                sair=input("Você deseja tentar novamente? [s]im ou [n]ão:").lower()
                break
            if sair in resposta:
                letras_acertadas=""
                tentativas=0
                break
    if sair=="não" or sair=="nao" or sair=="n":
        print("Encerrando o programa.")
        break
    elif sair=="sim" or sair=="s":
        try_again=True
        os.system('cls')
        continue

        # continue
    # elif sair=="sim" or sair=="s":
    #     os.system('cls')
    #     senha = random.choice(lista_senhas)
    #     tam_senha=len(senha)
    #     print("Esse é o jogo da senha, você precisa adivinhar uma palavra aleatória que possui" , tam_senha,
    #             "letras, e você possui 6 vidas.")
    #     continue