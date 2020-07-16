
import sqlite3

banco = sqlite3.connect('financeiro.db')
sql = banco.cursor()
sair = 'n'


def verificar_se_existe(id_despesa):
    sql.execute(f'SELECT id FROM despesas WHERE id = {id_despesa}')
    return sql.fetchone()


def listar_por_status(filtro):
    sql.execute(f"SELECT * FROM despesas WHERE status = '{filtro}'")

    for row in sql.fetchall():
        print('ID:', row[0])
        print('Descrição:', row[1])
        print('Valor:', row[2])
        print('Status:', row[3])
        print('----------------------')

    input('Enter para continuar...')


while sair == 'n':
    print(''' ##### SISTEMA DE FINANÇAS PESSOAL
    [1] - Cadastrar nova despesa (INSERT)
    [2] - Remover despesa (DELETE e SELECT *)
    [3] - Dar baixa na despesa (UPDATE)
    [4] - Ver despesas pagas (SELECT COM WHERE)
    [5] - Ver despesas pendentes (SELECT COM WHERE)
    [6]  - Sair  
    ''')
    opcao = int(input('OPÇÃO: '))

    if opcao == 1:
        print("### INFORME OS DADOS DA DESPESA ###")
        descricao = input("Descrição: ")
        valor = float(input("Valor: "))

        sql.execute(f"INSERT INTO despesas (descricao, valor, status) VALUES ('{descricao}', {valor}, 'pendente')")
        banco.commit()
        input('DESPESA REGISTRADA! Enter para continuar...')
    elif opcao == 2:
        print("### SELECIONE A DESPESA PARA REMOVER ###")
        sql.execute('SELECT * FROM despesas')

        for row in sql.fetchall():
            print('ID:', row[0])
            print('Descrição:', row[1])
            print('Valor:', row[2])
            print('Status:', row[3])
            print('----------------------')

        ID = int(input('ID para remover: '))
        sql.execute(f'DELETE FROM despesas WHERE id = {ID}')
        banco.commit()
        input('DESPESA REMOVIDA! Enter para continuar...')
    elif opcao == 3:
        print("### SELECIONE A DESPESA PARA DAR BAIXA ###")
        sql.execute("SELECT * FROM despesas WHERE status = 'pendente'")

        for row in sql.fetchall():
            print('ID:', row[0])
            print('Descrição:', row[1])
            print('Valor:', row[2])
            print('----------------------')
        ID = int(input('ID para dar baixar: '))

        retorno = verificar_se_existe(ID)

        if not retorno:
            input('ESSE ID NÃO EXISTE! Enter para continuar...')
        else:
            sql.execute(f"UPDATE despesas SET status = 'pago' WHERE id = {ID}")
            banco.commit()
            input('DESPESA BAIXADA! Enter para continuar...')
    elif opcao == 4:
        print("### TODAS AS DESPESAS PAGAS ###")
        listar_por_status('pago')
    elif opcao == 5:
        print("### TODAS AS DESPESAS PENDENTES ###")
        listar_por_status('pendente')
    elif opcao == 6:
        sair = 's'
    else:
        input('OPÇÃO INVÁLIDA! Enter para continuar...')
