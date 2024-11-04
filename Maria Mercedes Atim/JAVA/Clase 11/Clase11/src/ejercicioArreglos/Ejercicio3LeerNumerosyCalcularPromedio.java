/*Ejercicio 3:
Leer 5 numeros pro teclado, almacenarlos en un arreglo y a continuacion realizar la media
de los numeros positivos, la media de los negativos y contar el numero de 0 ingresados.
 */
package ejercicioArreglos; 

import java.util.Scanner; 

public class Ejercicio3LeerNumerosyCalcularPromedio { 
    
    public static void main(String[] args) { 
        
        int numeros[] = new int[5]; // Creamos un arreglo para almacenar 5 números
        Scanner entrada = new Scanner(System.in); // Creamos un objeto Scanner para leer la entrada del usuario
        
        System.out.println("Por favor ingrese 5 numeros: "); // Pedimos al usuario que ingrese 5 números
        
        // Bucle para leer 5 números y almacenarlos en el arreglo
        for (int i = 0; i < numeros.length; i++) { // Itera 5 veces
            System.out.print("Número " + (i + 1) + ": "); // Pide el número correspondiente
            numeros[i] = entrada.nextInt(); // Lee el número y lo guarda en el arreglo
        }

        // Inicializamos variables para cálculos
        int sumaPositivos = 0; // Suma de números positivos
        int sumaNegativos = 0; // Suma de números negativos
        int contadorPositivos = 0; // Contador de números positivos
        int contadorNegativos = 0; // Contador de números negativos
        int contadorCeros = 0; // Contador de ceros

        // Bucle para calcular medias y contar ceros
        for (int num : numeros) { // Itera sobre cada número en el arreglo
            if (num > 0) { // Si el número es positivo
                sumaPositivos += num; // Suma el número a la suma de positivos
                contadorPositivos++; // Incrementa el contador de positivos
            } else if (num < 0) { // Si el número es negativo
                sumaNegativos += num; // Suma el número a la suma de negativos
                contadorNegativos++; // Incrementa el contador de negativos
            } else { // Si el número es 0
                contadorCeros++; // Incrementa el contador de ceros
            }
        }
        // Calculamos y mostramos la media de números positivos
        if (contadorPositivos > 0) { // Solo si hay números positivos
            double mediaPositivos = (double) sumaPositivos / contadorPositivos; // Calcula la media
            System.out.println("La media de los números positivos es: " + mediaPositivos); // Muestra la media
        } else {
            System.out.println("No se ingresaron números positivos."); // Mensaje si no hay positivos
        }
        // Calculamso y mostramos la media de números negativos
        if (contadorNegativos > 0) { // Solo si hay números negativos
            double mediaNegativos = (double) sumaNegativos / contadorNegativos; // Calcula la media
            System.out.println("La media de los números negativos es: " + mediaNegativos); // Muestra la media
        } else {
            System.out.println("No se ingresaron números negativos."); // Mensaje si no hay negativos
        }

        // Mostramos el conteo de ceros
        System.out.println("Se ingresaron " + contadorCeros + " ceros."); // Muestra la cantidad de ceros
    }
}