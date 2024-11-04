package clase_6;

import javax.swing.JOptionPane;

public class Ejercicio2Clase6Pedir10NumerosYMostrarSumaJOPane {

    public static void main(String[] args) {

        int numero, suma = 0; // Inicializamos las variables

        for (int iterador = 0; iterador < 10; iterador++) { // Se va a repetir 10 veces
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
            System.out.println(numero);
            suma += numero; // Actualizamos la suma
        }
        System.out.println("La suma de los números ingresados es: " + suma);
    }
}