frase = input('Digite uma frase: ').strip().upper().replace(' ', '')

# range (start = 8, stop = -1, step = -1)
# i = 0
# start = 12
# stop =  -1
# step =  -1
invertida = ''

for i in range(len(frase) -1, -1, -1):
    invertida += frase[i]

if frase == invertida:
    print(f'A frase {frase}  É UM PALÍNDROMO. Resultado => {invertida}')
else:
    print(f'A frase {frase}  NÃO É UM PALÍNDROMO. Resultado => {invertida}')


