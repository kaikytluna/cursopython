"""
Faça um programa que pergunte a hora ao usuário e baseando-se no hórario descrito, exiba a saudação apropriada 
Ex: Bom dia 0-11, Boa Tarde 12-17 e Boa noite 18-23
"""
horario=input("Insira o horário atual(Apenas numerais): ")

if horario.isdigit():
    int_horario=int(horario)
    if 12<=int_horario<=17:
        print("Boa tarde!")
    elif 18<=int_horario<=23:
        print("Boa noite!")
    elif 0<=int_horario<=4:
        print("Boa madrugada!")
    else:
        print("Bom dia!")
else:
    print("Você não digitou um numeral")






