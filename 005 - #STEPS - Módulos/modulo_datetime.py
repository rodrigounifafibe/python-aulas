
# Utilizando o módulo datetime para obter informações de data e hora. 

from datetime import date, datetime
print(f'Hoje é dia {date.today()}')
print(f'Hoje é dia {date.today().strftime("%d/%m/%Y")}')
print(f'Hoje é dia {date.today().day}, do mês {date.today().month} e o ano é {date.today().year}')
print(f'Agora é: {datetime.now().strftime("%H:%M:%S")}')