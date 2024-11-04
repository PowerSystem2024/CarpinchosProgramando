package capybarafilms;

public class CreadorDePeliculas {

    public static void main(String[] args) {

        Pelicula peli1, peli2;
        peli1 = new Pelicula("Titanic", "James Cameron", 1500, 250, "Romantica", "Español", "3D");
        peli2 = new Pelicula("Orgullo y Prejuicio", "Ang Lee", 2000, 150, "Romantica", "Español", "2D");

        System.out.println(peli1);
        System.out.println(peli2);

    }

}
