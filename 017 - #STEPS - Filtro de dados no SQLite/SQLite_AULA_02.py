import sqlite3

# Conecta-se com o arquivo de dados.
banco = sqlite3.connect('banco.db')

# Cursor para executar os comandos.
sql = banco.cursor()

# Recuperando todas as colunas da tabela ( * ).
# sql.execute('SELECT * nome FROM alunos')

# Recuperando colunas especificas da tabela (curso e nome).
# sql.execute('SELECT curso, nome FROM alunos')

# Filtrando pela cidade. Filtro de igualdade com o WHERE.
# sql.execute("SELECT nome, curso, cidade FROM alunos WHERE idade = 'Bebedouro'")

# Filtra pela idade dos alunos. Maior ( > ), Menor ( < ), Maior Igual ( >= ) e Menor Igual ( <= )
# sql.execute('SELECT * FROM alunos WHERE idade <= 23')

# Filtrando por valores que sejam diferentes.
# sql.execute("SELECT * FROM alunos WHERE cidade <> 'Bebedouro'")

# Ordernando o resultado da consulta.
# sql.execute("SELECT * FROM alunos WHERE cidade = 'Bebedouro' ORDER BY nome")


# Ordenando por valores decrescente.
# sql.execute("SELECT * FROM alunos ORDER BY idade DESC")

# Ranking na consulta.
sql.execute("SELECT * FROM alunos ORDER BY nota DESC LIMIT 3")

for row in sql.fetchall():
    print('NOME: ', row[0])
    print('IDADE: ', row[1])
    print('CURSO: ', row[2])
    print('CIDADE: ', row[3])
    print('NOTA: ', row[4])

    print('-----------------------------')




