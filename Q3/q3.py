'''
Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
'''

#Biblioteca para leitura de Arquivo Json
import json


#Função que define valor inicial a fim de evitar começar o valor com 0 (dias sem faturamento)
def valorInicial(dados):
    valor = dados[0]["valor"]
    
    contador= 1
    while valor <= 0:
        valor = dados[contador]["valor"]
        contador += 1
    return valor


def menorFaturamento(dados):
    #Obtem valor inicial
    valor = valorInicial(dados)

    #verificando menor faturamento do mês
    menor = {}
    for i in dados:
        if i["valor"] < valor and i["valor"] != 0:
            valor = i["valor"]
            menor = i 

    return menor["valor"]


def maiorFaturamento(dados):
    #Obtem valor inicial
    valor = valorInicial(dados)
    #verificando menor faturamento do mês
    maior = {}
    for i in dados:
        if i["valor"] > valor and i["valor"] != 0:
            valor = i["valor"]
            maior = i

    return maior["valor"]

#438172

def fMaiorMedia(dados):

    #Encontrando a média do mês ignorando valores com faturamento 0 (sem faturamento)
    mediaMensal = [x["valor"] for x in dados if x["valor"] != 0]
    mediaMensal = sum(mediaMensal)/len(mediaMensal)

    faturamentoMaiorMedia = []
    
    for i in dados:
        if i["valor"] > mediaMensal:
            faturamentoMaiorMedia.append(i)

    numeroDeDiasMaiorMedia = len(faturamentoMaiorMedia)

    return mediaMensal, numeroDeDiasMaiorMedia, faturamentoMaiorMedia


def main():
    
    #Abrindo e lendo arquivo Json

    with open("Q3\dados.json", "r") as file:
        dados = json.load(file)
    file.close()

    print("Menor Faturamento do mês: ", menorFaturamento(dados))
    print("Maior Faturamento do mês: ", maiorFaturamento(dados))
    print()
    
    mediaMesal, numeroDias, diasEspecificos = fMaiorMedia(dados)

    print(f"Média mensal: {mediaMesal}")
    print(f"Número de dias que o faturamento superou a média mensal: {numeroDias}")
    print()
    print("Dias detalhados em que o faturamento superou a média mensal:")
    print(*diasEspecificos, sep="\n")


if __name__ == "__main__":
    main()
