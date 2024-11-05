package Clase03;

import javax.swing.JOptionPane;

public class Ejercicio4 {

    public static void main(String[] args) {
        int numero, contador = 0;

        do {
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número. Para finalizar ingrese un número negativo."));
            if (numero >= 0) {
                contador++;
            }
        } while (numero >= 0);

        System.out.println("Ha ingresado un número negativo.");
        System.out.println("Se han ingresado " + contador + " números.");
    }
}