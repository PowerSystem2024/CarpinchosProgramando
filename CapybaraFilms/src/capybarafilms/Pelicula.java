package capybarafilms.domain.entities;

import capybarafilms.domain.entities.types.FormatoPelicula;

public class Pelicula {

    private String nombre; // Almacena el nombre de la película
    private String director; // Almacena el nombre del director de la película
    private int duracion; // Almacena la duración de la película en minutos
    private String genero; // Almacena el género de la película
    private String idioma; // Almacena el idioma en que se presenta la película
    private FormatoPelicula formato; // Almacena el formato de la película (2D, 3D, etc.)

    // Constructor que inicializa todos los atributos de la película
    public Pelicula(String nombre, String director, int duracion, String genero, String idioma, FormatoPelicula formato) {
        this.nombre = nombre; // Asigna el nombre de la película
        this.director = director; // Asigna el director de la película
        this.duracion = duracion; // Asigna la duración de la película
        this.genero = genero; // Asigna el género de la película
        this.idioma = idioma; // Asigna el idioma de la película
        this.formato = formato; // Asigna el formato de la película
    }

    // Método para obtener el nombre de la película
    public String getNombre() {
        return nombre;
    }

    // Método para establecer un nuevo nombre a la película
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    // Método para obtener el director de la película
    public String getDirector() {
        return director;
    }

    // Método para establecer un nuevo director a la película
    public void setDirector(String director) {
        this.director = director;
    }

    // Método para obtener la duración de la película
    public int getDuracion() {
        return duracion;
    }

    // Método para establecer una nueva duración a la película
    public void setDuracion(int duracion) {
        this.duracion = duracion;
    }

    // Método para obtener el género de la película
    public String getGenero() {
        return genero;
    }

    // Método para establecer un nuevo género a la película
    public void setGenero(String genero) {
        this.genero = genero;
    }

    // Método para obtener el idioma de la película
    public String getIdioma() {
        return idioma;
    }

    // Método para establecer un nuevo idioma a la película
    public void setIdioma(String idioma) {
        this.idioma = idioma;
    }

    // Método para obtener el formato de la película
    public FormatoPelicula getFormato() {
        return formato;
    }

    // Método para establecer un nuevo formato a la película
    public void setFormato(FormatoPelicula formato) {
        this.formato = formato;
    }

    // Método que devuelve una representación en texto de la película
    @Override
    public String toString() {
        return "Pelicula { " +
                " nombre: '" + nombre + '\'' +
                ", director: '" + director + '\'' +
                ", duracion: " + duracion +
                ", genero: '" + genero + '\'' +
                ", idioma: '" + idioma + '\'' +
                ", formato: " + formato +
                '}'; // Muestra toda la información de la película
    }
}

 a 