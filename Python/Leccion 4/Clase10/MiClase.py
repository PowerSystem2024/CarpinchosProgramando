class MiClase:

    variable_clase = "Esta es una variable de Clase"

    def __init__(self,variable_instancia):
        self.variable_instancia = variable_instancia


print(MiClase.variable_clase)
miClase1 = MiClase("Esta es una variable de instancia")
print(miClase1.variable_instancia)
miClase2 = MiClase("Esta es una PRUEBA variable de instancia")
print(miClase2.variable_instancia)