package Ciclos;

import javax.swing.JOptionPane;

public class Ciclos11 {
    public static void main(String[] args) {
        long producto = 1;
        for(int i = 1; i<=20; i+=2){    // El aumento apunta a solo ir por los impares
            producto *= i;
        }
        JOptionPane.showMessageDialog(null,"El producto de los numeros impares es: "+producto);
    }
}
