# Hacer un programa donde el usuario ingrese una frase, se le devolvera la misma frase pero sin espacios en blanco y ademas un contador de caracteres de la frase sin contar espacios.
# Por ejemplo: "Vivir por siempre en paz"
# Frase final: "vivirporsiempreenpaz"  Contador de caracteres: 20

frase = input("\nIngrese una frase: ")
frase2 = ""
for letra in frase:
    if letra != " ":
        frase2 += letra
frase = frase2
print(f"\nFrase final: {frase}\n")
print(f"Cantidad de caractedes de la frase: {len(frase)}")