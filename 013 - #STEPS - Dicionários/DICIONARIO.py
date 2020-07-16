'''
    2 categorias de lista => imutável x mutável
    () => imutável => Tupla
    [] => mutável => lista simples
    {} => mutável => Dicionário

    Dicionário ele composto:
    chave:key
    Exemplo => email:rodrigo@email.com
'''

frutas = {
    'laranja': 430,
    'banana': 123,
    'uva': 75
}

print('Quantas frutas tem disponível: ', len(frutas))
print('Quantas bananas tem: ', frutas['banana'])
frutas['banana'] = 175
print('Agora, tem essa quantidade de bananas: ', frutas['banana'])

# Adicionando dinamicamente um atributo (key : value)
key = input('Digite o nome da nova fruta: ')
value = int(input(f'Digite a quantidade disponível da {key}: '))

# colocando uma nova chave (fruta) com um novo valor (quantidade).
frutas[key] = value

# mostra o dicionário por completo
print(frutas.items())

# mostra somente as keys do dicionário
print(frutas.keys())

# mostra somente os valores do dicionário
print(frutas.values())

print('PERCORRENDO TODAS AS CHAVES DO DICIONÁRIO')
for i in frutas:
    print(i)

print('Super FOR para percorrer dicionário')
for key, value in frutas.items():
    print(f'A fruta {key.upper()} TEM {value} unidades.')

if 'abacate' in frutas:
    print('TEM ABACATE')
else:
    print('NÃO TEM ABACATE')


