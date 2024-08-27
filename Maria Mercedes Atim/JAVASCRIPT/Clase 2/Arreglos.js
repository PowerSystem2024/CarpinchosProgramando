// Un arreglo puede contener varios tipos de datos. Y se declaran de multiples formas:
//let autos = new Array("Ferrari", "Renault", "BMW"); //Sintaxis antigua

const autos = ["Ferrari", "Renault", "BMW"]; //Defnir los elementos del arreglo
console.log(autos);

//Recorremos los elementos del arreglo:
console.log(autos[0]); //Indicamos el indice del elemento que queremos ver.
console.log(autos[2]);

console.log("---- Recorremos el arreglo con for: ----");
for(let i = 0; i < autos.length; i++){
    console.log("En la posicion " + i +" esta: "+autos[i]);
}

//Modificamos los elementos del arreglo
console.log("---- Modificamos elementos del arreglo: ----");
autos[1] = "Volvo";
console.log(autos[1]);

//Agregamos nuevos valores al arreglo
console.log("---- Agregamos nuevos elementos al arreglo (Forma 1): ----");
autos.push("Audi"); //Se agrega el elemento al final del arreglo
console.log(autos);

//Otras formas de agregar elementos al arreglo.
console.log("---- Agregamos nuevos elementos al arreglo (Forma 2): ----");
autos[autos.length] = "Porche";
console.log(autos);

//Agregar elementos (Tener mucho cuidado)
console.log("---- Agregamos nuevos elementos al arreglo (Forma 3): ----");
autos[6] = "Renault"; //Llena el espacio de memoria aunque saltee varias posiciones.
console.log(autos);

//Verificar si estamos trabajando con un arreglo
console.log("---- Verificamos si es un arreglo: ----");
console.log(Array.isArray(autos)); //Devuelve un booleano

console.log("---- Verificamos si es un arreglo con Instance of ----");
console.log(autos instanceof Array); //Si es instancia de la clase Array