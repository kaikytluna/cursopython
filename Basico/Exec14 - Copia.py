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
while True:

    letra_digitada=input("Insira uma letra: ")

    if len(letra_digitada)>1:
        print("Insira apenas uma letra")
        continue
    
    if letra_digitada not in senha:
        tentativas+=1

    if letra_digitada in senha:
        letras_acertadas+=letra_digitada

    senha_formada=""
    
    for letra in senha:
        if letra in letras_acertadas:
            senha_formada+=letra
        else:
            senha_formada+="*"
    print(senha_formada)

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
                letras_acertadas=""
                tentativas=0
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

        continue
