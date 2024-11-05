from Computadora import Computadora  # Importa la clase Computadora
from Teclado import Teclado  # Importa la clase Teclado
from Raton import Raton  # Importa la clase Raton
from Monitor import Monitor  # Importa la clase Monitor
from Orden import Orden  # Importa la clase Orden

# Definición de la primera computadora con sus componentes
teclado1 = Teclado("Logitech", "USB")  # Crea un teclado USB Logitech
raton1 = Raton("HP", "USB")  # Crea un ratón USB de la marca HP
monitor1 = Monitor("Samsung", "24 pulgadas")  # Crea un monitor Samsung de 24 pulgadas
computadora1 = Computadora("HP", monitor1, teclado1, raton1)  # Crea una computadora HP con los componentes anteriores

# Definición de la segunda computadora con sus componentes
teclado2 = Teclado("RedDragon", "inalambrico")  # Crea un teclado inalámbrico RedDragon
raton2 = Raton("Corsair", "USB")  # Crea un ratón USB de la marca Corsair
monitor2 = Monitor("ViewSonic", "25 pulgadas")  # Crea un monitor ViewSonic de 25 pulgadas
computadora2 = Computadora("ThermalTake", monitor2, teclado2, raton2)  # Crea una computadora ThermalTake

# Lista de computadoras para la primera orden
computadoras1 = [computadora1, computadora2]  # Lista con las primeras dos computadoras
orden1 = Orden(computadoras1)  # Crea la primera orden con las computadoras anteriores
print(orden1)

# Definición de la tercera computadora con sus componentes
teclado3 = Teclado("Corsair", "USB")  # Crea un teclado USB Corsair
raton3 = Raton("Genius", "USB")  # Crea un ratón USB Genius
monitor3 = Monitor("LG", "27 pulgadas")  # Crea un monitor LG de 27 pulgadas
computadora3 = Computadora("Dell", monitor3, teclado3, raton3)  # Crea una computadora Dell

# Definición de la cuarta computadora con sus componentes
teclado4 = Teclado("Razer", "inalambrico")  # Crea un teclado inalámbrico Razer
raton4 = Raton("SteelSeries", "USB")  # Crea un ratón USB SteelSeries
monitor4 = Monitor("BenQ", "24.5 pulgadas")  # Crea un monitor BenQ de 24.5 pulgadas
computadora4 = Computadora("CyberPowerPC", monitor4, teclado4, raton4)  # Crea una computadora CyberPowerPC

# Lista de computadoras para la segunda orden
computadoras2 = [computadora3, computadora4]  # Lista con las computadoras tres y cuatro
orden2 = Orden(computadoras2)  # Crea la segunda orden con las computadoras anteriores

# Imprime las órdenes
print(orden2)  # Muestra la segunda orden con las computadoras tres y cuatro

# Agrega la computadora4 a la orden1
orden1.agregarComputadoras(computadora4)  # Agrega la computadora cuatro a la orden uno
print("Orden 1 Modificada: ")
print(orden1)  # Muestra la primera orden con tres computadoras

# Agrega la computadora1 a la orden2
orden2.agregarComputadoras(computadora1)  # Agrega la computadora uno a la orden dos
print("Orden 2 Modificada: ")
print(orden2)  # Muestra la segunda orden con tres computadoras
