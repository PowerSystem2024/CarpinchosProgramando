package test;

import operaciones.Operaciones;

public class TestOperaciones {

    public static void main(String[] args) {
        var resultado = Operaciones.sumar(7, 9);
        System.out.println("resultado = " + resultado);
        
        var resultado2 = Operaciones.sumar(5.0, 7);//Con el método double, al menos uno debe ser de tipo double
        System.out.println("resultado2 = " + resultado2);
        
        var resultado3 = Operaciones.sumar(8, 6L);//el 6(tipo Long) busca el más compatible, en éste caso el double
        System.out.println("resultado3 = " +resultado3);
        
        
    }

}
