# tupla de 10 posições
times = ('Santo André', 'Palmeiras', 'São Paulo', 'Red Bull Bragantino',
         'Mirassol', 'Guarani', 'Novorizontino', 'Santos', 'Inter de Limeira', 'Corinthians')

print('Os 5 primeiros são: ', times[0:5])
print('OS 4 últimos colocados:', times[-4:])
print('Times em Ordem alfabética: ', sorted(times))

solicacao = input('Informe o time que você quer saber a posição: ')
print(f'O time {solicacao} está na {times.index(solicacao) + 1}º posição do campeonato!')


