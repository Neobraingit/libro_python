# Declarar una clase simple
class Perro:
    def __init__(self, nombre, edad) :
        self.nombre = nombre
        self.edad = edad
        
mi_perro = Perro ('tobi', 12)
print (mi_perro.nombre)
print (mi_perro.edad)

mi_perro.edad = 48

print (mi_perro.edad)


