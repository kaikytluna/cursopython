while True:
    num_1=input("Insira o primeiro número: ")
    num_2=input("Insira o segundo número: ")
    operador=input("Insira o operador(+-/*): ")
    numeros_validos=None
    operador_valido="+-/*"

# region verificação dos dados

    try:
        num_1_float=float(num_1)
        num_2_float=float(num_2)
        numeros_validos=True

    except:
        numeros_validos=None

    if not numeros_validos:
        print("Um ou ambos os números são invalidos:")
        continue

    if operador not in operador_valido:
        print("Erro no operador!")
    
    if len(operador)>1:
        print("Insira apenas um operador!")

# endregion

    if operador=="+":
        resultado=num_1_float+num_2_float
    if operador=="-":
        resultado=num_1_float-num_2_float
    if operador=="/":
        resultado=num_1_float/num_2_float
    if operador=="*":
        resultado=num_1_float*num_2_float
    if resultado.is_integer():
        result_int=int(resultado)
        print(result_int)
    else:
        print(resultado)

# region saida
    while True:    
        sair=input("Deseja fazer outro cálculo? [s]im ou [n]ão: ").lower()
        if sair=="não" or sair=="nao" or sair=="n":
            if sair:
                break
        elif sair=="sim" or sair=="s":
            break
        else:
            print("Resposta invalida! Digite apenas [s]im ou [n]ão")
    if sair=="não" or sair=="nao" or sair=="n":
        break
# endregion

print("Você saiu da calculadora")