// Para pasar por Referencia necesitamos crear un objeto.

const persona = {
    nombre: "Juan",
    apellido: "Lepez"
}
console.log("La primera instancia de persona es: ", persona);

function cambiarValorObjeto(p1){ //Paso por Referencia, la variable p1 apunta al objeto
p1.nombre = "Ignacio";
p1.apellido = "Perez";
}

cambiarValorObjeto(persona);
console.log("\nDespues de la modificación con la función, persona es: ", persona);