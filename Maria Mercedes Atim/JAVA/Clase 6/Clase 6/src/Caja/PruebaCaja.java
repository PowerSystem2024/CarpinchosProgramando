package caja;

public class PruebaCaja{
    
    public static void main(String[] args) {
        
        //Variables Locales
        double ancho = 3.0;
        double alto = 2.0;
        double profundo = 6.0;
        
        Caja caja1 = new Caja(); // Instancia del objeto con constructor vacío.
        caja1.ancho = ancho; // Le pasamos valores al objeto
        caja1.alto = alto;
        caja1.profundidad = profundo;
        double resultado = caja1.calcularVolumen(); // Llamamos al metodo.
        System.out.println("Calculamos sin parámetros. "
                + "El resultado del volumen de la caja es: " + resultado);
         
        
        Caja miCaja = new Caja();
        miCaja.calcularVolumen(2.0, 4.0, 6.0);
        
    }    
}