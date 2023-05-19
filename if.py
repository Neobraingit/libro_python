# Pone todos los nombres de conches con la primera letra en mayúsculas menos bmw que irán todas en mayúsculas.

cars = ['audi', 'bmw', 'peugeot', 'seat']
for car in cars:
    if car == 'bmw':
        print (car.upper())
    else:
        print (car.title())
        
# True o False.

car = 'bmw'
print (car == 'bmw')

# Comprobación de desigualdad

car = 'bmw'
if car != 'bmw':
    print(False)
else:
    print (True)
    
# Comprobar valores numéricos

edad = 18
if edad == 18 :
    print (f'Mi edad es {edad}')
    
# And y or

edad = 22
if edad == 22 or edad == 22:
    print (f'Tienes {edad} años')
    
# Comprobar si un valor está en una lista

ls = 'cebollas', 'pimientos', 'puerro'
if 'cebollas' in ls:
    print ('Si, tengo cebollas...')
    
# Comprobar si un valor no está en una lista
numeros = []
for i in range(1, 101):
    numeros.append(i)
    if 2 not in numeros:
        print ('No está en la lista')
    elif 3 in numeros:
        print ('El 3 está en la lista')
        break
print (numeros)

    