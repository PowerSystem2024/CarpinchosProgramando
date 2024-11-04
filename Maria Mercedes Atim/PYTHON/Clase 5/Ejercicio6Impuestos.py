# Calculadora de impuestos: Crear una funcionpara calcular el total de un pago incluyendo un impuesto aplicado. (IVA)
# Formula: pagoTotal = pagoSinImpuesto + pagoSinImpuesto * (impuesto/100)
# Proporcione el pago sin impuesto: 1000
# Proporcione el monto del impuesto: 21%
# Pago con impuesto: 1210

def calcularPagoConImpuesto(pagoSinImpuesto, impuesto):
    montoImpuesto = pagoSinImpuesto * (impuesto / 100) # Calculamos el monto del impuesto
    pagoTotal = pagoSinImpuesto + montoImpuesto # Calculamos el total con impuesto
    return pagoTotal

pagoSinImpuesto = float(input("Proporcione el pago sin impuesto: ")) # Solicitamos al usuario el monto inicial sin impuesto
impuesto = float(input("Proporcione el monto del impuesto (en porcentaje): ")) # Solicitamos al usuario el porcentaje del impuesto

pagoTotal = calcularPagoConImpuesto(pagoSinImpuesto, impuesto) # Calculamos el pago total

print(f"Pago con impuesto: {pagoTotal:.2f}") # Muestra el resultado con hasta 2 decimales.