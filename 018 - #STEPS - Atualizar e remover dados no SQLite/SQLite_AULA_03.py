import sqlite3

banco = sqlite3.connect('banco.db')
sql = banco.cursor()

# id = input('ID do aluno: ')
# novaNota = int(input('Nova nota: '))

# ID -> IDentity (identificador, númerico ou hash e único)
# PK -> Primary Key (Chave-Primária = garantir que o id seja único)
# AI -> Auto Increment (Distribuí o ID)

# Atualiza registros.
# sql.execute(f"UPDATE alunos SET nota = {novaNota} WHERE id = {id}")
# banco.commit()
# print('NOTA ATUALIZADA!')

# Remover registros.
# alunoId = int(input('ID do aluno para remover: '))
# sql.execute(f"DELETE FROM alunos WHERE id = {alunoId}")
# banco.commit()
# print('ALUNO REMOVIDO!')

nome = input('Nome: ')
idade = int(input('Idade: '))
cidade = input('Cidade: ')
curso = input('Curso: ')
nota = int(input('Nota: '))
sql.execute(f"INSERT INTO alunos "
            f"(nome, idade, cidade, curso, nota)"
            f"VALUES('{nome}', {idade}, '{cidade}', '{curso}', {nota})")
banco.commit()
print('ALUNO CADASTRADO!')
