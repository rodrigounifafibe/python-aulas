# TUPLAS são listas imutáveis. Ou seja, o conteúdo da lista não muda.

filmes = (
    input('Informe o primeiro filme: '),
    input('Informe o segundo  filme: '),
    input('Informe o terceiro filme: ')
)

indice = 0
while indice < 3:
    print(f'Na posição {indice} está o filme {filmes[indice]}')
    indice = indice + 1




