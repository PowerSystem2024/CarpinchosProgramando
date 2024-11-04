package test; 
import domain.Persona; // Importa la clase Persona del paquete domain

public class TestArreglosObject { 

    public static void main(String[] args) { 
        Persona personas[] = new Persona[2]; // Crea un arreglo para almacenar 2 objetos Persona
        personas[0] = new Persona("Ana Paula"); // Inicializa el primer objeto Persona
        personas[1] = new Persona("Melina"); // Inicializa el segundo objeto Persona

        // Muestra la referencia de memoria del primer objeto Persona
        System.out.println("personas 0 = " + personas[0]); // Muestra información del objeto en la posición 0
        System.out.println("personas 1 = " + personas[1]); // Muestra información del objeto en la posición 1
        
        // Recorre el arreglo personas y muestra cada objeto
        for(int i = 0; i < personas.length; i++){ // Itera sobre cada posición del arreglo
            System.out.println("En el arreglo personas en la posicion: "+ i +" está: "+ personas[i]);
        }
        
        System.out.println(""); 
        
        // Crea un arreglo de frutas con 3 elementos
        String frutas[] = {"Banana", "Pera", "Durazno"}; // Arreglo de cadenas de texto
        
        // Recorre el arreglo frutas y muestra cada fruta
        for (int i = 0; i < frutas.length; i++) { // Itera sobre cada posición del arreglo
            System.out.println("En el arreglo frutas, en la posicion: "+i+" está la fruta: "+frutas[i]);
        }
    }
}