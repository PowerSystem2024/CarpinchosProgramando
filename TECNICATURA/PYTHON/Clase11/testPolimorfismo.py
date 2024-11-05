from Empleado import Empleado
from Gerente import Gerente

def imprimirDetalles(objeto):
    # Llamado indirecto al str de la clase Empleado o Gerente
    # print(objeto)
    # Tipo de dato que recibe
    print(type(objeto))
    print(objeto.mostrarDetalles())
    # No se puede acceder al objeto 'departamento' a menos que
    # se utilice el método isinstance()
    # isinstance(objeto, clase) -> comprueba si un objeto está 
    #                          instanciado dentro de una clase, 
    #                          entonces va a ejecutar el código 
    #                          sin errores
    # Si es falso, no accederá al objeto
    if(isinstance(objeto, Gerente)):
        print(objeto.departamento)

empleado = Empleado('Ana', 50000.00)
imprimirDetalles(empleado)

gerente = Gerente('Lucas', 60000.00, 'Robótica')
imprimirDetalles(gerente)
