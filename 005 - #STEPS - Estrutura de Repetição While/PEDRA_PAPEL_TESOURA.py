from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

opcaoValida = 0
while opcaoValida == 0:
    print('''Escolha a sua jogada:
            [0] - PEDRA
            [1] - PAPEL
            [2] - TESOURA        
          ''')
    jogador = int(input('Sua jogada:'))

    if jogador >= 0 and jogador <= 2:
        opcaoValida = 1
    else:
        print('Opção inválida!')

print('#' * 20)
print('O computador escolheu: ', itens[computador])
print('O jogador escolheu: ', itens[jogador])

# computador escolheu PEDRA
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCEU!')
    else:
        print('COMPUTADOR VENCEU!')
# computador escolheu PAPEL
elif computador == 1:
    if jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCEU!')
    else:
        print('COMPUTADOR VENCEU!')
# computador escolheu TESOURA
elif computador == 2:
    if jogador == 2:
        print('EMPATE!')
    elif jogador == 0:
        print('JOGADOR VENCEU!')
    else:
        print('COMPUTADOR VENCEU!')