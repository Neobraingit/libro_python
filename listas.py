# Introducción a las listas
# Creamos una lista
ls = ['name', 'last_name', 'age']

# Acceder a los elementos de la lista
print (ls[0].title())

# Usar las cadenas con formato en las listas
print (f'El primer elemento de la lista es ', ls[0].title())

# Modificar elementos de una lista
ls[0] = 'nombre'
print (ls)

# Añadir elementos a una lista
ls.append('Apodo') # Esto nos añade el nuevo elemento al final de la lista
print (ls)

# Insertar elementos a una lista
ls.insert(2, 'Cuca') # Esto nos añade un elemento en le índice que le digamos
print (ls)

# Eliminar elementos de una lista
del ls[0] # Esto nos borra el elemento que está en el índice indicado
print (ls)

# Sacar un elemento de una lista pero poder seguir usándolo
ls.pop(1)
print (ls)

# Eliminar un elemento de una lista desconociendo el índice; lo haremos por valor
ls.remove('age') # Eliminamos un elemento por su valor
print (ls)

# Ordenar una lista
ls.sort() # Nos ordena la lista alfabéticamente
print (ls)

# Imprimir la lista en orden inverso
ls.reverse()
print (ls)

# Longitud de una lista
print (len(ls))

# Bucle for con listas
magicians = ['Gandalf', 'Saruman', 'Harry Potter']
for magician in magicians:
    print (magician)
    
# Más bucle for con listas
magicians = ['Gandalf', 'Saruman', 'Harry Potter']
for magician in magicians:
    print (f'El mago {magician} hace buenos trucos')
print ('Esto se repite una sola vez por que no está sangrada dentro del bucle for')
    
# Range para crear una lista de números
ls = list(range(1, 11))
print (ls)

# Segunda potencia 
squares = []
for i in range(1, 11):
    square = i ** 2
    squares.append(square)
    
# min, max, sum; máximo, mínimo y suma de los números de una lista
numeros = [1, 2, 3, 4, 5, 6]
print (max(numeros))
print (min(numeros))
print (sum(numeros))

# Usar el bucle for con un subconjunto de la lista
for i in numeros[:3]:
    print (i)
    
# Copiar una lista
coches = ['clío', 'toyota', 'rav4', 'zafira']
cochesdeeva = coches[:]
print (cochesdeeva)
    
    

    
    