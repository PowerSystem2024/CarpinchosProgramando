package Ciclos09;

import javax.swing.JOptionPane;

public class EjercicioCiclos09 {
    public static void main(String[] args) {
        String diaStr = JOptionPane.showInputDialog("Digite el día:");
        int dia = Integer.parseInt(diaStr);

        String mesStr = JOptionPane.showInputDialog("Digite el mes:");
        int mes = Integer.parseInt(mesStr);

        String anioStr = JOptionPane.showInputDialog("Digite el año:");
        int anio = Integer.parseInt(anioStr);

        if ((dia > 0) && (dia <= 30)) {
            if ((mes > 0) && (mes <= 12)) {
                if ((anio > 0) && (anio <= 2022)) {
                    JOptionPane.showMessageDialog(null, "La fecha ingresada es: " + dia + "/" + mes + "/" + anio);
                } else {
                    JOptionPane.showMessageDialog(null, "Fecha incorrecta, año incorrecto");
                }
            } else {
                JOptionPane.showMessageDialog(null, "Fecha incorrecta, mes incorrecto");
            }
        } else {
            JOptionPane.showMessageDialog(null, "Fecha incorrecta, día incorrecto");
        }
    }
}
