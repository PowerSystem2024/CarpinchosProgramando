package Ciclos03;

import javax.swing.*;
import java.util.Scanner;

public class Ejercicio03 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero;

        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));


        while (numero != 0) {
            if (numero % 2 == 0) {

                JOptionPane.showInputDialog(null,"El numero ingresado"+ numero + "es par");


            }
            else {
                JOptionPane.showInputDialog(null,"El numero ingresado"+ numero + "es impar");
            }

            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero"));

        }
        JOptionPane.showInputDialog(null,"El número ingresado es " +numero+ " finaliza el programa");
    }
}