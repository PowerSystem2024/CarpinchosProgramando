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

    private final Scanner entrada = new Scanner(System.in); 

       public void iniciarCompra() {
        // Mensaje de bienvenida
        System.out.println("----------------------------------------------------");
        System.out.println("--   Bienvenido/a a Capybara's Films!   --");
        System.out.println("----------------------------------------------------");
        System.out.println("Disfruta de la mejor experiencia de cine.\n");
    }

       
       
    public void mostrarPeliculas() {
        System.out.println("¿Qué película desea ver?");
        int index = 1; 
        for (Pelicula pelicula : Catalogo.getPeliculas()) {
            System.out.println(index + ") " + pelicula.getNombre());
            index++; 
        }
    }

    
    
    public int seleccionarPelicula() {
        int opcion = 0;
        boolean entradaValida = false;

            while (!entradaValida) {
            System.out.println("Seleccione el número de la película:");
            String input = entrada.nextLine(); 
            if (ServicioValidacion.esNumero(input)) {
                opcion = Integer.parseInt(input);
                if (opcion >= 1 && opcion <= Catalogo.getPeliculas().size()) {
                    entradaValida = true; 
                } else {
                    System.out.println("Opción inválida. Elija un número entre 1 y " + Catalogo.getPeliculas().size() + ".");
                }
            } else {
                System.out.println("Entrada inválida. Por favor, ingrese un número.");
            }
        }
        return opcion - 1;
    }

    
    
    
    public int solicitarCantidadEntradas() {
        int cantidad = 0;
        boolean entradaValida = false; 
            while (!entradaValida) {
            System.out.println("¿Cuántas entradas desea comprar?");
            String input = entrada.nextLine(); 
            if (ServicioValidacion.esNumero(input)) {
                cantidad = Integer.parseInt(input); 
                if (cantidad <= 0) {
                    System.out.println("La cantidad debe ser mayor que cero.");
                } else {
                    entradaValida = true; 
                }
            } else {
                System.out.println("Entrada inválida. Por favor, ingrese un número.");
            }
        }
        return cantidad; 
    }

    
    
    
public List<Butaca> seleccionarButacas(int cantidadEntradas, Sala sala) {
    List<Butaca> butacasSeleccionadas = new ArrayList<>();

    mostrarMatrizButacas(sala);

       for (int i = 0; i < cantidadEntradas; i++) {
        int fila, butaca;
        do {
            System.out.println("Ingrese la fila (0 a 11) para la entrada " + (i + 1) + ": ");
            fila = entrada.nextInt();
            while (fila >= 12 || fila < 0) {
                System.out.println("Número de fila no válido");
                fila = entrada.nextInt();
            }
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
    int filas = 12; 
    int butacasPorFila = 12;

    System.out.print("   "); 
    for (int b = 0; b < butacasPorFila; b++) {
        System.out.print(" " + b + " "); 
    }
    System.out.println(); 
    for (int fila = 0; fila < filas; fila++) {
        System.out.print(fila + " ");
        for (int butaca = 0; butaca < butacasPorFila; butaca++) {
            Butaca b = sala.getButaca(new Ubicacion(fila, butaca)); 
            if (b.isEstado()) {
                System.out.print("[X] ");
            } else {
                System.out.print("[ ] "); 
            }
        }
        System.out.println();
    }
}



    public Reserva realizarReserva(Cliente cliente, Sala sala, Candy candy, List<Butaca> butacas) {
           return new Reserva(cliente, sala, candy, butacas);
    }

    
    
public Candy seleccionarCombo() {
       System.out.println("""
        ¿Desea comprar algún combo de nuestro candy?
        1) Sí
        2) No""");

    int opcionCombo;
    while (true) {
        String input = entrada.nextLine(); 
        if (ServicioValidacion.esNumero(input) && input.length() > 0) {
            opcionCombo = Integer.parseInt(input);
            if (opcionCombo == 1) {
                break; 
            } else if (opcionCombo == 2) {
                return null;
            } else {
                System.out.println("Opción inválida. Por favor, elija 1 o 2.");
            }
        } else {
            System.out.println("Entrada inválida. Por favor, ingrese un número.");
        }
    }
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