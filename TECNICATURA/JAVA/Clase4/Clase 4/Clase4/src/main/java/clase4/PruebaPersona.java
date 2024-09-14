package clase4;

public class PruebaPersona{
    
    public static void main(String[] args) {
        
     Persona persona1; // Se declara una variable del tipo Persona
     persona1 = new Persona(); // Se instancia un objeto de tipo Persona
     persona1.nombre = "Mercedes"; // Se asigna a cada atributo los datos del objeto. Con la notacion de punto seleccionamos el atributo a modificar.
     persona1.apellido = "Atim";
     persona1.obtenerInformacion(); // Invocamos al metodo del objeto Persona que recibe los valores y los imprime.
     
     Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2);     
        System.out.println("persona1 = " + persona1);
        persona2.obtenerInformacion(); // Si no se asigna valor, mostrará null. Cada objeto tiene su propia información.
        persona2.nombre = "Nelson";
        persona2.apellido = "Rios";
        persona2.obtenerInformacion();
    }
}