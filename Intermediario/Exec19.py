def generator(n):
    yield 0
    print("Continuando...")
    print(1)
    print(2)
    # yield 3
    print(4)
    return "ACABOU"

try:
    ...    
    gen=generator(1)
    print(next(gen))
    print(next(gen))

finally:
    print("cu")

# try:
#     print(next(gen))
#     print(next(gen))

# except StopIteration:
#     print('fim do generator')