class Aritmetica:

    # DEFINIENDO LOS ATRIBUTOS
    def __init__(self, operandoA,operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    # DEFINIENDO LOS METODOS
    def sumar(self):
        return self.operandoA + self.operandoB
    def resta(self):
        return self.operandoA - self.operandoB
    def multiplicacion(self):
        return self.operandoA * self.operandoB
    def division(self):
        if self.operandoB == 0:
            return 0
        else:
            return self.operandoA / self.operandoB
    
ariemetica1 = Aritmetica(2,0)

print(f"La suma es: {ariemetica1.sumar()}")
print(ariemetica1.resta())
print(ariemetica1.multiplicacion())
print(ariemetica1.division())