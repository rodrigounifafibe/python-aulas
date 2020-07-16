import sqlite3

# Criando o banco de dados.
banco = sqlite3.connect('banco.db')

# É através do cursor que podemos executar comandos dentro do SQLite.
cursor = banco.cursor()

# Criando a tabela dentro do banco de dados.
cursor.execute("CREATE TABLE pessoas (nome TEXT, idade INTEGER, cidade TEXT)")

# Confirma a execução dos comandos dentro do arquivo de dados.
# O commit é utilizado somente quando o arquivo de dados é alterado.
banco.commit()

# Vamos inserir uma pessoa na tabela.
cursor.execute("INSERT INTO pessoas VALUES('Ana', 32, 'Viradouro')")
banco.commit()

# Vamos ler o conteúdo do arquivo de dados.
cursor.execute('SELECT * FROM pessoas')
print('CONTEÚDO DA TABELA PESSOAS:')
print(cursor.fetchall())




