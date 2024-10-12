package capybarafilms.domain.entities;

import capybarafilms.domain.entities.types.FormatoPelicula; // Importamos el tipo de formato de película.
import java.util.ArrayList; // Importamos la clase para crear listas.
import java.util.List; // Importamos la interfaz para usar listas.

public class Catalogo {

    // Este método devuelve una lista de películas disponibles.
    public static List<Pelicula> getPeliculas() {
        List<Pelicula> peliculas = new ArrayList<>(); // Creamos una nueva lista para las películas.

        // Agregamos películas a la lista con su información (nombre, director, duración, género, idioma y formato).
        peliculas.add(new Pelicula("Shrek", "Andrew Adamson", 90, "Comedia", "Español", FormatoPelicula.DOS_D));
        peliculas.add(new Pelicula("Shrek 2", "Andrew Adamson", 95, "Comedia", "Español", FormatoPelicula.DOS_D));
        peliculas.add(new Pelicula("Titanic", "James Cameron", 195, "Drama", "Español", FormatoPelicula.DOS_D));
        peliculas.add(new Pelicula("Cuando el terror acecha", "John Carpenter", 100, "Terror", "Español", FormatoPelicula.DOS_D));
        peliculas.add(new Pelicula("El Señor de los Anillos: La Comunidad del Anillo", "Peter Jackson", 178, "Aventura", "Español", FormatoPelicula.DOS_D));
        peliculas.add(new Pelicula("El Padrino", "Francis Ford Coppola",  175, "Crimen", "Español", FormatoPelicula.DOS_D));
        peliculas.add(new Pelicula("Forrest Gump", "Robert Zemeckis", 142, "Drama", "Español", FormatoPelicula.DOS_D));
        peliculas.add(new Pelicula("Jurassic Park", "Steven Spielberg",  127, "Ciencia Ficción", "Español", FormatoPelicula.DOS_D));
        peliculas.add(new Pelicula("Star Wars: Episodio IV - Una Nueva Esperanza", "George Lucas", 121, "Ciencia Ficción", "Español", FormatoPelicula.DOS_D));
        peliculas.add(new Pelicula("Matrix", "Lana Wachowski, Lilly Wachowski", 136, "Ciencia Ficción", "Español", FormatoPelicula.DOS_D));
        peliculas.add(new Pelicula("Coco", "Lee Unkrich, Adrian Molina", 105, "Animación", "Español", FormatoPelicula.DOS_D));
        peliculas.add(new Pelicula("La La Land", "Damien Chazelle", 128, "Musical", "Español", FormatoPelicula.DOS_D));
        peliculas.add(new Pelicula("El gran Lebowski", "Joel Coen, Ethan Coen", 117, "Comedia", "Español", FormatoPelicula.DOS_D));
        peliculas.add(new Pelicula("Pulp Fiction", "Quentin Tarantino", 154, "Crimen", "Español", FormatoPelicula.DOS_D));
        peliculas.add(new Pelicula("Los Increíbles", "Brad Bird", 115, "Animación", "Español", FormatoPelicula.DOS_D));
        peliculas.add(new Pelicula("El Rey León", "Roger Allers, Rob Minkoff", 88, "Animación", "Español", FormatoPelicula.DOS_D));
        peliculas.add(new Pelicula("Gladiador", "Ridley Scott", 155, "Acción", "Español", FormatoPelicula.DOS_D));
        peliculas.add(new Pelicula("Avatar", "James Cameron",  162, "Ciencia Ficción", "Español", FormatoPelicula.TRES_D));
        peliculas.add(new Pelicula("Harry Potter y la piedra filosofal", "Chris Columbus", 152, "Aventura", "Español", FormatoPelicula.DOS_D));
        peliculas.add(new Pelicula("Los Vengadores", "Joss Whedon", 143, "Acción", "Español", FormatoPelicula.DOS_D));

        return peliculas; // Devolvemos la lista completa de películas.
    }
}
