from files.HOTEL_FUNCOES import relatorio, remover, cadastrar
from files.HOTEL_MENU import menu

quartos_reservados = {}
opcao = ''


while opcao != 's':
    opcao = menu()
    if opcao == 'n':
        cadastrar(quartos_reservados)
    elif opcao == 'r':
        relatorio(quartos_reservados)
    elif opcao == 'd':
        relatorio(quartos_reservados)
        remover(quartos_reservados)
    else:
        input('Opção indisponível. Clique em qualquer tecla para continuar...')
