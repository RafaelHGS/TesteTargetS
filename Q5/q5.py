'''
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
'''

#Uso de laço for
def inversorPalavras1(palavra = str):
    novaPalavra = ""
    for i in range(len(palavra), 0, -1):
        novaPalavra += palavra[i-1]

    return novaPalavra


#Maneira "Preguiçosa" de inverter uma string na linguagem python
def inversorPalavras2(palavra = str):
    return palavra[::-1]


#Uso de list comprehension
def inversorPalavras3(palavra = str):
    return ''.join([palavra[x-1] for x in range(len(palavra),0, -1)])


def main():
    palavra = str(input("Digite uma palavra a ser invertida: "))
    
    print(inversorPalavras1(palavra))
    print(inversorPalavras2(palavra))
    print(inversorPalavras3(palavra))

    return


if __name__ == "__main__":
    main()
