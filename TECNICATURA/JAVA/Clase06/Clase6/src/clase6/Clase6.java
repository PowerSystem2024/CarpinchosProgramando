
package clase6;
public class Clase6 {
    // Método MAIN
    public static void main(String[] args) {
        /*Alcance de variables
            - Las variables solo se pueden utilizar dentro del método que se definió.
            - Las variables se pueden llamar a través de otros métodos.
        */
        // Creación de variables locales (int o var)
        // var -> se puede utilizar para las variables locales
        var a = 10;
        var b = 7;
        
        // Llamado al método
        miMetodo();
        
        SobrecargaDeMetodos sobrecargaConstructor1 = new SobrecargaDeMetodos();
        sobrecargaConstructor1.a = 3;
        sobrecargaConstructor1.b = 7;
        
        System.out.println("sobrecargaConstructor1 a: " + sobrecargaConstructor1.a);
        System.out.println("sobrecargaConstructor1 b: " + sobrecargaConstructor1.b);
        
        System.out.println("");
        
        // var -> nunca se debe utilizar para los parámetros
        SobrecargaDeMetodos sobrecargaConstructor2 = new SobrecargaDeMetodos(5, 8);
        System.out.println("sobrecargaConstructor2 a: " + sobrecargaConstructor2.a);
        System.out.println("sobrecargaConstructor2 b: " + sobrecargaConstructor2.b);
    }
    
    // Creación de nuevo método
    public static void miMetodo(){
        // Creación de una variable
        // Saltará error ya que la variable no puede trascender del método main 
        // al nuevo método.
        // a = 10;
        
        // Para evitar este error, hay que llamar desde el main al método "miMetodo"
        System.out.println("Aquí hay otro método.");
    }
            
}
