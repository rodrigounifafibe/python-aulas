quartos_reservados = {}
opcao = ''

'''
    {key   : value}
    {quarto: hospede}
'''

while opcao != 's':
    # Obtém a opção escolhida pelo usuário.
    print('''
    =-=-=-= OPÇÕES DO SISTEMA =-=-=-=
        [N] = nova reserva
        [D] = Remover reserva
        [R] = Exibir Relatório 
        [S] = Sair do Programa 
    ''')
    opcao = input('Opção: ').lower()

    if opcao == 'n':
        # Perguntar o quarto para o usuário.
        quarto = int(input('Informe o número do quarto: '))
        if quarto in quartos_reservados:
            print('Este quarto está ocupado. Escolha outro!')
        else:
            # Perguntar o nome do hospede.
            hospede = input('Informe o nome do hospede: ')
            quartos_reservados[quarto] = hospede
    else:
        print('Opção indisponível por enquanto.')


print('=-=-=-=-= RELATÓRIO DOS QUARTOS =-=-=-=-=')
for quarto, hospede in quartos_reservados.items():
    print(f'QUARTO Nº {quarto} = {hospede.upper()}')

