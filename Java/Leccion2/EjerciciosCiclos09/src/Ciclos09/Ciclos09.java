package Ciclos09;

import java.util.Scanner;




public class Ciclos09 {


        public static void main(String[] args) {
            Scanner entrada = new Scanner(System.in);
            System.out.println("Digite el día: ");
            int dia = entrada.nextInt();
            System.out.println("Digite el mes: ");
            int mes = entrada.nextInt();
            System.out.println("Digite el año: ");
            int anio = entrada.nextInt();

            if ((dia > 0) && (dia <= 30)) {
                if ((mes > 0) && (mes <= 12)) {
                    if ((anio > 0) && (anio <= 2022)) {
                        System.out.println("La fecha ingresada es: " + dia + "/" + mes + "/" + anio);
                    } else {
                        System.out.println("Fecha incorrecta, año incorrecto");
                    }
                } else {
                    System.out.println("Fecha incorrecta, mes incorrecto");
                }
            } else {
                System.out.println("Fecha incorrecta, día incorrecto");
            }
        }
    }
