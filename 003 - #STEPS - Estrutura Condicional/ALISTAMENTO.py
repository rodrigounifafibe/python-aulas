from datetime import date
anoAtual = date.today().year

anoNascimento = int(input('Informe o ano que você nasceu:'))
idade = anoAtual - anoNascimento

if idade == 18:
    print('Você tem que se alistar esse ANO!')
elif idade < 18:
    falta = 18 - idade
    print(f'Você deve se alistar em {falta} anos')
else:
    falta = idade - 18
    print(f'Você deveria ter se alistado há {falta} anos.'
          f'Você já foi dispensado?')