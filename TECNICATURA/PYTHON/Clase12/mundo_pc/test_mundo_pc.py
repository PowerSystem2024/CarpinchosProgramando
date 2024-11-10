from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado

teclado1 = Teclado('LG', 'USB')
monitor1 = Monitor('LG', '15 pulgadas')
raton1 = Raton('Genius', 'USB')
computadora1 = Computadora('HP', monitor1, teclado1, raton1)


teclado2 = Teclado('Genius', 'USB')
monitor2 = Monitor('LG', '17 pulgadas')
raton2 = Raton('Genius', 'Bluetooth')
computadora2 = Computadora('DELL', monitor2, teclado2, raton2)

##

teclado3 = Teclado('Lenovo', 'USB')
monitor3 = Monitor('Lenovo', '17 pulgadas')
raton3 = Raton('Genius', 'USB')
computadora3 = Computadora('Lenovo', monitor3, teclado3, raton3)


teclado4 = Teclado('Genius', 'USB')
monitor4 = Monitor('Philips', '15 pulgadas')
raton4 = Raton('Genius', 'Bluetooth')
computadora4 = Computadora('DELL', monitor4, teclado4, raton4)

computadora6 = Computadora('Samsung', monitor4, teclado2, raton2)
computadora7 = Computadora('Gamer', monitor3, teclado1, raton2)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
orden1.agregar_computadoras(computadora6)
print(orden1)

computadoras2 = [computadora3, computadora4, computadora6, computadora7]
orden2 = Orden(computadoras2)
orden2.agregar_computadoras(computadoras2)
print(orden2)


