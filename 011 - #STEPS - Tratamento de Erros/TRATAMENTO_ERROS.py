try:
    numero = int(input('Número: '))
    print('Triplo é: ', numero * 3)
except:
    print('Valor inválido. Somente número é aceito!')
finally:
    print('Fim do programa. Fechou?')


