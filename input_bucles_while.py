# Input
print ('Dime tu nombre: ')
nombre = input()

# Int para las entradas numéricas
print ('Dime tu edad: ')
edad = int(input())

# Bucle while
numero = 1 
while numero != 5 :
    numero += 1
    print (numero)
    
# Qué eliga el usuario cuando salir del programa
print ('Dime la palabra mágica: ')
palabra = input()
while palabra != 'quit':
    print ('Dime la palabra mágica: ')
    palabra = input()
else:
    print ('Has salido del programa¡¡')
    
# Bandera
active = False
while active:
    print ('Hola me llamo Marcos')
    break
    