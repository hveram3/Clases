#EJEMPLO Clases 1 ordenar
#Nombre: Heidy Vera
#Aula: Software A1

class Oredenar:
    def __init__(self,lista):
       self.lista=lista
       
    def recorrerElemento(self):
        for ele in self.lista:
            print(ele)
            
    def recorrerEnumerate(self):
        for pos,ele in enumerate(self.lista):
            print(pos,ele)
            
    def recorrerRange(self):
        for pos,ele in range(self.lista):
            print(pos,self.lista[pos])
            
    def buscar(self,buscado):
        enc=False
        for pos,ele in enumerate(self.lista):
            if ele == buscado:
                enc=True
                break
        if enc == True: return pos
        else:return -1 
    
             
                
lista = [2,3,1,5,8,10] = [1,2,3,5,8,10]
ord1 = Oredenar(lista)
# ord1.recorrerElemento()
# ord1.recorrerEnumerate()
#ord1.recorrerRange()
print(ord1.buscar(3))
buscado=9
resp = ord1.buscar(buscado)
if resp !=1:
    print("Numero={} se encuentra en la Posicion:({})" .format(buscado,resp))
else:
    print("El Numero={} no se encuentra en la lista". format (buscado))