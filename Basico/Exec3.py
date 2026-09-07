primeiro_valor= input("Insira o primeiro valor: ")
segundo_valor= input("Insira o segundo valor: ")

int_primeiro_valor= int(primeiro_valor)
int_segundo_valor= int(segundo_valor)

if primeiro_valor>segundo_valor:
    print(f"O primeiro valor: {int_primeiro_valor}, é maior que o segundo valor: {int_segundo_valor}")
if segundo_valor>primeiro_valor:
    print(f"O segundo valor: {int_segundo_valor}, é maior que o primeiro valor: {int_primeiro_valor}")
