quartos_reservados = {}
opcao = ''

'''
    {key   : value}
    {quarto: hospede}
'''

def Relatorio():
    print('=-=-=-=-= RELATÓRIO DOS QUARTOS =-=-=-=-=')
    for quarto, hospede in quartos_reservados.items():
        print(f'QUARTO Nº {quarto} = {hospede.upper()}')
    input('Continuar...')

def ReservarQuarto():
    # Perguntar o quarto para o usuário.
    quarto = int(input('Informe o número do quarto: '))
    if quarto in quartos_reservados:
        print('Este quarto está ocupado. Escolha outro!')
    else:
        # Perguntar o nome do hospede.
        hospede = input('Informe o nome do hospede: ')
        quartos_reservados[quarto] = hospede

def Remover(quarto):
    del quartos_reservados[quarto]
    input('Quarto liberado com sucesso!')

while opcao != 's':
    # Obtém a opção escolhida pelo usuário.
    print('''
    =-=-=-= OPÇÕES DO SISTEMA =-=-=-=
        [N] = Nova reserva
        [D] = Remover reserva
        [R] = Relatório 
        [S] = Sair do Programa 
    ''')
    opcao = input('Opção: ').lower()

    if opcao == 'n':
       ReservarQuarto()
    elif opcao == 'd':
        Remover(int(input('Informe o número do quarto: ')))
    elif opcao == 'r':
        Relatorio()
    else:
        print('Opção inválida.')







