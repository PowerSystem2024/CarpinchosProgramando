package Caja;

public class Caja {
    //Atributos (caracteristicas)
    int ancho;
    int alto;
    int profundo;

    //Métodos y constructores (acciones)
    public Caja() { //Constructor 1 = vacío
    }

    //Constructor con parámetros
    public Caja(int ancho, int alto, int profundo) { //Constructor 2
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
    }

    public int calcularVolumen() {  //metodo para calcular
        return ancho * alto * profundo;
    }
}
