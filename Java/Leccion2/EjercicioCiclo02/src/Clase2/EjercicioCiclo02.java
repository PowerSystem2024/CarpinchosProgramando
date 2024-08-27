package Clase2;

import javax.swing.JOptionPane;

public class EjercicioCiclo02 {

    public static void main(String[] args) {
        int numero;

        numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero para verificar si es negativo o positivo. "));
        while (numero != 0){
            if(numero > 0){
                JOptionPane.showMessageDialog(null, "El número ingresado ("+numero+") es positivo.");
            }
            else{
                JOptionPane.showMessageDialog(null, "El número ingresado ("+numero+") es negativo");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro numero para verificar si es positivo o negativo. "
                    + "El programa finaliza cuando ingrese cero. "));
        }
        System.out.println("El programa se detuvo, se ingresaron numeros negativos o cero. ");
    }
}