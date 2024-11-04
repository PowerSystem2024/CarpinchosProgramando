package Operaciones;

public class Aritmetica{
    // Atributos de la clase
    
    int a, b;
    
    // Metodos
    
    public void sumarNumeros(){
        int resultado = a+b;
        System.out.println("resultado = " + resultado);  // Enviar información a la consola NO es lo mismo que retornar un valor. 
    }   
    
    public int sumarConRetorno(){ //Retorna un valor entero
        int resultado = a + b;
        return resultado;
    }
    
    public int sumarConArgumentos(int arg1,  int arg2){
        this.a = arg1; // El argumento "a" se asigna el atributo this.a
        this.b = arg2; // El uso del this en este caso es opcional
        //return a + b;
        return sumarConRetorno();
    }
}