# Manipulando Cadeias de Texto

frase = 'Aprendendo Python'

# Observação importante: ao lidar com intervalos, o python sempre ignora o último valor do intervalo definido.

# Exibindo qual caracter está na posição 11.
print(frase[11])

# Exibindo quais caracteres estão dentro do Intervalo 11 à 17.
# Quando trabalhamos com Ranges (intervalo), o último número não entra na contagem.
print(frase[11:17])

# Dentro do Intervalo 11 à 17, pega o caracter e pula de dois em dois.
print(frase[11:17:2])

# Quanto omitido o inicio, ele começa do caracter zero.
print(frase[:5])

# Indicando o inicio, mas não o final. Automaticamente para até o ultimo caracter.
print(frase[11:])

# Indicando o inicio, mas não o final. E pulando de três em três caracteres.
print(frase[9::3])

# Análise de cadeias de caracteres

# Len para ver o cumprimento de uma string.
print(len(frase))

# Count, vai contar quantas vezes aparece na string a letra "p" minuscula.
print(frase.count('p'))

# Count, considerando do 0 ao 12 (porque o 13 será excluido) irá buscar a letra p minuscula.
print(frase.count('p', 0, 13))


# Find vai encontrar em que momento aparece "end"
print(frase.find('end'))

# Find retorna o valor -1, quando o valor não é encontrado.
print(frase.find('Rodrigo'))


# In retorna verdadeiro ou falso caso exista na string.
print('Curso' in frase)

# Transformações

# Usando Replace
print(frase.replace('Python', 'Rodrigo'))

# Usando Upper e Lower para maiscula e minuscula
print(frase.upper())
print(frase.lower())

# Capitalize joga todos os caracteres para minusculo e somente o primeiro caracter em maiscula.
print(frase.capitalize())

# Title verifica quantas palavras a frase tem, e coloca o primeiro caracter de cada palavra em maiscula.
print(frase.title())

# Removendo espacos antes e depois com o Strip
fraseComEspacoExcedente = '   Aprendendo Python  '

print(fraseComEspacoExcedente.strip())
print('Com espaço: ', len(fraseComEspacoExcedente))
print('Sem espaço: ', len(fraseComEspacoExcedente.strip()))

# Remove os espaços somente da esquerda com lstring (left strip)
print('Sem espaço: ', len(fraseComEspacoExcedente.lstrip()))

# Remove os espaços somente da direita com rstring (right strip)
print('Sem espaço: ', len(fraseComEspacoExcedente.rstrip()))







