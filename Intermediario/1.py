cpf = '27764656615'
cpf_formatado = ''

def format_cpf(a):
    cpf_formatado = ''
    i = 0

    for digito in a:
        if i % 3 == 0 and i != 0:
            cpf_formatado += ' '

        cpf_formatado += digito
        i += 1

    return cpf_formatado

cpf_formatado = format_cpf(cpf)
print(cpf_formatado)