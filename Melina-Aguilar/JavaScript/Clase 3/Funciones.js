// Funcion: es un codigo reutilizable que podremos llamar tantas veces como sea necesario
// se la puede llamar antes o despues de declararla, esto se llama 'hosting' automaticamente el programa lo pone antes.

miFuncion(8, 2); // Se lo conoce como 'hoisting'

// Declaramos una funcion
function miFuncion(a, b){       // Dentro de esos parentesis (a, b) puede o no tener parametros
    console.log("Sumamos: "+ (a + b));    // Cuerpo de la funcion
}

// Llamamos a la funcion
miFuncion(5, 4);