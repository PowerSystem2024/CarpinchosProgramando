
package pasoPorValor;

/* Paso por Valor
    El paso por valor es una copia de los valores que reciben la variable 
    original.
*/

public class PasoPorValor {
    // Método Main
    public static void main(String[] args) {
        var valorX = 20;
        System.out.println("valorX = " + valorX);
        System.out.println("valorX = " + valorX);
        
        /* 
        Llamado al Método cambioValor y enviado de una copia (valorX)
         Es decir, está copiando el valor que recibe la variable local.
         */
        cambioValor(valorX);
    }
    
    // Método Nuevo
    // Muestra el valor copiado del Método Main
    public static void cambioValor(int arg1){
        System.out.println("arg1 = " + arg1);
        arg1 = 15;
    }
}
