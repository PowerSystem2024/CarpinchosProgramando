// Pedir un numero y calcular su factorial. Hacerlo con JOprionPane
package clase7;

import javax.swing.JOptionPane;

public class Ejercicio3CiclosFactorialDeUnNumeroIngresadoJOptionPane {

    public static void main(String[] args) {
        int numero;
        long factorial = 1; // Iniciamos factorial en 1 y como long ya que es un numero que va creciendo rapidamente.
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número para calcular su factorial: "));
        
        for (int i = 1; i <= numero; i++) { //Iniciamos el iterador en 1. iterará hasta el numero que ingresó el usuario y avanzará de 1 en 1
            factorial *= i; // Multiplicamos el resultado de la multiplicacion de los numeros y lo guardamos en factorial.
        }
        
        JOptionPane.showMessageDialog(null, "El factorial de:  " + numero + "! es: " + factorial);
    }
}