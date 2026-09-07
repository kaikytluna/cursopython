x=2

def escopo():
    def outra_funcao():
        y=1
        print(y)
    outra_funcao()
    print(x)

escopo()