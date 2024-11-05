// Pedir Numeros hasta que se teclee un 0. Mostrar la suma de todos los numeros introducidos.
// Lo hacemos con JOptionPane
package Clase04;

import javax.swing.JOptionPane;

public class EjercicioCiclos1 {

    public static void main(String[] args) {
        int numero, suma = 0;

        do {
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
            suma += numero;
        } while (numero != 0);
        System.out.println("Se ha ingresado 0, finalizó el programa. \nLa suma de los numeros ingresados es: " + suma);
    }
}