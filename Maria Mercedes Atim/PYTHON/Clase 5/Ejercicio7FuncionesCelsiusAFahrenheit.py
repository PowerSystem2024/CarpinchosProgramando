# Conversor de temperaturas: Realizar dos funciones para convertir grados Celsius a Fahrenheit y viceversa.
# Celsius a Fahrenheit: (0 °C × 9/5) + 32 = 32 °F
# Fahrenheit a Celsius: °C = (°F - 32) × 5/9

def celsiusAFahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32 # Convierte grados celsius a Fahrenheit
    return fahrenheit

def fahrenheitACelsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9 # Convierte Fahrenheit a celsius
    return celsius

temperaturaCelsius = 100
temperaturaFahrenheit = celsiusAFahrenheit(temperaturaCelsius)
print(f"{temperaturaCelsius} °C es igual a {temperaturaFahrenheit} °F")

temperaturaFahrenheit = 500
temperaturaCelsius = fahrenheitACelsius(temperaturaFahrenheit)
print(f"{temperaturaFahrenheit} °F es igual a {temperaturaCelsius} °C")