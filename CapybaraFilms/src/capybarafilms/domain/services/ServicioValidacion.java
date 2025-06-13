package capybarafilms.domain.services;

import capybarafilms.domain.entities.Cliente;
import java.util.Scanner;

public class ServicioValidacion {

    private final Scanner entrada = new Scanner(System.in); // Scanner para leer la entrada del usuario

    // Método que obtiene los datos del cliente y valida la información
    public Cliente obtenerDatosCliente() {
        String nombre; // Declarar fuera del bucle
        do {
            System.out.println("Por favor, Ingrese su nombre: ");
            nombre = entrada.nextLine(); // Lee el nombre del cliente
            if (nombre.isEmpty()) {
                System.out.println("El nombre no puede estar vacío. Intente de nuevo.");
            }
        } while (nombre.isEmpty()); // Repite hasta que el nombre sea válido

        String apellido; // Declarar fuera del bucle
        do {
            System.out.println("Ahora ingrese su apellido: ");
            apellido = entrada.nextLine(); // Lee el apellido del cliente
            if (apellido.isEmpty()) {
                System.out.println("El apellido no puede estar vacío. Intente de nuevo.");
            }
        } while (apellido.isEmpty()); // Repite hasta que el apellido sea válido
        String dni = obtenerDniValido(); // Obtiene un DNI válido
        String mail;
        // Ciclo para validar el correo electrónico
        do {
            System.out.println("Ingrese su mail (debe contener '@' y terminar con '.com'): ");
            mail = entrada.nextLine(); // Lee el correo electrónico
            // Verifica que el correo contenga '@' y termine en '.com'
            if (!mail.contains("@") || !mail.endsWith(".com")) {
                System.out.println("Correo electrónico inválido.");
            }
        } while (!mail.contains("@") || !mail.endsWith(".com")); // Repite hasta que el correo sea válido

        return new Cliente(nombre, apellido, dni, mail); // Devuelve un nuevo cliente con los datos ingresados
    }

    // Método que valida el DNI del cliente
    private String obtenerDniValido() {
        String dni;
        // Ciclo hasta que se ingrese un DNI válido
        while (true) {
            System.out.println("Ahora ingrese su DNI (8 dígitos): ");
            dni = entrada.nextLine(); // Lee el DNI ingresado por el usuario

            // Verifica que el DNI tenga 8 dígitos, sean solo números y no comience con "00"
            if (dni.length() != 8 || !esSoloDigitos(dni) || dni.startsWith("00")) {
                System.out.println("DNI inválido. Intente nuevamente.");
            } else {
                break; // Sale del ciclo si el DNI es válido
            }
        }
        return dni; // Devuelve el DNI válido
    }

    // Método que verifica si una cadena contiene solo dígitos
    public static boolean esSoloDigitos(String dni) {
        // Verifica si todos los caracteres de la cadena son dígitos
        return dni.chars().allMatch(Character::isDigit);
    }

    // Método que verifica si una cadena es un número
    public static boolean esNumero(String str) {
        for (int i = 0; i < str.length(); i++) { // Usamos un bucle for que va desde el primer hasta el último carácter de la cadena.
            // Si algún carácter no es un dígito, devolver false
            if (!Character.isDigit(str.charAt(i))) { // Utilizamos Character.isDigit() para ver si el carácter actual es un número.
                return false;
            }
        }
        // Si todos los caracteres son dígitos, devolver true
        return true;
    }
}