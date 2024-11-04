// Diseñar un programa que muestre el producto de los 10 primeros numeros impares. Hacerlo con JOptionPane.
package clase7;

import javax.swing.JOptionPane;

public class Ejercicio1CiclosMostrarProductoPrimeros10Numeros {

    public static void main(String[] args) {

        int multiplicacion = 1, contador = 0; // Inicializamos las variables

        for (int i = 1; contador < 10; i += 2) { // Inicializamos el iterador en 1 y sumamos 2 en cada iteracion para que tome solamente los impares
            multiplicacion *= i; // Multiplicamos solamente el número impar alojado en i
            contador++; // Aumentamos el contador para que llegue a 10
        }
        JOptionPane.showMessageDialog(null, "El producto de los 10 primeros números impares es: " + multiplicacion);
    }
}