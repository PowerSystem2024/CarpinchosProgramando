/*Ejercicio 1: 
Leer 5 numeros, guardarlos en un arreglo y mostrarlos en el mismo orden introducidos.*/
package ejercicioArreglos;

import java.util.Scanner; // Importamos la clase Scanner para leer la entrada del usuario

public class Ejercicio1LeerNumeros { 

    public static void main(String[] args) { 
        
        Scanner entrada = new Scanner(System.in); // Creamos un objeto Scanner para leer la entrada del usuario
        
        System.out.println("Por favor ingrese 5 números."); // Pedimos al usuario que ingrese 5 números
        int numeros[] = new int[5]; // Crea un arreglo para almacenar 5 números
        
        // -------- Bucle para leer 5 números y almacenarlos en el arreglo
        for (int i = 0; i < 5; i++) { // Itera 5 veces
            System.out.print("Número " + (i + 1) + ": "); // Pide el número correspondiente
            numeros[i] = entrada.nextInt(); // Lee el número y lo guarda en el arreglo
        }
        
        System.out.println("Los números ingresados son:"); // Mensaje para indicar que se mostrarán los números
        
        // -------- Bucle para mostrar los números en el mismo orden en que fueron ingresados
        for (int i = 0; i < 5; i++) { // Itera sobre el arreglo
            System.out.println(numeros[i]); // Imprime cada número
        }
    }
}