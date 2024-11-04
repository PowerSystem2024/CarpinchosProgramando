
package pasoPorReferencia;

// Se importa la clase Persona desde el paquete Clases
// import paquete.clase;
import Clases.Persona;

/* Paso Por Referencia
    Es el acceso del uso de una clase. En este caso, la clase Persona.
*/

public class PasoPorReferencia {
    // Método Main
    public static void main(String[] args) {
        // Llamado al constructor de la clase Persona a través del objeto
        Persona persona1 = new Persona();
        
        // Si los atributos no fueran públicos, saltaría un error en esta línea.
        // Es decir, no se podría acceder a los atributos.
        persona1.nombre = "Ana";
        System.out.println("persona nombre = " + persona1.nombre);
        
        // Llamado del método
        cambiarValor(persona1);
        
        // Imprime la memoria heap
        System.out.println("El cambio que se realizó en el nombre es: " + persona1);
        // Muestra directamente el cambio de nombre
        System.out.println("El cambio que se realizó en el nombre es: " + persona1.nombre);
        
        persona1 = cambiarElValor(persona1);
        
        // Esto mostrará que es inválido.
        // Persona persona2 = null;
        
        Persona persona2 = new Persona();
        persona2 = cambiarElValor(persona2);
        System.out.println("El nuevo valor del objeto es = " + persona2.nombre);
    }
    
    // Creación de un nuevo método
    // Para acceder al objeto y a la clase, hay que utilizar los parámetros.
    // En este caso, los parámetros son Persona (Clase)
    public static void cambiarValor(Persona persona){
        persona.nombre = "Mercedes";
    }
    
    // PALABRAS RETURN Y NULL
    // Creación de un nuevo método tipo object
    public static Persona cambiarElValor(Persona persona){
        // Null -> Vacío, carece de valor
        if(persona == null){
            System.out.println("El valor de persona es inválido: NULL");
            return null;
        }
        else{
            persona.nombre = "Nelson";
            // Si el return se coloca antes, anulará todo el código que continua. 
            // Es decir, no se ejecutarán las siguientes líneas.
            return persona; 
        }  
    }
}
