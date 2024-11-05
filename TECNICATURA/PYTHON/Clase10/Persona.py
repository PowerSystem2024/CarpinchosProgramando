class Persona:
    contador_personas = 0  # Contador de personas creadas
    
    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre, edad):
        Persona.contador_personas += 1  # Incrementa el contador
        self.id_persona = Persona.contador_personas  # Asigna ID único
        self.nombre = nombre  # Asigna nombre
        self.edad = edad  # Asigna edad

    def __str__(self):
        return f"Persona : id: {self.id_persona}, nombre: {self.nombre}, edad: {self.edad}"  # Representación en cadena

# Crear instancias de Persona
persona1 = Persona("Wanda", 21)  # Crea una persona
print(persona1)  # Imprime la información de persona1 llama a __str__

persona2 = Persona("Nicolas", 24)  # Crea otra persona
print(persona2)  # Imprime la información de persona2

persona3 = Persona("Melina", 20)  # Crea una persona mas
print(persona3)  # Imprime la información de persona3

Persona.generar_siguiente_valor() # Aumenta a 1 el contador

persona4 = Persona("Mariana", 26)  # Crea una persona mas
print(persona4)  # Imprime la información de persona4

print(f"Valor contador personas: {Persona.contador_personas}")  # Imprime el total de personas creadas