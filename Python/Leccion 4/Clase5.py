# hacer un programa que pida una cadena por teclado, luego meter los caracteres en una lista, sin repetirlos
def sinRepetirCaracteres(cadena):
    sinRepetidos = []
    for i in cadena:
        sinRepetidos.append(i)
        sinRepetidosSet = set(sinRepetidos)
    print(sinRepetidosSet)
sinRepetirCaracteres("hola hola hola")



# hacer un programa que simule una agenda de contactos, crear un diccionario
# donde la clase sea el nombre del usuario y el valor sea el teelefono, el programa debe tener el sgte menu:
# nuevo contacto
# borrar contacto
# ver contactos existentes
# salir
def agendaTelefonica():
    agenda = {
        "wanda": 2604352412,
        "ramon": 2604310989,
        "miriam": 260431234
    }
    while True:
        opcion = int(input("""A continuación, seleccione una opción: \n
                    1 - Crear un nuevo contacto
                    2 - Eliminar un contacto
                    3 - Ver contactos existentes
                    4 - Salir \n
                    """))
        if opcion == 1:
            nombre = input("Ingrese el nombre para el nuevo contacto: ")
            numero = int(input(f"Ingrese el número para el contacto {nombre}: "))
            agenda[nombre] = numero
            print(f"Contacto {nombre} agregado correctamente.\n")
        elif opcion == 2:
            nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
            if nombre in agenda:
                del agenda[nombre]
                print(f"Contacto {nombre} eliminado correctamente.\n")
            else:
                print(f"El contacto {nombre} no existe en la agenda.\n")
        elif opcion == 3:
            print("Contactos existentes:")
            for nombre, numero in agenda.items():
                print(f"{nombre}: {numero}")
            print()
        elif opcion == 4:
            print("Saliendo de la agenda.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.\n")
agendaTelefonica()


def show(name, lastname):
    print(name, lastname)
person = ["mercedes", "atim"]
show(person[0], person[1])
show(*person)
person2 = ('Wanda', "Lanatta")
show(*person2)
person3 = {"name": "Fernando", "lastname": "Simich"}
show(**person3)

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
    if n == 3:
        break
    else:
        print("esto se termino")


names = ["Lucia","Mica", "Mariana"]
alongP = [p for p in names if p[0] == "p"]
print(alongP)
bottleC = [
    {"name": "quilmes", "country": "arg"},
    {"name": "corona", "country": "mx"},
    {"name": "stella artois", "country": "belgium"}
]
arg = [b for b in bottleC if b["country"] == "arg"]
print(arg)
print(bottleC)

def miFuncion(name, lastName):
    print(f"nombre {name} apellido {lastName}")
miFuncion("Maria", "Mercedes")
miFuncion("Fernando", "Simcih")
miFuncion("Flor", "Gaston")

def sumar(a, b):
    return  a + b
print(sumar(1, 2))

def listaNombres(*nombres):
    for nombre in nombres:
        print(nombre)
listaNombres("Flor", "Luis", "Elizabeth", "Jazmin")
# crear una funcion para sumar los valores recibidos de tipo int, utilizando como argumento *args, sumar todos los valores
def sumAllValues(*nums):
    sum = 0
    for i in nums:
        sum += i
    return sum
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10]
res = sumAllValues(*n)
print(res)
# funcion con *args para multiplicar
def multiplicarTodo(*nums):
    multi = 1
    for i in nums:
        multi *= i
    return multi
n = [1, 2, 3]
res = multiplicarTodo(*n)
print(res)




def listaTerminos(**termino):
    for llave, valor in termino.items():
        print(f"{llave} : {valor}")
listaTerminos(IDE = "integrated developmet envirometn", pk = "primary key")


def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres = ["tito", "pepe"]
desplegarNombres(nombres)
desplegarNombres("carla")
desplegarNombres((11, 10))
desplegarNombres([22, 55])

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
res = factorial(5)
print(f"el factorial de 5 es {res}")

# imprimir una lista de numeros de forma descendente de forma recursiva
def recursivaDescendiente(n):
    if n == 1:
        print(1)
    else:
        print(n)
        recursivaDescendiente(n - 1)
recursivaDescendiente(5)

# crear una funcion para calcular el total del pago incluyendo un iimpuesto aplica (iva)
def calculadora():
    precioBruto = int(input("ingrese el precio bruto de su compra: "))
    precioIva = precioBruto + (precioBruto * 0.21)
    print(f"el total de su compra es de {precioIva}")
calculadora()

# crear dos funciones para pasar de celsius a fahrenheit
def CtoF(temp):
    print(f"la temperatura en fahrenhei es {(temp * (9/5)) + 32}")
def FtoC(temp):
    print(f"la temperatura en celcius es {(temp - 32) * (9/5)}")
CtoF(10)
FtoC(19)


