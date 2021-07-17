#EJEMPLO Clases 4 logica
#Nombre: Heidy Vera
#Aula: Software A1
#fecha:16/07/21

class programacion (Ejercicios):
    def __init__(self):
        pass
    
    def divisores(self,num):
        cont=1
        divisores=[]
        for cont in range (1,num):
            rec = num % cont
            if rec == 0:
                divisores.append(cont)
        
        while cont < num:
            rec = num % cont
            if rec == 0:
                divisores.append(cont)
            cont = cont +1
        print(divisores)
            
        
class Programacion(Ejercicios):
    def __init__(self):
        pass
    
    def divisores(self,num):
        divisores=[]
        for cont in range (1,num):
            rec = num % cont
            if rec == 0:
                divisores.append(cont)      
                 
prog1 = programacion()
div = prog1.divisores(6) 
lista = [1,2]
lista2= lista+divmod   
print (lista2)
            

                    
   




  