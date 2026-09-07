while True:
    numero_1=input("Insira o primeiro número: ")
    numero_2=input("Insira o segundo número: ")
    operador=input("Agora insira a operação desejada (+-/): ")

# region Conversão e Verificação de dados
    numeros_validos= None
    num_1_float=0
    num_2_float=0

    try:
        num_1_float=float(numero_1)
        num_2_float=float(numero_2)
        numeros_validos= True
    except:
        numeros_validos= None
    
    if not numeros_validos:
        print("Um ou ambos os números digitados são inválidos")
        continue

    operadores_validos= "+-/*"

    if operador not in operadores_validos:
        print("Erro no operador!")
        continue

    if len(operador)>1:
        print("Digite apenas um operador!")
        continue
# endregion

# region operação
    # if operador=="+":
    #     print(f"O resultado da operação é {num_1_float+num_2_float}")
    # if operador=="-":
    #     print(f"O resultado da operação é {num_1_float-num_2_float}")
    # if operador=="/":
    #     print(f"O resultado da operação é {num_1_float/num_2_float}")
    # if operador=="*":
    #     print(f"O resultado da operação é {num_1_float*num_2_float}")
    resultado=0
    if operador=="+":
        resultado=num_1_float+num_2_float
    if operador=="-":
        resultado=num_1_float-num_2_float
    if operador=="/":
        resultado=num_1_float/num_2_float
    if operador=="*":
        resultado=num_1_float*num_2_float    
    

    if resultado.is_integer():
        print(f"O resultado da operação é {int(resultado)}")
    else:
        print(f"O resultado da operação é {resultado}")

# endregion

# region saida
    while True:
        saida_invalida=False
        sair=input("Você quer fazer outra conta? [s]im ou [n]ão: ").lower()
        if sair=="n" or sair=="não":
            # if sair:
            break
        elif sair=="s" or sair=="sim":
            break
        else:
            print("Resposta invalida! Digite apenas [s]im ou [n]ão")
    if sair=="n" or sair=="não":
        break
# endregion

print("Você saiu da calculadora")

"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.

"""