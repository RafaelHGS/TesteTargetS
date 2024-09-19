'''
Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  

'''

def percentualFaturamento(estados):

    faturamentoTotal = sum(estados.values())

    faturamentoDoEstado = []

    for estado, faturamento in estados.items():
        percentual= round((faturamento/faturamentoTotal*100), 2)
        auxEstado = {f"{estado}" : percentual}
        faturamentoDoEstado.append(auxEstado)

    return faturamentoDoEstado



def main():

    #Lista de faturamento por estado
    estados = {"SP": 67836.43,
            "RJ": 36678.66,
            "MG": 29229.88,
            "ES": 27165.48,
            "Outros": 19849.53}

    print("Percentual de faturamento de cada estado: ")
    print(*percentualFaturamento(estados),sep='\n')

    return

if __name__ == "__main__":
    main()
