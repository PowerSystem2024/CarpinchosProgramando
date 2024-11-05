package EjercicioArreglos;
/*Ejercicio 1:
Leer 5 numeros, guardarlos en un arreglo y mostrarlos en el mismo orden introducidos.*/


import java.util.Scanner; // Importamos la clase Scanner para leer la entrada del usuario

public class Ejercicio1 {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in); // Creamos un objeto Scanner para leer la entrada del usuario

        System.out.println("Por favor ingrese 5 numeros."); // Pedimos al usuario que ingrese 5 n�meros
        int numeros[] = new int[5]; // Crea un arreglo para almacenar 5 n�meros

        // -------- Bucle para leer 5 n�meros y almacenarlos en el arreglo
        for (int i = 0; i < 5; i++) { // Itera 5 veces
            System.out.print("Numero " + (i + 1) + ": "); // Pide el n�mero correspondiente
            numeros[i] = entrada.nextInt(); // Lee el n�mero y lo guarda en el arreglo
        }

        System.out.println("Los numeros ingresados son:"); // Mensaje para indicar que se mostrar�n los n�meros

        // -------- Bucle para mostrar los n�meros en el mismo orden en que fueron ingresados
        for (int i = 0; i < 5; i++) { // Itera sobre el arreglo
            System.out.println(numeros[i]); // Imprime cada n�mero
        }
    }
}