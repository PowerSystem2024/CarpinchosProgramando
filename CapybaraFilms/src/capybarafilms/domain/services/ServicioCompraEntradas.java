package capybarafilms.domain.services; // Define el paquete donde se encuentra la clase

import java.util.ArrayList; // Importa la clase ArrayList para manejar listas dinámicas
import java.util.List; // Importa la interfaz List para trabajar con listas
import java.util.Scanner; // Importa la clase Scanner para leer entradas del usuario
// Importa las entidades necesarias desde el paquete domain.entities
import capybarafilms.domain.entities.Butaca;
import capybarafilms.domain.entities.Candy;
import capybarafilms.domain.entities.Catalogo;
import capybarafilms.domain.entities.Cliente;
import capybarafilms.domain.entities.Pelicula;
import capybarafilms.domain.entities.Reserva;
import capybarafilms.domain.entities.Sala;
import capybarafilms.domain.entities.types.TipoCandy; // Importa los tipos de Candy
import capybarafilms.domain.entities.types.Ubicacion; // Importa la clase Ubicacion para las butacas

public class ServicioCompraEntradas { // Clase que gestiona la compra de entradas

    private final Scanner entrada = new Scanner(System.in); // Inicializa un escáner para leer entradas del usuario

    public void iniciarCompra() { // Método para iniciar el proceso de compra
        // Mensaje de bienvenida
        System.out.println("--------------------------------------------------------------------");
        System.out.println("*              Bienvenido/a a Capybara's Films!               *");
        System.out.println("--------------------------------------------------------------------");
        System.out.println("***    Disfruta de la mejor experiencia de cine.     ***");
        System.out.println("");
        System.out.println("A continuación ingrese sus datos para adquirir las entradas a la función de cine.");
    }

    public void mostrarPeliculas() { // Método para mostrar las películas disponibles
        System.out.println("¿Qué película desea ver?"); // Pregunta al usuario qué película quiere ver
        int index = 1; // Inicializa el índice para enumerar las películas
        for (Pelicula pelicula : Catalogo.getPeliculas()) { // Itera sobre las películas en el catálogo
            System.out.println(index + ") " + pelicula.getNombre()); // Muestra el índice y el nombre de la película
            index++; // Incrementa el índice
        }
    }

    public int seleccionarPelicula() { // Método para seleccionar una película
        int opcion = 0; // Inicializa la opción elegida
        boolean entradaValida = false; // Bandera para verificar la validez de la entrada

        while (!entradaValida) { // Ciclo hasta que la entrada sea válida
            System.out.println("Seleccione el número de la película:"); // Solicita al usuario seleccionar una película
            String input = entrada.nextLine(); // Lee la entrada del usuario
            if (ServicioValidacion.esNumero(input)) { // Verifica si la entrada es un número
                opcion = Integer.parseInt(input); // Convierte la entrada a un entero
                // Verifica si la opción está dentro del rango válido
                if (opcion >= 1 && opcion <= Catalogo.getPeliculas().size()) {
                    entradaValida = true; // Marca la entrada como válida
                } else {
                    System.out.println("Opción inválida. Elija un número entre 1 y " + Catalogo.getPeliculas().size() + "."); // Mensaje de error
                }
            } else {
                System.out.println("Entrada inválida. Por favor, ingrese un número."); // Mensaje de error para entrada no numérica
            }
        }
        return opcion - 1; // Devuelve el índice de la película seleccionada (ajustado a 0)
    }

    public int solicitarCantidadEntradas() { // Método para solicitar la cantidad de entradas
        int cantidad = 0; // Inicializa la cantidad de entradas
        boolean entradaValida = false; // Bandera para verificar la validez de la entrada
        while (!entradaValida) { // Ciclo hasta que la entrada sea válida
            System.out.println("¿Cuántas entradas desea comprar?"); // Pregunta al usuario la cantidad de entradas
            String input = entrada.nextLine(); // Lee la entrada del usuario
            if (ServicioValidacion.esNumero(input)) { // Verifica si la entrada es un número
                cantidad = Integer.parseInt(input); // Convierte la entrada a un entero
                if (cantidad <= 0) { // Verifica si la cantidad es válida
                    System.out.println("La cantidad debe ser mayor que cero."); // Mensaje de error
                } else {
                    entradaValida = true; // Marca la entrada como válida
                }
            } else {
                System.out.println("Entrada inválida. Por favor, ingrese un número."); // Mensaje de error para entrada no numérica
            }
        }
        return cantidad; // Devuelve la cantidad de entradas solicitadas
    }

    public List<Butaca> seleccionarButacas(int cantidadEntradas, Sala sala) { // Método para seleccionar butacas
        List<Butaca> butacasSeleccionadas = new ArrayList<>(); // Lista para almacenar las butacas seleccionadas

        mostrarMatrizButacas(sala); // Muestra la matriz de butacas disponibles

        for (int i = 0; i < cantidadEntradas; i++) { // Ciclo para seleccionar la cantidad de entradas deseada
            int fila, butaca; // Variables para almacenar la fila y número de butaca
            do {
                // Solicita la fila para la butaca
                System.out.println("Ingrese la fila (0 a 11) para la entrada " + (i + 1) + ": ");
                fila = entrada.nextInt(); // Lee la fila del usuario
                // Verifica si la fila es válida
                while (fila >= 12 || fila < 0) {
                    System.out.println("Número de fila no válido"); // Mensaje de error
                    fila = entrada.nextInt(); // Vuelve a solicitar la fila
                }
                // Solicita el número de butaca
                System.out.println("Ingrese el número de butaca (0 a 11) para la entrada " + (i + 1) + ": ");
                butaca = entrada.nextInt(); // Lee el número de butaca del usuario
                // Verifica si la butaca es válida
                while (butaca >= 12 || butaca < 0) {
                    System.out.println("Número de butaca no válido"); // Mensaje de error
                    butaca = entrada.nextInt(); // Vuelve a solicitar el número de butaca
                }
                Ubicacion ubicacion = new Ubicacion(fila, butaca); // Crea una nueva ubicación para la butaca
                if (sala.butacaEstaOcupada(ubicacion)) { // Verifica si la butaca está ocupada
                    System.out.println("La butaca está ocupada. Intente con otra."); // Mensaje de error
                } else {
                    Butaca butacaSeleccionada = sala.getButaca(ubicacion); // Obtiene la butaca seleccionada
                    butacasSeleccionadas.add(butacaSeleccionada); // Agrega la butaca a la lista de seleccionadas
                    sala.asignarButaca(ubicacion); // Marca la butaca como ocupada en la sala
                    break; // Sale del ciclo al seleccionar una butaca válida
                }
            } while (true); // Repite hasta que se seleccione una butaca válida
        }
        return butacasSeleccionadas; // Devuelve la lista de butacas seleccionadas
    }

    public void mostrarMatrizButacas(Sala sala) { // Método para mostrar la matriz de butacas
        int filas = 12; // Número total de filas
        int butacasPorFila = 12; // Número de butacas por fila

        System.out.print("   "); // Espacio para la cabecera
        for (int b = 0; b < butacasPorFila; b++) { // Muestra los números de butacas en la cabecera
            System.out.print(" " + b + " "); // Imprime el número de butaca
        }
        System.out.println(); // Salto de línea
        for (int fila = 0; fila < filas; fila++) { // Itera sobre las filas
            System.out.print(fila + " "); // Imprime el número de fila
            for (int butaca = 0; butaca < butacasPorFila; butaca++) { // Itera sobre las butacas
                Butaca b = sala.getButaca(new Ubicacion(fila, butaca)); // Obtiene la butaca de la sala
                if (b.isEstado()) { // Verifica si la butaca está ocupada
                    System.out.print("[X] "); // Imprime '[X]' si la butaca está ocupada
                } else {
                    System.out.print("[ ] "); // Imprime '[ ]' si la butaca está libre
                }
            }
            System.out.println(); // Salto de línea al finalizar la fila
        }
    }

    public Reserva realizarReserva(Cliente cliente, Sala sala, Candy candy, List<Butaca> butacas) { // Método para realizar una reserva
        return new Reserva(cliente, sala, candy, butacas); // Crea y devuelve una nueva reserva
    }

    public Candy seleccionarCombo() { // Método para seleccionar un combo de snacks
        // Mensaje para preguntar si desea comprar un combo
        System.out.println("""
        ¿Desea comprar algún combo de nuestro candy?
        1) Sí
        2) No""");
        Integer opcionCombo; // Variable para almacenar la opción del combo
        entrada.nextLine();
        while (true) { // Ciclo hasta que se seleccione una opción válida
            String input = entrada.nextLine(); // Lee la entrada del usuario
            if (!input.isEmpty() && ServicioValidacion.esNumero(input)) {  // Verifica si la entrada es un número
                opcionCombo = Integer.parseInt(input); // Convierte la entrada a un entero
                if (opcionCombo == 1) { // Si elige 'Sí'
                    break; // Sale del ciclo para seleccionar el combo
                } else if (opcionCombo == 2) { // Si elige 'No'
                    return null; // Devuelve null si no desea combo
                } else {
                    System.out.println("Opción inválida. Por favor, elija 1 o 2."); // Mensaje de error
                }
            } else {
                System.out.println("Entrada inválida. Por favor, ingrese un número."); // Mensaje de error para entrada no numérica
            }
        }
        TipoCandy tipoCandy = null; // Inicializa el tipo de candy
        int opcion; // Variable para la opción del tamaño del combo
        do {
            // Pregunta por el tamaño del combo
            System.out.println("""
            ¿Qué tamaño de combo desea?
            1) CHICO: Una bolsa de pochoclos  + una gaseosa mediana.
            2) MEDIANO: Un balde de pochoclos + dos gaseosas medianas.
            3) GRANDE: Un balde familiar de pochoclos + cuatro bebidas grandes.""");
            String input = entrada.nextLine(); // Lee la entrada del usuario
            if (ServicioValidacion.esNumero(input) && input.length() > 0) { // Verifica si la entrada es un número
                opcion = Integer.parseInt(input); // Convierte la entrada a un entero
                switch (opcion) { // Selecciona el tipo de combo basado en la opción
                    case 1 ->
                        tipoCandy = TipoCandy.CHICO; // Asigna tipo CHICO
                    case 2 ->
                        tipoCandy = TipoCandy.MEDIANO; // Asigna tipo MEDIANO
                    case 3 ->
                        tipoCandy = TipoCandy.GRANDE; // Asigna tipo GRANDE
                    default ->
                        System.out.println("Opción inválida."); // Mensaje de error para opción no válida
                }
            } else {
                System.out.println("Entrada inválida."); // Mensaje de error para entrada no numérica
            }
        } while (tipoCandy == null); // Repite hasta que se seleccione un tipo de candy válido

        return new Candy(tipoCandy); // Devuelve un nuevo objeto Candy con el tipo seleccionado
    }
}