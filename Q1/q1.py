'''
1) Observe o trecho de código abaixo:
int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?
'''


def valorDaSoma(indice = 13, soma = 0, k =0):
    for i in range(indice):
        k+=1
        soma+=k
    return soma


def main():
    #Código "simples e direto"
    indice = 13
    soma =0
    k = 0

    #Função
    while k < indice:
        k +=1
        soma += k


    print(soma) #Resultado obtido = 91



    #Uso de função, permitindo valores padrão e alteração de valores
    print(valorDaSoma())

    return

if __name__ == "__main__":
    main()
