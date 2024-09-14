package capybarafilms;

public class Butaca {
    int numero;
    char fila;
    String categoria;
    boolean estado;

    public Butaca(int numero, char fila, String categoria, boolean estado) {
        this.numero = numero;
        this.fila = fila;
        this.categoria = categoria;
        this.estado = estado;
    }

    public int getNumero() {
        return numero;
    }

    public char getFila() {
        return fila;
    }

    public String getCategoria() {
        return categoria;
    }

    public boolean isEstado() {
        return estado;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public void setFila(char fila) {
        this.fila = fila;
    }

    public void setCategoria(String categoria) {
        this.categoria = categoria;
    }

    public void setEstado(boolean estado) {
        this.estado = estado;
    }

    @Override
    public String toString() {
        return "Butaca{" + "numero=" + numero + ", fila=" + fila + ", categoria=" + categoria + ", estado=" + estado + '}';
    }
    
    
    
}
