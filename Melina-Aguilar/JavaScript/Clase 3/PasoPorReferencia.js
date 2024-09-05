/* Paso por referencia: a la funcion le pasamos la referencia hexadecimal de el espacio de
 memoria donde estaba alojado el objeto. Cuando creamos el objeto se creo un espacio de memoria
 y al pasarle ese objeto en el llamado de la funcion (como un parametro) le estamos pasando
 directamente esa valor hexadecimal de la memoria y de esta forma dentro de la funcion a traves
 de la variable 'persona1' hemos modificado esos valores y luego esa variable se destruya al
 finalizar la funcion pero la modificiacion quedo grabada dentro del objeto 'persona'.
 */

// Definimos un objeto
const persona = {
    nombre: 'Juan',
    apellido: 'Lopez'
}

console.log(persona);

function cambiarValorObjeto(persona1){
    persona1.nombre = 'Ignacio';
    persona1.apellido = 'Perez';
}

cambiarValorObjeto(persona); // La variable 'persona1' al finalizar la funcion se destruye
                             // pero las modificaciones afectaran permanentemente al objeto 'persona'.
console.log(persona);