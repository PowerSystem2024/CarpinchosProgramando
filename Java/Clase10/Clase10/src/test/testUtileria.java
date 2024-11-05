package test;
//import ar.com.codesystem.*;
// si usamos el asterisco estamos importando todas las clases que estan dentro del paquete
import ar.com.codesystem.Utileria;

//import static ar.com.codesystem.Utileria.imprimir;//Solo aplica para métodos estáticos

public class testUtileria {

    public static void main(String[] args) {
        Utileria.imprimir("Saludos a todos los alumnos de la tecnicatura");
        //imprimir("Terminamos en unos minutos");
        // ar.com.codesystem.Utileria.imprimir("Ahora si estamos terminando");//No es lo mas recomendado
    }
}
