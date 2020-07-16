filmes = []
opcao = 's'


def relatorio():
    print('--- FILMES ---')
    posicao = 0
    for filme in filmes:
        print(f'Opção Nº{posicao} - {filme}')
        posicao += 1


while opcao != 'p':

    print('''
    [C] - Cadastrar um novo filme
    [M] - Mostrar os filmes cadastrados
    [R] - Remover um filme
    [P] - Parar o programa
    ''')
    opcao = input('>>> Opção: ').lower()

    if opcao == 'c':
        filmes.append(input('Digite o nome do filme: '))
    elif opcao == 'm':
        relatorio()
    elif opcao == 'r':
        relatorio()
        filmes.pop(int(input('Digite a posição do filme para remover: ')))