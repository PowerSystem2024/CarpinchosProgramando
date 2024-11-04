package pasoPorValor;

public class PasoPorValor {
    
// Paso por valor es una copia que se toma de una informacion pero no modifica el original.
    
    public static void main(String[] args) {
        var valorX = 20;
        System.out.println("valorX = " + valorX);
        cambioValor(valorX); // Parámetro por valor
        System.out.println("valorX = " + valorX);
    }
    
    public static void cambioValor(int arg){
        System.out.println("arg = " + arg);
        arg = 15;
    }
        
}