package capybarafilms.test;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import capybarafilms.domain.entities.Butaca;
import capybarafilms.domain.entities.Candy;
import capybarafilms.domain.entities.Catalogo;
import capybarafilms.domain.entities.Cliente;
import capybarafilms.domain.entities.Pelicula;
import capybarafilms.domain.entities.Reserva;
import capybarafilms.domain.entities.Sala;
import capybarafilms.domain.entities.types.TipoCandy;
import capybarafilms.domain.entities.types.Ubicacion;

public class ComprarEntradaTest {

    private static String menuMensaje; // Mensaje que se muestra en el menú principal
    private static final Scanner entrada = new Scanner(System.in); // Scanner para leer la entrada del usuario

    public static void main(String[] args) {
        // Inicializa el mensaje de bienvenida
        menuMensaje = """
****************************
* Bienvenido a Capybara Films *
****************************
Por favor ingrese sus datos para continuar con la compra de la/s entrada/s.
""";

        mostrarMensaje(); // Muestra el mensaje de bienvenida
        Cliente cliente = obtenerDatosCliente(); // Llama al método para obtener los datos del cliente
        mostrarPeliculas(); // Muestra las películas disponibles
        int peliculaIndex = seleccionarPelicula(); // Permite al usuario seleccionar una película
        int cantidadEntradas = solicitarCantidadEntradas(); // Pregunta cuántas entradas desea comprar
        boolean agregarCombo = agregarCombo(); // Pregunta si se desea agregar un combo de snacks
        Candy candy = null; // Inicializa la variable de tipo Candy

        // Si el usuario quiere agregar un combo, se selecciona
        if (agregarCombo) {
            candy = seleccionarCombo(); // Llama al método para seleccionar el tipo de combo
            System.out.println("Has agregado un combo: " + candy.getTipo().getNombre()); // Muestra el tipo de combo agregado
        }

        // Obtiene la película seleccionada y crea una nueva sala para esa película
        Pelicula peliculaSeleccionada = Catalogo.getPeliculas().get(peliculaIndex);
        Sala sala = new Sala(peliculaSeleccionada); // Crea una sala basada en la película seleccionada
        List<Butaca> butacasAsignadas = seleccionarButacas(cantidadEntradas, sala); // Llama al método para seleccionar las butacas
        Reserva reserva = new Reserva(cliente, sala, candy, butacasAsignadas); // Crea una nueva reserva con los datos ingresados

        // Muestra el resumen de la reserva al usuario
        reserva.mostrarResumen();

        // Agradece al usuario por su compra
        System.out.println("¡Gracias por su compra, " + cliente.getNombre() + "!");
    }

    // Método que obtiene y valida los datos del cliente
    private static Cliente obtenerDatosCliente() {
        System.out.println("Ingrese su nombre: ");
        String nombre = entrada.nextLine(); // Lee el nombre del cliente

        System.out.println("Ingrese su apellido: ");
        String apellido = entrada.nextLine(); // Lee el apellido del cliente

        // Llama al método para obtener un DNI válido
        String dni = obtenerDniValido();

        // Valida el correo electrónico ingresado por el usuario
        String mail;
        do {
            System.out.println("Ingrese su mail (debe contener '@' y '.com'): ");
            mail = entrada.nextLine(); // Lee el correo electrónico
            if (!mail.contains("@") || !mail.endsWith(".com")) {
                System.out.println("Correo electrónico inválido."); // Mensaje de error si el correo es inválido
            }
        } while (!mail.contains("@") || !mail.endsWith(".com")); // Repite hasta que el correo sea válido

        // Crea y devuelve un nuevo objeto Cliente con los datos ingresados
        return new Cliente(nombre, apellido, dni, mail);
    }

    // Método que obtiene un DNI válido del usuario
    private static String obtenerDniValido() {
        String dni;
        while (true) {
            System.out.println("Ingrese su DNI (8 dígitos): ");
            dni = entrada.nextLine(); // Lee el DNI

            // Verifica que el DNI tenga exactamente 8 dígitos
            if (dni.length() != 8) {
                System.out.println("DNI inválido. Debe tener 8 dígitos."); // Mensaje de error
                continue; // Pide nuevamente el DNI
            }

            // Verifica que el DNI contenga solo dígitos
            if (!esSoloDigitos(dni)) {
                System.out.println("DNI inválido. Debe contener solo números."); // Mensaje de error
                continue; // Pide nuevamente el DNI
            }

            // Verifica que el DNI no comience con dos ceros
            if (dni.startsWith("00")) {
                System.out.println("DNI inválido. No puede empezar con dos ceros."); // Mensaje de error
                continue; // Pide nuevamente el DNI
            }
            break; // Sale del bucle si el DNI es válido
        }
        return dni; // Devuelve el DNI válido
    }

    // Método que verifica si el DNI contiene solo dígitos
    private static boolean esSoloDigitos(String dni) {
        for (char c : dni.toCharArray()) {
            if (!Character.isDigit(c)) {
                return false; // Devuelve false si encuentra un carácter no numérico
            }
        }
        return true; // Devuelve true si todos los caracteres son dígitos
    }

    // Método que muestra las películas disponibles para seleccionar
    private static void mostrarPeliculas() {
        System.out.println("¿Qué película desea ver?");
        int index = 1; // Contador para enumerar las películas
        for (Pelicula pelicula : Catalogo.getPeliculas()) {
            System.out.println(index + ") " + pelicula.getNombre()); // Muestra el nombre de cada película
            index++; // Incrementa el contador
        }
    }

    // Método que permite al usuario seleccionar una película
    private static int seleccionarPelicula() {
        int opcion = 0; // Inicializa la opción seleccionada
        boolean entradaValida = false; // Bandera para verificar la validez de la entrada

        // Repite hasta que el usuario ingrese una opción válida
        while (!entradaValida) {
            System.out.println("Seleccione el número de la película:");
            String input = entrada.nextLine(); // Lee la entrada como cadena

            // Verifica si la entrada es un número y está en el rango
            if (esNumero(input)) {
                opcion = Integer.parseInt(input); // Convierte la cadena a número
                if (opcion >= 1 && opcion <= Catalogo.getPeliculas().size()) {
                    entradaValida = true; // La entrada es válida
                } else {
                    System.out.println("Opción inválida. Por favor, elija un número entre 1 y " + Catalogo.getPeliculas().size() + "."); // Mensaje de error
                }
            } else {
                System.out.println("Entrada inválida. Por favor, ingrese un número."); // Mensaje de error
            }
        }
        return opcion - 1; // Devuelve la opción restando 1 para usarla como índice
    }

    // Método que verifica si una cadena es un número
    private static boolean esNumero(String str) {
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            if (!Character.isDigit(c)) {
                return false; // Devuelve false si encuentra un carácter no numérico
            }
        }
        return true; // Devuelve true si todos los caracteres son dígitos
    }

    // Método que solicita la cantidad de entradas que el usuario desea comprar
    private static int solicitarCantidadEntradas() {
        int cantidad = 0; // Inicializa la cantidad de entradas
        boolean entradaValida = false; // Bandera para verificar la validez de la entrada

        // Repite hasta que el usuario ingrese una cantidad válida
        while (!entradaValida) {
            System.out.println("¿Cuántas entradas desea comprar?");
            String input = entrada.nextLine(); // Lee la entrada como cadena

            if (esNumero(input)) {
                cantidad = Integer.parseInt(input); // Convierte la cadena a entero
                if (cantidad <= 0) {
                    System.out.println("La cantidad debe ser mayor que cero."); // Mensaje de error si la cantidad de entradas no es válida
                } else {
                    entradaValida = true; // La entrada es válida
                }
            } else {
                System.out.println("Entrada inválida. Por favor, ingrese un número."); // Mensaje de error
            }
        }
        return cantidad; // Devuelve la cantidad válida de entradas
    }

    // Método que permite seleccionar las butacas para las entradas compradas
    private static List<Butaca> seleccionarButacas(int cantidadEntradas, Sala sala) {
        List<Butaca> butacasSeleccionadas = new ArrayList<>(); // Lista para almacenar las butacas seleccionadas

        // Itera por la cantidad de entradas solicitadas
        for (int i = 0; i < cantidadEntradas; i++) {
            int fila, butaca; // Inicializa las variables de fila y butaca
            do {
                System.out.println("Ingrese la fila (0 a 11) para la entrada " + (i + 1) + ": ");
                fila = entrada.nextInt(); // Lee la fila seleccionada
               while (fila >= 12 || fila <= -1) {
               
               System.out.println("Numero de fila no valido");
                System.out.println("Ingrese la fila (0 a 11) para la entrada " + (i + 1) + ": ");
                fila = entrada.nextInt(); // Lee la fila seleccionada
               }

                System.out.println("Ingrese el número de butaca (0 a 11) para la entrada " + (i + 1) + ": ");
                butaca = entrada.nextInt(); // Lee el número de butaca seleccionada
                while (butaca >= 12 || butaca <= -1) {
               
                    System.out.println("Numero de butaca no valido");
                     System.out.println("Ingrese la butaca (0 a 11) para la entrada " + (i + 1) + ": ");
                     butaca = entrada.nextInt(); // Lee la fila seleccionada
                    }
                // Verifica que los números de fila y butaca estén dentro del rango permitido
                if (fila < 0 || fila >= sala.getCapacidad() || butaca < 0 || butaca >= sala.getCapacidad()) {
                    System.out.println("Fila o butaca fuera de rango. Intente de nuevo."); // Mensaje de error
                    continue; // Vuelve a pedir la entrada
                }

                Ubicacion ubicacion = new Ubicacion(fila, butaca); // Crea la ubicación de la butaca después de validar

                // Verifica si la butaca está ocupada
                if (sala.butacaEstaOcupada(ubicacion)) {
                    System.out.println("La butaca está ocupada. Intente con otra."); // Mensaje de error si la butaca está ocupada
                } else {
                    Butaca butacaSeleccionada = sala.getButaca(ubicacion); // Obtiene la butaca seleccionada
                    butacasSeleccionadas.add(butacaSeleccionada); // Añade la butaca seleccionada a la lista
                    sala.asignarButaca(ubicacion); // Asigna la butaca en la sala
                    break; // Sale del bucle si se selecciona una butaca válida
                }
            } while (true); // Continúa hasta que se seleccione una butaca válida
        }
        return butacasSeleccionadas; // Devuelve la lista de butacas seleccionadas
    }

    // Método para preguntar si se desea agregar un combo
    private static boolean agregarCombo() {
        int opcion = 0; // Inicializa la opción seleccionada
        boolean entradaValida = false; // Bandera para verificar la validez de la entrada

        // Repite hasta que el usuario ingrese una opción válida
        while (!entradaValida) {
            System.out.println("""
        Desea agregar algún combo?
        1) Si
        2) No""");

            String input = entrada.nextLine(); // Lee la entrada como cadena

            // Verifica si la entrada es un número y está en el rango
            if (esNumero(input)) {
                opcion = Integer.parseInt(input); // Convierte la cadena a número
                if (opcion >= 1 && opcion <= 2) {
                    entradaValida = true; // La entrada es válida
                } else {
                    System.out.println("Opción inválida. Por favor ingrese 1 para Sí o 2 para No."); // Mensaje de error
                }
            } else {
                System.out.println("Entrada inválida. Por favor, ingrese un número."); // Mensaje de error
            }
        }

        return opcion == 1; // Devuelve true si se seleccionó "Sí"
    }

    // Método para seleccionar un combo
    private static Candy seleccionarCombo() {
        TipoCandy tipoCandy = null; // Inicializa el tipo de candy
        int opcion; // Variable para almacenar la opción seleccionada
        do {
            System.out.println("""
        ¿Qué tamaño de combo desea?
        1) CHICO
        2) MEDIANO
        3) GRANDE""");
            opcion = entrada.nextInt(); // Lee la opción seleccionada
            switch (opcion) {
                case 1 -> tipoCandy = TipoCandy.CHICO; // Selecciona combo chico
                case 2 -> tipoCandy = TipoCandy.MEDIANO; // Selecciona combo mediano
                case 3 -> tipoCandy = TipoCandy.GRANDE; // Selecciona combo grande
                default -> System.out.println("Opción inválida. Por favor ingrese una opción válida."); // Mensaje de error
            }
        } while (tipoCandy == null); // Continúa hasta que se seleccione un tipo de combo

        return new Candy(tipoCandy); // Crea y devuelve el combo
    }

    // Método para mostrar el mensaje de bienvenida
    private static void mostrarMensaje() {
        System.out.println(menuMensaje); // Muestra el mensaje del menú
    }
}
