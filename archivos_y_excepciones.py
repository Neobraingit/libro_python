# Leer e imprimir archivo por pantalla
with open('fichero.txt') as documento:
  contenido  = documento.read()
  print (contenido)
  
  # Leer línea a línea
  filename = 'fichero.txt' 
  with open(filename) as documento2:
      for line in documento2:
          print (line)
          
filename = 'fichero.txt'
with open(filename, 'w') as documento3:
    documento3.write('Me gusta la programación')
    
with open('fichero.txt') as leer:
    contenido2 = leer.read()
    print (contenido2)
          
