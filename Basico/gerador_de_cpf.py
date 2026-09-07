import math
import random
"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf=''.join(str(random.randint(1,9)) for _ in range(11))
# cpf="060.678.010-60"
# print(cpf)
cpf_valido=None
cpf_gerado=0
while True and cpf_gerado<=10:
    cpf_valido=None
    while not cpf_valido:
        cpf=''.join(str(random.randint(1,9)) for _ in range(11))
        digitos_cpf=[]
        digitos_cpf_x10=[]
        cont_reg_1=10
        cont_reg_2=11
        indice=0
        if len(cpf)>11:
            for digito in cpf:
                if indice<11 and digito.isdigit():
                    digitos_cpf.append(digito)
                    indice+=1
                else:
                    indice+=1
                    continue
        else:

            for digito in cpf:
                if indice<9:
                    digitos_cpf.append(digito)
                    indice+=1

        for digito in digitos_cpf:
            digitos_cpf_x10.append(int(digito)*cont_reg_1)
            cont_reg_1-=1

        soma_1=sum(digitos_cpf_x10)
        resto_1=soma_1*10 % 11
        resultado_penultimo_dgt= 0 if resto_1>9 else resto_1
        digitos_cpf.append(resultado_penultimo_dgt)
        digitos_cpf_x10=[]

        for digito in digitos_cpf:
            digitos_cpf_x10.append(int(digito)*cont_reg_2)
            cont_reg_2-=1

    

        soma_2 = sum(digitos_cpf_x10)
        resto_2 = soma_2*10 % 11
        resultado_ultimo_dgt = 0 if resto_2>9 else resto_2
        digitos_cpf.append(resultado_ultimo_dgt)
        tam_cpf=len(cpf)
        if int(cpf[-2])==resultado_penultimo_dgt and int(cpf[-1])==resultado_ultimo_dgt:
            cpf_valido=True
            print(cpf)
            break
        else:
            cpf_valido=False
            continue
    cpf_gerado+=1
    continue


















"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

# numeros_cpf=[]
# multiplos_cpf=[]
# contagem_regressiva_1=10
# contagem_regressiva_2=11

# # region penultimo digito
# indice_dig1=0
# for numero in cpf:
#     if indice_dig1<=9 and numero.isdigit():
#         numeros_cpf.append(numero)
#         indice_dig1+=1
#     else:
#         indice_dig1+=1
#         continue


# for numero in numeros_cpf:
#     multiplos_cpf.append(int(numero)*contagem_regressiva_1)
#     contagem_regressiva_1-=1

# soma= sum(int(numero) for numero in multiplos_cpf)
# resto=soma*10 % 11

# if resto<=9:
#     resultado=resto
# elif resto>9:
#     resultado=0

# penultimo_digito=resultado
# numeros_cpf.append(penultimo_digito)

# # endregion

# # region ultimo digito
# multiplos_cpf=[]
# for numero in numeros_cpf:
#     multiplos_cpf.append(int(numero)*contagem_regressiva_2)
#     contagem_regressiva_2-=1

# soma= sum(int(numero) for numero in multiplos_cpf)
# resto_segundo_digito=soma*10 % 11
# print(multiplos_cpf)

# # if resto<=9:
# #     resultado=resto
# # elif resto>9:
# #     resultado=0

# ultimo_digito=resultado
# # print(multiplos_cpf)