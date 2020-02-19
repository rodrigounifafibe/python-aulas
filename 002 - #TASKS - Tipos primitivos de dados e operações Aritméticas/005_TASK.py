""" 
  > TASK 5:
  Escreve um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""

medida = float(input('Informe uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {:.2f}cm e {:.2f}mm'.format(medida, cm, mm))
