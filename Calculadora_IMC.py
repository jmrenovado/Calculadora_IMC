# Calculadora de IMC
# IMC = peso / (altura x altura)
# < 19: Delgado
# entre 20 y 25: normal
# entre 26 y 30: sobre peso
# > de 30: obesidad

peso = float(input('Ingrese su peso en kg'))
alturaCm = float(input('Ingrese su altura en cm'))
alturaMt = alturaCm / 100
imc = peso / (alturaMt * alturaMt)

print('Su IMC es de ' + str(imc))

if imc < 20:
    print('Delgado')
if imc >= 20 and imc < 25:
    print('Peso normal')
if imc >= 26 and imc < 30:
    print('Peso normal') 
if imc >= 30:
    print('Peso normal') 

