# Métodos en las cadenas
name = 'ada lovelace'
print (name.title())
print (name.lower())
print (name.upper())

# Cadenas format
name = 'Marcos'
last_name = 'Carmona'
full_name = f'Mi nombre es {name} {last_name}'
print (full_name)
print (f'Hello, my name is {full_name.title()}')

# Tabulaciones y saltos de línea
print (f'\t{name}')
print (f'\nCarmona')

# Eliminar espacios en blanco
favorite_languaje = 'Python '
print (favorite_languaje)
print (favorite_languaje.rstrip()) # Elimina espacios a la derecha
print (favorite_languaje.lstrip()) # Elimina espacios a la izquierda
print (favorite_languaje.strip()) # Elimina espacios a los dos lados a la vez


