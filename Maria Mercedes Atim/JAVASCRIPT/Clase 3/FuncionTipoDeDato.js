//Function es un tipo de datos. Una funcion tambien puede ser un objeto con propiedades y metodos

function miFuncion(a, b){ // Esta funcion es del tipo funcion
    return a + b;
}

console.log("Tipo de dato de la funcion: "+ typeof miFuncion);

function miFuncion2(a, b){
    console.log("\n",arguments); // Este metodo nos muestra los argumentos. Lo asocia como un arreglo.
    console.log("La funcion tiene " + arguments.length + " argumentos."); // Aqui se muestra la cantidad de argumentos.
}

miFuncion2(5, 7, 3, 6);

// To String
let miFuncionTexto = miFuncion2.toString();
console.log("\nConversion de la funcion a texto:" + miFuncionTexto);