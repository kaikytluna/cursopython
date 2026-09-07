# # def imprimir(a,b,c):
# #     print('abc')

# # imprimir()

# def saudacao(nome="sem nome"):
#     print(f"Olá, {nome}!")

# saudacao('kaiky')
# saudacao()
cpf='27764656615'
cpf_formatado=''

i=0
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
