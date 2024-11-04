package domain; 

public class Persona { 
    public String nombre; // Atributo que almacena el nombre de la persona

    // Constructor que inicializa el nombre
    public Persona(String nombre) { 
        this.nombre = nombre; // Asigna el nombre al atributo de la clase
    }

    // Método para obtener el nombre
    public String getNombre() { 
        return nombre; // Retorna el nombre de la persona
    }

    // Método para settear un nuevo nombre
    public void setNombre(String nombre) { 
        this.nombre = nombre; // Actualiza el nombre de la persona
    }

    // Método para representar la persona como una cadena de texto
    @Override
    public String toString() { 
        StringBuilder sb = new StringBuilder(); // Crea un objeto StringBuilder para construir la cadena
        sb.append("Persona {"); // Agrega el inicio de la representación
        sb.append("nombre = ").append(nombre); // Agrega el nombre a la representación
        sb.append(", direccion en memoria = ").append(super.toString()); // Agrega la dirección de memoria del objeto
        sb.append('}'); // Cierra la representación
        return sb.toString(); // Retorna la representación como cadena de texto
    }    
}