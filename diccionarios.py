alien = {'color ': 'green', 'points' : 5 }

# Acceder a los valores del diccionario
print (alien['color '])
print (alien['points'])

# Añadir nuevos clave:valor
alien['tipo'] = 'nave'
print (alien)

# Cambiar el valor de un diccionario
alien['tipo'] = 'interstelar'
print (alien)

# Obtener un valor con get
print (alien.get('color '))

# Bucle for en un diciionario
for k, v in alien.items(): # Ojo al método items que hay que utilizar también
    print (k)
    print (v)
    
# Pasar el bucle por las claves solamente
for k in alien.keys():
    print (k)

# Pasar el bucle por las claves y ordenarlas
for k in sorted(alien.keys()):
    print (k)
    
# Pasar el bucle por los valores del diccionario
for v in alien.values():
    print (v)

# Listas dentro de diccionarios
pizza = {'Margarita' : ['peperoni', 'mozarella', 'atun']}
for i in pizza.values():
    print (i)
    
# Un diciionario en un diccionario
coches = {'marcas' : {'seat', 'bmw', 'renault'}}
for c in sorted(coches.values()):
    print (c)
