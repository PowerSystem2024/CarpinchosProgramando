package test; // Paquete donde se encuentra la clase TestHerencia

import domain.Cliente;
import domain.Empleado; // Importa la clase Empleado del paquete domain
import domain.Persona;
import java.util.Date;

public class TestHerencia { // Clase principal para probar la herencia
    public static void main(String[] args) { // Método principal que se ejecuta al iniciar el programa
        Empleado empleado1 = new Empleado("Nazareno", 70000); // Crea una nueva instancia de Empleado
        System.out.println("empleado1 = " + empleado1); // Imprime la representación de empleado1
//        Date fecha1 = new Date(); // creamos una fecha
//        Cliente cliente1 = new Cliente(fecha1, true, "Nelson", 'M', 39, "San Ramon Nonato 900");
//        System.out.println("cliente1 = " + cliente1);
//        
//        Persona persona1 = new Persona();
    }
}