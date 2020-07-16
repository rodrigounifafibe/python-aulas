# Qtde de posições no vetor/lista -  inicia no 1
# Qtde de iterações/voltar - inicia no 0

techs = ['Python', 'Java Script', 'C#', 'Visual Basic', 'PHP', 'Ruby']

# Parametros do Range do FOR
# start = início do loop (primeira elemento sequência/volta)
# stop =  fim do loop (último  elemento da sequência/volta)
# step = intervalo entre os elementos

for i in range(0, len(techs), 2):
    print(f'Na posição {i} está a linguagem {techs[i]}')
