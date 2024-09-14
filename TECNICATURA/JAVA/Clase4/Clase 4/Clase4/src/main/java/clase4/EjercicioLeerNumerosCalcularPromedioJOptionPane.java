// Solicitar el ingreso de numeros hasta que se introduzca uno negativo y calcular la media.
// Realizamos el ejercicio con JOptionPane
package clase4;

import javax.swing.JOptionPane;

public class EjercicioLeerNumerosCalcularPromedioJOptionPane {

    public static void main(String[] args) {

        int numero, suma = 0, contador = 0;
       float promedio;

        do {
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero. Para finalizar, ingrese un numero negativo."));
            if (numero >= 0) {
                suma += numero;
                contador++;
            }
        } while (numero >= 0);
        promedio = (float) suma / contador;
        System.out.println("Se ingresó un número negativo. El programa finalizó. \nLa media aritmética de los números ingresados es: " + promedio);
    }
}