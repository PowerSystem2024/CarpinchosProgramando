# Ejercicio: Tienda de Libros
# 1. Mostrar: 'Ingrese los siguientes datos del libro:'
# 2. Ingrese el nombre del libro.
# 3. Ingrese el ID del libro.
# 4. Ingrese el precio del libro.
# 5. Indicar si el envío es gratuito (True/False).
# 6. Mostrar:
#   Nombre:
#   ID: 
#   Precio: 
#   ¿Envío Gratuito?

print('Ingrese los siguientes datos:')
nombreLibro = input('Nombre del Libro: ')
idLibro = int(input('ID del Libro: '))
precioLibro = float(input('Precio del Libro: $'))
envio = input('Indique si el envío es gratuito (True) o no (False): ')

if envio == 'True':
    envio == True
elif envio == 'False':
    envio == False
else:
    print('Ingresó un valor incorrecto, por favor ingrese True o False.')

print(f'''
    Nombre del Libro: {nombreLibro}
    ID del Libro: {idLibro}
    Precio del Libro: ${precioLibro}
    ¿Envio Gratuito?: {envio}
''')
