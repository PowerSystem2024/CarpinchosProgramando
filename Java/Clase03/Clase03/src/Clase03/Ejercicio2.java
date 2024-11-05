package Clase03;

import javax.swing.JOptionPane;

public class Ejercicio2{

    public static void main(String[] args) {

        int numero;

        do {
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número para verificar si es PAR o IMPAR"));
            if (numero % 2 == 0) {
                System.out.println("El número " + numero + " es PAR.");
            } else {
                System.out.println("El número " + numero + " es IMPAR.");
            }
        } while (numero != 0);
        System.out.println("Se ingresó un Cero. El programa finalizó.");
    }
}
