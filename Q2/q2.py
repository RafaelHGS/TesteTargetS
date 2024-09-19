'''
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
'''

#Função para cálculo da sequência de fibonnacci
def Fibonnacci(numero):
    seqFibonnacci = [0, 1]      #Inicio da Sequencia

    for i in range(numero+1):   #Construção da sequência em uma lista
        proximo = seqFibonnacci[i] + seqFibonnacci[i+1]
        seqFibonnacci.append(proximo)
        if proximo >= 1:
            continue

    if numero in seqFibonnacci:
        return f"O número {numero} PERTENCE a sequência de Fibonnacci"
    else:
        return f"O número {numero} NÃO PERTENCE a sequência de Fibonnacci"
    

#Teste de código
def main():
    print(Fibonnacci(2))
    print(Fibonnacci(5))
    print(Fibonnacci(7))
    print(Fibonnacci(34))
    print(Fibonnacci(35)) 


if __name__ == "__main__":
    main()