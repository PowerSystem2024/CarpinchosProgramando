// Bucle while
let contador = 0;
while (contador < 3) {
    console.log(contador); // 0, 1, 2
    contador++;
}
console.log("Fin del ciclo while"); // Fin del ciclo while

// Bucle do-while
let conteo = 0;
do {
    console.log(conteo); // 0, 1, 2
    conteo++;
} while (conteo < 3);
console.log("Fin del ciclo do-while"); // Fin del ciclo do-while

// Bucle for
for (let contando = 0; contando < 3; contando++) {
    console.log(contando); // 0, 1, 2
}
console.log("Fin del ciclo for"); // Fin del ciclo for

// Bucle for para imprimir números pares
for (let contando = 0; contando <= 10; contando++) {
    if (contando % 2 == 0) {
        console.log(contando); // 0, 2, 4, 6, 8, 10
    }
}
console.log("Termina el ciclo al encontrar el primer número par"); // Termina el ciclo al encontrar el primer número par

// Bucle for para saltar números impares
for (let contando = 0; contando <= 10; contando++) {
    if (contando % 2 !== 0) {
        continue;
    }
    console.log(contando); // 0, 2, 4, 6, 8, 10
}
console.log("Termina el ciclo"); // Termina el ciclo
