// Leer numeros hasta que se introduzca un cero. Para cada uno, indicar si es PAR o IMPAR.
// Haremos con la clase JOptionPane.
package clase_3;

import javax.swing.JOptionPane;

public class Ejercicio2ParImparJOptionPane {

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
