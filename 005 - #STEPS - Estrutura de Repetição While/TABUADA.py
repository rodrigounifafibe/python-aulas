indice = 0
continuar = 's'

while continuar.lower() == 's':
    tabuada = int(input('Informe um número para gerar a tabuada: '))
    indice = 0

    while(indice <= 10):
        print(f'{tabuada} x {indice} = {tabuada * indice}')
        indice = indice + 1

    continuar = input('Gerar outra tabuada? [S] - SIM ou [N] - NÃO ### RESPOSTA: ')

print('OBRIGADO POR UTILIZAR O SISTEMA DE TABUADA')



