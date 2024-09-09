# Dadas las horas trabajadas de 5 personas y la tarifa de pago, 
# calcular el salario y la sumatoria de todos los salarios.

def calcularSalario(horasTrabajadas, tarifa):
    salario = horasTrabajadas * tarifa
    return salario

horasTrabajadas = []
tarifas = []
totalSalarios = 0

for i in range(5):
    horas = float(input(f"Ingrese las horas trabajadas de la persona {i+1}: "))
    tarifa = float(input(f"Ingrese la tarifa de pago por hora de la persona {i+1}: "))
    horasTrabajadas.append(horas)
    tarifas.append(tarifa)

print("\nSalarios individuales: ")
for i in range(5):
    salarioPersona = calcularSalario(horasTrabajadas[i], tarifas[i])
    print(f"Persona {i+1}: ${salarioPersona:.2f}")
    totalSalarios += salarioPersona

print("\nSuma total de salarios: ", totalSalarios)
