package capybarafilms.domain.services;

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

public class ServicioCompraEntradas {

    private final Scanner entrada = new Scanner(System.in); // Scanner para leer la entrada del usuario

    // Método que inicia la interacción y muestra el mensaje de bienvenida
    public void iniciarCompra() {
        // Mensaje de bienvenida
        System.out.println("----------------------------------------------------");
        System.out.println("--   Bienvenido/a a Capybara's Films!   --");
        System.out.println("----------------------------------------------------");
        System.out.println("Disfruta de la mejor experiencia de cine.\n");
    }

    // Método para mostrar las películas disponibles
    public void mostrarPeliculas() {
        System.out.println("¿Qué película desea ver?");
        int index = 1; // Contador para numerar las películas
        // Recorre y muestra las películas del catálogo
        for (Pelicula pelicula : Catalogo.getPeliculas()) {
            System.out.println(index + ") " + pelicula.getNombre());
            index++; // Incrementa el contador
        }
    }

    // Método para seleccionar una película
    public int seleccionarPelicula() {
        int opcion = 0;
        boolean entradaValida = false; // Bandera para verificar si la entrada es válida

        // Ciclo hasta que el usuario ingrese una opción válida
        while (!entradaValida) {
            System.out.println("Seleccione el número de la película:");
            String input = entrada.nextLine(); // Lee la entrada del usuario
            // Verifica si la entrada es un número
            if (ServicioValidacion.esNumero(input)) {
                opcion = Integer.parseInt(input); // Convierte la entrada a número
                // Verifica si la opción está en el rango válido
                if (opcion >= 1 && opcion <= Catalogo.getPeliculas().size()) {
                    entradaValida = true; // Marca la entrada como válida
                } else {
                    System.out.println("Opción inválida. Elija un número entre 1 y " + Catalogo.getPeliculas().size() + ".");
                }
            } else {
                System.out.println("Entrada inválida. Por favor, ingrese un número.");
            }
        }
        return opcion - 1; // Devuelve la opción seleccionada (ajustada para ser índice de lista)
    }

    // Método para solicitar la cantidad de entradas
    public int solicitarCantidadEntradas() {
        int cantidad = 0;
        boolean entradaValida = false; // Bandera para validar la entrada

        // Ciclo hasta que se ingrese una cantidad válida
        while (!entradaValida) {
            System.out.println("¿Cuántas entradas desea comprar?");
            String input = entrada.nextLine(); // Lee la entrada del usuario
            // Verifica si la entrada es un número
            if (ServicioValidacion.esNumero(input)) {
                cantidad = Integer.parseInt(input); // Convierte la entrada a entero
                if (cantidad <= 0) {
                    System.out.println("La cantidad debe ser mayor que cero.");
                } else {
                    entradaValida = true; // La cantidad es válida
                }
            } else {
                System.out.println("Entrada inválida. Por favor, ingrese un número.");
            }
        }
        return cantidad; // Devuelve la cantidad de entradas
    }

public List<Butaca> seleccionarButacas(int cantidadEntradas, Sala sala) {
    List<Butaca> butacasSeleccionadas = new ArrayList<>();

    // Mostrar la matriz de butacas
    mostrarMatrizButacas(sala);

    // Ciclo para seleccionar butacas según la cantidad de entradas
    for (int i = 0; i < cantidadEntradas; i++) {
        int fila, butaca;
        do {
            // Solicita al usuario que ingrese la fila
            System.out.println("Ingrese la fila (0 a 11) para la entrada " + (i + 1) + ": ");
            fila = entrada.nextInt();
            while (fila >= 12 || fila < 0) {
                System.out.println("Número de fila no válido");
                fila = entrada.nextInt();
            }
            // Solicita al usuario que ingrese el número de butaca
            System.out.println("Ingrese el número de butaca (0 a 11) para la entrada " + (i + 1) + ": ");
            butaca = entrada.nextInt();
            while (butaca >= 12 || butaca < 0) {
                System.out.println("Número de butaca no válido");
                butaca = entrada.nextInt();
            }
            Ubicacion ubicacion = new Ubicacion(fila, butaca);
            if (sala.butacaEstaOcupada(ubicacion)) {
                System.out.println("La butaca está ocupada. Intente con otra.");
            } else {
                Butaca butacaSeleccionada = sala.getButaca(ubicacion);
                butacasSeleccionadas.add(butacaSeleccionada);
                sala.asignarButaca(ubicacion);
                break;
            }
        } while (true);
    }
    return butacasSeleccionadas;
}

public void mostrarMatrizButacas(Sala sala) {
    // Suponiendo que sala tiene un método para obtener la capacidad
    int filas = 12; // Cambia esto según la cantidad de filas
    int butacasPorFila = 12; // Cambia esto según la cantidad de butacas por fila

    System.out.print("   "); // Espacio para el encabezado de butacas
    for (int b = 0; b < butacasPorFila; b++) {
        System.out.print(" " + b + " "); // Imprime los números de las butacas
    }
    System.out.println(); // Nueva línea después del encabezado

    // Imprime cada fila con su número
    for (int fila = 0; fila < filas; fila++) {
        System.out.print(fila + " "); // Imprime el número de la fila
        for (int butaca = 0; butaca < butacasPorFila; butaca++) {
            Butaca b = sala.getButaca(new Ubicacion(fila, butaca)); // Obtiene la butaca actual
            // Agrega un símbolo dependiendo del estado de la butaca
            if (b.isEstado()) {
                System.out.print("[X] "); // Ocupada
            } else {
                System.out.print("[ ] "); // Disponible
            }
        }
        System.out.println(); // Salto de línea al final de cada fila
    }
}

    // Método para crear una reserva
    public Reserva realizarReserva(Cliente cliente, Sala sala, Candy candy, List<Butaca> butacas) {
        // Crea y devuelve una nueva reserva con los datos proporcionados
        return new Reserva(cliente, sala, candy, butacas);
    }

public Candy seleccionarCombo() {
    // Pregunta inicial sobre la compra del combo
    System.out.println("""
        ¿Desea comprar algún combo de nuestro candy?
        1) Sí
        2) No""");

    int opcionCombo;
    while (true) {
        String input = entrada.nextLine(); // Usa el Scanner de la clase
        if (ServicioValidacion.esNumero(input) && input.length() > 0) {
            opcionCombo = Integer.parseInt(input);
            if (opcionCombo == 1) {
                // Si elige "Sí", se procede a seleccionar el tipo de combo
                break; // Salimos del bucle para continuar con la selección de tamaño
            } else if (opcionCombo == 2) {
                // Si elige "No", se retorna null o un objeto Candy vacío
                return null; // O puedes retornar new Candy(TipoCandy.SIN_COMBO) si lo defines
            } else {
                System.out.println("Opción inválida. Por favor, elija 1 o 2.");
            }
        } else {
            System.out.println("Entrada inválida. Por favor, ingrese un número.");
        }
    }
    // Selección del tamaño de combo
    TipoCandy tipoCandy = null;
    int opcion;
    do {
        System.out.println("""
            ¿Qué tamaño de combo desea?
            1) CHICO: Una bolsa de pochoclos  + una gaseosa mediana.
            2) MEDIANO: Un balde de pochoclos + dos gaseosas medianas.
            3) GRANDE: Un balde familiar de pochoclos + cuatro bebidas grandes.""");

        String input = entrada.nextLine();
        if (ServicioValidacion.esNumero(input) && input.length() > 0) {
            opcion = Integer.parseInt(input);
            switch (opcion) {
                case 1 -> tipoCandy = TipoCandy.CHICO;
                case 2 -> tipoCandy = TipoCandy.MEDIANO;
                case 3 -> tipoCandy = TipoCandy.GRANDE;
                default -> System.out.println("Opción inválida.");
            }
        } else {
            System.out.println("Entrada inválida.");
        }
    } while (tipoCandy == null);
    
    return new Candy(tipoCandy);
 }
}