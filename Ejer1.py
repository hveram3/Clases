#Uso de while
c = 1
While True:
 print(c)
 
 
 
#While validacion
Vocal = input("Inrese Vocal")
while Vocal not in ('a','e','i','o','u'):
    if Vocal =='.':
        break
    Vocal = input ("vocal:")
print('Su vocal o punto es :{}'.format(vocal))
