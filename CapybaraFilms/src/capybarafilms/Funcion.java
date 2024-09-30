package capybarafilms;

public class Funcion {

    public static void main(String[] args) {
        Pelicula peli1, peli2;
        peli1 = new Pelicula("Titanic", "James Cameron", 1500, 250, "Romantica", "Español", "3D");
        peli2 = new Pelicula("Orgullo y Prejuicio", "Ang Lee", 2000, 150, "Romantica", "Español", "2D");

        System.out.println(peli1);
        System.out.println(peli2);

        Cliente cliente1, cliente2, cliente3;
        cliente1 = new Cliente("Fernando", "Simich", "40665434", "fersimich@gmail.com");
        cliente2 = new Cliente("Rosa", "Martinez", "30456435", "rosamartinez@gmail.com");
        cliente3= new Cliente ("Lautaro", "Martinez", "4564434", "lautimartinez@gmail.com");


        System.out.println(cliente1.getNombre());
        System.out.println(cliente2.toString());
        System.out.println(cliente2.getApellido());

    }
}