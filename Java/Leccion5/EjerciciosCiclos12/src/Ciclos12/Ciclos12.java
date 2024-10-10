package Ciclos12;

import javax.swing.JOptionPane;

public class Ciclos12 {

    public static void main(String[] args) {
        long factorial = 1;
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        for (int i = 1; i <= numero; i++) {
            factorial *= i;
        }
        JOptionPane.showMessageDialog(null, "El factorial del numero ingresado es: " + factorial);
    }
}
