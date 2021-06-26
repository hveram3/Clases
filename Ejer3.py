#Funciones sin retorno
def vocales(frase):
    for car in frase:
        if car in ('a','e','i','o','u'):
            print(car)

"llamada a funcion"
oracion = input ('ingrese oracion:')
vocales(oracion.lower())

"funcion con retorno de valor"
def promedio(notas):
    summ = 0
    for n in notas:
    summ + = n
return summ/ len(notas)

#llamada a funcion
listasnotas = [2,4,6,8,10]
prom = promedio(listanotas)
print('promedio:{}={}'.format(listanotas,prom))
