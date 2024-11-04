class Aritmetica:
    """
    El nombre de este tipo de comentario es DocString
    Esto es documentacion de la clase en Python
    Vamos a hacer en esta clase algunas operaciondes de:
    suma, resta, multiplicacion y mas.
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB
    
    def restar(self):
        return self.operandoA - self.operandoB
    
    def multiplicar(self):
        return self.operandoA * self.operandoB
    
    def dividir(self):
        return self.operandoA / self.operandoB
    
# Creamos instancia de la clase aritmetica:
aritmetica1 = Aritmetica(7,9)
print("Resultado de la suma de los argumentos con metodo SUMAR: ", aritmetica1.sumar())

print("\nResultado de la resta de los argumentos con metodo RESTAR: ", aritmetica1.restar())

print("\nResultado de la multiplicacion de los argumentos con metodo MULTIPLICAR: ", aritmetica1.multiplicar())

resultado = aritmetica1.dividir()
print(f"\nResultado de la division de los argumentos con metodo DIVIDIR: {resultado:.2f}")
