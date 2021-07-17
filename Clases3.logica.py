#EJEMPLO Clases 3 logica
#Nombre: Heidy Vera
#Aula: Software A1

class Ejercicios:
    def __init__(self):
        pass
    
    def parImpar(self,numero):
        if numero % 2 == 0:
            print("{} es Par".Format(numero))
        else:
            print("{}es Impar".format(numero))
            
ejer = Ejercicios()
num = int(input("Ingrese un numero:  "))
lista = [2,3,1,5,6,8,10]
for num in lista:
    ejer.parImpar(num)
print("llamada 3")
ejer.parImpar(23)
    