package ejercicios.clase2.ciclos;

import javax.swing.JOptionPane;

public class Ejercicio2JOptionpaneClase2 {
    
    public static void main(String[] args) {
        int numero;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero para calcular su cuadrado. "));
        while (numero > 0){
        JOptionPane.showMessageDialog(null, "El cuadrado del número ingresado es: " + numero*numero);
        numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro numero para calcular su cuadrado. "));
        }
        System.out.println("El programa se detuvo, se ingresaron numeros negativos o cero. ");
    }
}