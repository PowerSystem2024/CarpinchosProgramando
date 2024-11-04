package Test;

import Domain.Cliente;
import Domain.Empleado;
import java.util.Date;

public class TestHerencia {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Wanda",700000);
        System.out.println("empleado1: " + empleado1);

        Date fecha1 = new Date();

        Cliente cliente1 = new Cliente(fecha1,true,"Wanda",'F',25,"Calle falsa 123");
        System.out.println("cliente1: " + cliente1);
    }

}