nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))

media = (nota1 + nota2 + nota3) / 3
print(f'A sua média é {media:.1f}')
if media >= 7:
    print('APROVADO!')
elif media < 7 and media >= 5:
    print('RECUPERAÇÃO!')
else:
    print('REPROVADO!')