x = int(input("Ingrsese un numero entero:"))
if x <0:
    x =0
    print('Negativo cambiado a cero')
elif x == 0:
    print('cero')
elif x == 1:
    print('uno')
else:
    print('Ninguna opcion')
print("Ok")if type(x)== int else print("_")