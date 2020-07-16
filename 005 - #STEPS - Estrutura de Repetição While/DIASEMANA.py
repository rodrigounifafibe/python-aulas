diasSemana = ("Inválido", "domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sábado")
dia = int(input('INFORME UM NÚMERO DE 1 - 7: '))

if dia <= 0 or dia > 7:
    print(diasSemana[0])
else:
    print(diasSemana[dia])