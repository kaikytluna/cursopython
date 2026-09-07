import math
import random

cpf=''.join(str(random.randint(1,9)) for _ in range(11))

# with open("CPFS10.txt", "r", encoding="utf-8") as arquivo:
#     lista_cpfs = arquivo.read().splitlines()

# cpf = (lista_cpfs)
# cpf="060.678.010-60"
# print(cpf)
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
        break
    else:
        cpf_valido=False
        continue

cpf_formatado = ''

def format_cpf(a):
    cpf_formatado=''
    i=0

    for digito in a:
        if i % 3 ==0 and i!=0 and i!= 9:
            cpf_formatado+="."

        if i==9:
            cpf_formatado+="-"

        cpf_formatado+=digito
        i+=1

    return cpf_formatado

cpf_formatado = format_cpf(cpf)

print(cpf_formatado)

