package Clase04;
import java.util.Scanner;

public class EjercicioCiclos2 {

    public static void main(String[] args) {
        int numero, suma = 0;
        Scanner entrada = new Scanner(System.in);

        do {
            System.out.println("Ingrese un numero: ");
            numero = entrada.nextInt();
            suma += numero;
        } while (numero != 0);
        System.out.println("La suma de los numeros ingresados es: " + suma);
    }
}