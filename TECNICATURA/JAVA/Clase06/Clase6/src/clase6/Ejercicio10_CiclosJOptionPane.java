/*
Ejercicio 10: Ciclos - Clase Scanner y Clase JOptionPane
    Pedir 10 números y escribir la suma total.
*/

package clase6;
import javax.swing.JOptionPane;

public class Ejercicio10_CiclosJOptionPane {
    public static void main(String[] args) {
        int sumaTotal = 0;
        
        for (int i = 1; i < 11; i++) {
            String input = JOptionPane.showInputDialog("Ingrese el número " + i + ":");
            int numero = Integer.parseInt(input);
            
            sumaTotal += numero;
        }
        
        JOptionPane.showMessageDialog(null, "La suma total de los 10 números es: " + sumaTotal);
    }
}
