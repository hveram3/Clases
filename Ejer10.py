class ciclo:
    
    def __intit__(self,numero=5):
        self.numero=numero
        self.numero2=0
        
    def usowhile(self):
        car = input("ingrese vocal")
        car = car.lower()
        while car not in('a','e','i','o','u'):
            car = input("ingrese vocal").lower()
        print("Felicitacion su vocal es:{}".format(car))



ciclo1 = ciclo()
ciclo1.usowhile()
print("fin de uso ciclo")