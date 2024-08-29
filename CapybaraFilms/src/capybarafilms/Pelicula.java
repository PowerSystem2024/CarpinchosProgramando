package capybarafilms;

public class Pelicula {

    public String nombre;
    public String director;
    public int precio;
    public int duracion;
    public String categoria;
    public String idioma;
    public String formato;

    public Pelicula(String nombre, String director, int precio, int duracion, String categoria, String idioma, String formato) {
        this.nombre = nombre;
        this.director = director;
        this.precio = precio;
        this.duracion = duracion;
        this.categoria = categoria;
        this.idioma = idioma;
        this.formato = formato;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getDirector() {
        return director;
    }

    public void setDirector(String director) {
        this.director = director;
    }

    public int getPrecio() {
        return precio;
    }

    public void setPrecio(int precio) {
        this.precio = precio;
    }

    public int getDuracion() {
        return duracion;
    }

    public void setDuracion(int duracion) {
        this.duracion = duracion;
    }

    public String getCategoria() {
        return categoria;
    }

    public void setCategoria(String categoria) {
        this.categoria = categoria;
    }

    public String getIdioma() {
        return idioma;
    }

    public void setIdioma(String idioma) {
        this.idioma = idioma;
    }

    public String getFormato() {
        return formato;
    }

    public void setFormato(String formato) {
        this.formato = formato;
    }
  
    @Override
    public String toString() {
        return "Pelicula:\n" + "nombre: " + nombre + ", director: " + director + ", precio: " + precio + ", duracion: " + duracion + ", categoria: " + categoria + ", idioma: " + idioma + ", formato: " + formato;
    }
}