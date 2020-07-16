preco = float(input('Informe o valor da compra R$ '))

print('''FORMAS DE PAGAMENTO
        [1] - à vista dinheiro/cheque
        [2] - à vista no cartão
        [3] - 2x no cartão
        [4] - 3x ou mais no cartão
''')

opcao = int(input('Opção:' ))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de '
          f'R${parcela:.2f} SEM JUROS!')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    qtdeParcelas = int(input('Quantas parcelas?'))
    valorParcela = total / qtdeParcelas
    print(f'Sua compra será parcelada em {qtdeParcelas}x'
          f' de R${valorParcela:.2f} e o total é {total}')
else:
    total = preco
    print('Opção de pagamento inválida! Tente novamente!')

print(f'Sua compra de R${preco:.2f} '
      f'vai custa no final R${total:.2f}')








