package clase5;

import javax.swing.JOptionPane;

public class FechaCorrectaJOptionPane {

    public static void main(String[] args) {
        int dia = Integer.parseInt(JOptionPane.showInputDialog("Introduce el día:"));
        int mes = Integer.parseInt(JOptionPane.showInputDialog("Introduce el mes:"));
        int año = Integer.parseInt(JOptionPane.showInputDialog("Introduce el año:"));

        if ((dia != 0) && (dia <= 30)) {
            if ((mes != 0) && (mes <= 12)) {
                if ((año != 0) && (año <= 2024)) {
                    JOptionPane.showConfirmDialog(null, "La fecha ingresada es correcta: " + dia + "/" + mes + "/" + año);
                } else {
                    JOptionPane.showConfirmDialog(null, "Fecha incorrecta, año incorrecto.");
                }
            } else {
                JOptionPane.showConfirmDialog(null, "Fecha incorrecta, mes incorrecto.");
            }
        } else {
            JOptionPane.showConfirmDialog(null, "Fecha incorrecta, dia incorrecto.");
        }
    }
}