# Ejercicio 4: Funciones - Calculadora de Impuestos
# Crear una función para calcular el total de un pago, 
# incluyendo un impuesto aplicado (IVA)
# Fórmula:
#   pagoTotal = pagoSinImpuesto + pagoSinImpuesto * (impuesto/100)
# Proporcione el pago sin impuesto: 1000
# Proporcione el monto del impuesto 21%
# Pago con impuesto: xxxxx

pagoSinImpuesto = float(input('Proporcione el pago sin impuesto: '))
impuesto = float(input('Proporcione el monto del impuesto: '))

pagoTotal = pagoSinImpuesto + pagoSinImpuesto * (impuesto/100)

print(f'El pago total, incluyendo el impuesto es de: {pagoTotal}')
