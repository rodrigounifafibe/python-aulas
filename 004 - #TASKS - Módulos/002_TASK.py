# > TASK
# Desenvolva uma aplicação que pergunte o ano de nascimento da pessoa
# e utilizando o módulo datetime mostre quantos anos a pessoa têm.

from datetime import date
ano = int(input('Que ano você nasceu? '))
print(f'Neste ano você terá {date.today().year - ano} anos. Certo?')
