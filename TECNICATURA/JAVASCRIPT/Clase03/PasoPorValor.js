// Paso por valor es cuando usamos tipos que no son objetos (tipos numericos, booleanos, etc)
// Tipos primitivos: No se puede aociar ni propiedades ni métodos a éste valor.
// PASO POR VALOR <- NO AFECTA EL ORIGINAL DE LA COPIA
// PASO POR REFERENCIA <- AFECTA DIRECTAMENTE EL ORIGINAL

let k = 10;
function cambiarValor(a){ // Paso por valor
    a = 20;
}

cambiarValor(k);
console.log(k); // La funcion no afecta a la variable global K