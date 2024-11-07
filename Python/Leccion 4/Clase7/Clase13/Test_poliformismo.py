from Empleado import Empleado 
from Gerente import Gerente

def imprimir_detalles(objeto):
   # print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
     print(objeto.departamento)

empleado = Empleado ("Simich", 888)
imprimir_detalles(empleado)

gerente = Gerente("Melani", 900000,"Sistemas")
imprimir_detalles(gerente)