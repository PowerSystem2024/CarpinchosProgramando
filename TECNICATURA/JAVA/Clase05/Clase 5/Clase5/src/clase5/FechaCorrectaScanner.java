//Pedir el dia, mes, y año de una fecha e indicar si la fecha es correcta. 
//Suponiendo que todos los meses son de 30 dias.
package clase5;

import java.util.Scanner;

public class FechaCorrectaScanner {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.print("Introduce el día: ");
        int dia = entrada.nextInt();

        System.out.print("Introduce el mes: ");
        int mes = entrada.nextInt();

        System.out.print("Introduce el año: ");
        int año = entrada.nextInt();

        if ((dia != 0) && (dia <= 30)) {
            if ((mes != 0) && (mes <= 12)) {
                if ((año != 0) && (año <= 2024)) {
                    System.out.println("La fecha ingresada es: "+dia+"/"+mes+"/"+año);
                }
                else{
                    System.out.println("Fecha incorrecta, año incorrecto.");
                }
            }
            else{
              System.out.println("Fecha incorrecta, mes incorrecto.");  
            }
        }
        else{
            System.out.println("Fecha incorrecta, dia incorrecto.");
        }
    }
}