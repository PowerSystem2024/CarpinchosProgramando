package clase5;

import javax.swing.JOptionPane;

public class MostrarNumeroHastaNJOptionPane {

    public static void main(String[] args) {

        int numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
        for (int i = 1; i <= numero; i++) {
            System.out.println(i);
        }
    }
}
