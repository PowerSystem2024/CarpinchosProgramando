package Clase03;

import javax.swing.JOptionPane;

public class Ejercicio6 {

    public static void main(String[] args) {

        int numero, numeroAAdivinar, contador = 0;
        numeroAAdivinar = (int) (Math.random() * 101);  // El sistema genera un numero al azar.

        do {
            numero = Integer.parseInt(JOptionPane.showInputDialog(null, "Usted debe adivinar "
                    + "un número de 0 a 100. Ingrese un numero y se le indicará si adivinó, si es mayor o menor."));
            contador++; // Con contador contamos los intentos.
            if (numero < numeroAAdivinar) { // Le informa al usuario que el numero a adivinar es mayor.
                System.out.println("El número es mayor.");
            } else if (numero > numeroAAdivinar) { // Le informa al usuario que el numero a adivinar es menor.
                System.out.println("El número es menor.");
            } else {
                System.out.println("¡Felicidades! Usted adivinó el número :)");
            }
        } while (numero != numeroAAdivinar);
        System.out.println("Usted adivinó el número tras " + contador + " intentos.");
    }
}