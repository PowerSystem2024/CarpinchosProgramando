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
import capybarafilms.domain.entities.types.Ubicacion;

public class ServicioCompraEntradas {
    private final Scanner entrada = new Scanner(System.in); // Scanner para leer la entrada del usuario

    // Método que inicia la interacción y muestra el mensaje de bienvenida
    public void iniciarCompra() {
        // Mensaje de bienvenida
        System.out.println("---------------------------------------------------");
        System.out.println(" ¡Bienvenido/a a Capybara's Films! ");
        System.out.println("---------------------------------------------------");
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

    // Método para seleccionar las butacas
    public List<Butaca> seleccionarButacas(int cantidadEntradas, Sala sala) {
        List<Butaca> butacasSeleccionadas = new ArrayList<>(); // Lista para almacenar las butacas seleccionadas

        // Ciclo para seleccionar butacas según la cantidad de entradas
        for (int i = 0; i < cantidadEntradas; i++) {
            int fila, butaca; // Variables para la fila y la butaca
            System.out.println("Por favor seleccione las butacas que desea ocupar: ");
            do {
                // Solicita al usuario que ingrese la fila
                System.out.println("Ingrese la fila (0 a 11) para la entrada " + (i + 1) + ": ");
                fila = entrada.nextInt();
                while (fila >= 12 || fila < 0) {
                    System.out.println("Número de fila no válido");
                    fila = entrada.nextInt(); // Vuelve a solicitar una fila válida
                }

                // Solicita al usuario que ingrese el número de butaca
                System.out.println("Ingrese el número de butaca (0 a 11) para la entrada " + (i + 1) + ": ");
                butaca = entrada.nextInt();
                while (butaca >= 12 || butaca < 0) {
                    System.out.println("Número de butaca no válido");
                    butaca = entrada.nextInt(); // Vuelve a solicitar una butaca válida
                }

                Ubicacion ubicacion = new Ubicacion(fila, butaca); // Crea la ubicación de la butaca seleccionada
                // Verifica si la butaca está ocupada
                if (sala.butacaEstaOcupada(ubicacion)) {
                    System.out.println("La butaca está ocupada. Intente con otra.");
                } else {
                    Butaca butacaSeleccionada = sala.getButaca(ubicacion); // Obtiene la butaca seleccionada
                    butacasSeleccionadas.add(butacaSeleccionada); // Agrega la butaca a la lista
                    sala.asignarButaca(ubicacion); // Asigna la butaca en la sala
                    break; // Sale del bucle si la butaca es válida
                }
            } while (true); // Repite hasta seleccionar una butaca válida
        }
        return butacasSeleccionadas; // Devuelve la lista de butacas seleccionadas
    }

    // Método para crear una reserva
    public Reserva realizarReserva(Cliente cliente, Sala sala, Candy candy, List<Butaca> butacas) {
        // Crea y devuelve una nueva reserva con los datos proporcionados
        return new Reserva(cliente, sala, candy, butacas);
    }
}