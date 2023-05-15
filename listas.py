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
