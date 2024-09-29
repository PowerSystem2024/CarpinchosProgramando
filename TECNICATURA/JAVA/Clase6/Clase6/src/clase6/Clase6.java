
package clase6;
public class Clase6 {

    public static void main(String[] args) {
        SobrecargaDeMetodos sobrecargaConstructor1 = new SobrecargaDeMetodos();
        sobrecargaConstructor1.a = 3;
        sobrecargaConstructor1.b = 7;
        
        System.out.println("sobrecargaConstructor1 a: " + sobrecargaConstructor1.a);
        System.out.println("sobrecargaConstructor1 b: " + sobrecargaConstructor1.b);
        
        System.out.println("");
        
        SobrecargaDeMetodos sobrecargaConstructor2 = new SobrecargaDeMetodos(5, 8);
        System.out.println("sobrecargaConstructor2 a: " + sobrecargaConstructor2.a);
        System.out.println("sobrecargaConstructor2 b: " + sobrecargaConstructor2.b);
    }
    
}
