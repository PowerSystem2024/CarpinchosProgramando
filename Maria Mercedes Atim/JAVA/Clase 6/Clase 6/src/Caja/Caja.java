package caja;

public class Caja{
    public double ancho;
    public double alto;
    public double profundidad;

    public Caja() {
    }
    
    public Caja(double ancho, double alto, double profundidad) {
        this.ancho = ancho;
        this.alto = alto;
        this.profundidad = profundidad;
    }

    public double calcularVolumen(double ancho, double alto, double profundidad){
        double volumen;
        volumen = ancho * alto * profundidad;
        System.out.println("Calculamos con parámetros. "
                + "El volumen de la caja es: " + volumen + " cm3.");
        return volumen;
    }
    
    public double calcularVolumen(){
        return ancho * alto * profundidad;
    }
}