/* 
Ejercicio 2: Leer un numero e indicar si es positivo o negativo.
El proceso se repetira hasta que se introduzca un cero 0.
*/
package Ciclos02;

import javax.swing.JOptionPane;

public class Ejercicio02JOP {
    public static void main(String[] args) {
   
    var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
    while(numero != 0){
            if(numero > 0){
                System.out.println("El numero "+numero+" es postivo.");
            }
            else{
                System.out.println("El numero "+numero+" es negativo.");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
            
        }
    System.out.println("El numero "+numero+" finaliza el programa.");
    }   
}
