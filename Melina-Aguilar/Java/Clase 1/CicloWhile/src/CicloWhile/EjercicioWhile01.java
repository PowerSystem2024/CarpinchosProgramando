package CicloWhile;

public class EjercicioWhile01 {
   
    public static void main(String[] args){
  
//              --- Ciclo While ---

        var conteo = 0;     // Inferencia de tipos
        while(conteo < 3){
            System.out.println("conteo = " + conteo);
            conteo++;     // Vamos aumentando en uno la variable
        }
  
        
 //             --- Ciclo Do While ---
 
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        }while(contador < 3);
        
        
  //               --- Ciclo For ---
  
  
        // Break
        
    // Uso de las palabras 'Break' y 'Continue' junto a las etiquetas (Labels)    
      
    inicio: 
  // for(declarar variable de tipo contador;  condicion; incremento o decremento)
         for(var contando = 0; contando < 7; contando++){
            if(contando % 2 == 0){
                System.out.println("contando = " + contando);
                break inicio ; // apenas encuentra el primer numero en condicion se rompe 
                       // el ciclo y solo muestre ese.
            }
        }
        
        // Continue
        inicio:
         for(var contando = 0; contando < 7; contando++){
            if(contando % 2 != 0){
              continue inicio; // vamos a la siguiente iteracion
            }
            System.out.println("contando = " + contando);
        }   
    }        
}
