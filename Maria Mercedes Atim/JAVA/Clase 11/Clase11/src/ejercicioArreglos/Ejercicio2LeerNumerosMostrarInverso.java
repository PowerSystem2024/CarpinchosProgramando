/*Ejercicio 2:
Leer 5 numeros, guardarlos en un arreglo y mostrarlos en el orden inverso al introducido*/
package ejercicioArreglos; 

import java.util.Scanner; 

public class Ejercicio2LeerNumerosMostrarInverso { 

    public static void main(String[] args) { 
        
        Scanner entrada = new Scanner(System.in); // Creamos un objeto Scanner para leer la entrada del usuario
        
        System.out.println("Por favor ingrese 5 numeros: "); // Pedimos al usuario que ingrese 5 números
        int numeros[] = new int[5]; // Creamos un arreglo para almacenar 5 números
        
        // Bucle para leer 5 números y almacenarlos en el arreglo
        for (int i = 0; i < numeros.length; i++) { // Itera 5 veces
            System.out.print("Número " + (i + 1) + ": "); // Pide el número correspondiente
            numeros[i] = entrada.nextInt(); // Lee el número y lo guarda en el arreglo
        }
        
        System.out.println("Mostramos los números en orden inverso: "); // Mensaje para indicar que se mostrarán los números
        
        // Bucle para mostrar los números en orden inverso
        for (int i = numeros.length - 1; i >= 0; i--) { // Itera desde el último índice hasta el primero
            System.out.println(numeros[i]); // Imprime cada número en orden inverso
        }
    }
}