# > DESAFIO
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2 metros quadrados.

largura = float(input('Informe a LARGURA da parede: '))
altura = float(input('Informe a ALTURA da parede: '))
area = largura * altura

print('Sua parede tem a dimensão de {}x{} e sua área é de {} metros quadrados.'.format(largura, altura, area))

tinta = area / 2

print('Para pintar essa parede, você vai precisar de {} litros de tinta.'.format(tinta))

