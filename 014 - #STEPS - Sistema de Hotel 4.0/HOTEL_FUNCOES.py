def relatorio(quartos):
    print('=-=-=-=-= RELATÓRIO DOS QUARTOS =-=-=-=-=')
    for quarto, hospede in quartos.items():
        print(f"QUARTO Nº {quarto} = {hospede['nome'].upper()}")
    input('Enter para continuar...')


def remover(quartos):
    quarto = int(input('Informe o número do quarto que deseja remover: '))
    if quarto in quartos:
        del quartos[quarto]
        input('Quarto liberado com sucesso!')
    else:
        input('Esse quartão está disponível. Não há ninguem nele.')


def cadastrar(quartos):
    try:
        quarto = int(input('Informe o número do quarto: '))
        if quarto in quartos:
            print('Este quarto está ocupado. Escolha outro!')
        else:
            # Perguntar o nome do hospede.
            nome = input('Informe o nome do hospede: ')
            idade = input('Informe a idade do hospede: ')
            cidade = input('Informe a cidade do hospede: ')
            hospede = {'nome': nome, 'idade': idade, 'cidade': cidade}
            quartos[quarto] = hospede

    except Exception as e:
        print('Operação inválida. Detalhes do erro: ', e)
        input('Enter para continuar...')

