# calculadora.py
def calcular_consumo_energia(numeros_binarios):
    contadores = [[0, 0] for _ in range(len(numeros_binarios[0]))]

    for numero in numeros_binarios:
        for i, bit in enumerate(numero):
            if bit == '0':
                contadores[i][0] += 1
            else:
                contadores[i][1] += 1

    taxa_gama = ''
    taxa_epsilom = ''
    
    for contagem in contadores:
        if contagem[1] > contagem[0]:
            taxa_gama += '1'
            taxa_epsilom += '0'
        else:
            taxa_gama += '0'
            taxa_epsilom += '1'

    taxa_gama_decimal = int(taxa_gama, 2)
    taxa_epsilom_decimal = int(taxa_epsilom, 2)

    return taxa_gama_decimal * taxa_epsilom_decimal
