<script setup>
import { ref } from 'vue';
// Importación de componentes (img)
import ProyectoUno from "/src/assets/Proyectos/proyecto1.jpg";
import ProyectoDos from "/src/assets/Proyectos/proyecto2.jpg";
import ProyectoTres from "/src/assets/Proyectos/proyecto3.jpg";

const proyectos = ref([
    { id: 1, nombre: "Yo Dibujo", descripcion: "Creé una página web en un curso de programación web (Yo Puedo Programar - Junior Achievement) con los lenguajes HTML, CSS y JavaScript.", imagenes: [ProyectoUno], github: "https://github.com/anaprg05/YoDibujo.git" },
    { id: 2, nombre: "PCB en Electrónica", descripcion: "Creé una página web para una equivalencia del Instituto Leonardo Murialdo con los lenguajes HTML, CSS y JavaScript.", imagenes: [ProyectoDos], github: "https://github.com/anaprg05/EquivalenciasElectro.git" },
    { id: 3, nombre: "Beneficios de la Robótica y la Electrónica", descripcion: "Creé una página web para una equivalencia del Instituto Leonardo Murialdo con los lenguajes HTML, CSS y JavaScript.", imagenes: [ProyectoTres], github: "https://github.com/anaprg05/EquivalenciasElectro.git" }
]);

</script>

<template>
    <div class="galeria">
        <div class="proyecto" v-for="proyecto in proyectos" :key="proyecto.id">
            <div class="proyectoInfo">
                <div class="imagenes">
                    <img  v-for="(img, index) in proyecto.imagenes" :key="index" :src="img" alt="Proyecto" class="proyectoImagen"/>
                </div>
                <h3>{{ proyecto.nombre }}</h3>
                <p>{{ proyecto.descripcion }}</p>
            </div>
            <div class="proyectoLinks">
                <a :href="proyecto.github" target="_blank">
                    <p class="mensaje">Link al proyecto en Github</p>
                </a>
            </div>
        </div>
    </div>
</template>

<style scoped>
.galeria {
    width: 100%;
    height: 100%;
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    padding: 20px;
    justify-content: center;
    background: linear-gradient(-45deg, #DDE5B6, #B9CA88, #9B8965, #6C584C);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
    border-radius: 5px;
}

@keyframes gradient {
0% {
    background-position: 0% 50%;
}
50% {
    background-position: 100% 50%;
}
100% {
    background-position: 0% 50%;
}
}

.proyecto {
    display: flex;
    flex-direction: column;
    border: 2px solid #C5D397;
    border-radius: 8px;
    overflow: hidden;
    background-color: #ADC178;
    max-width: 222px;
    flex: 1 1 300px;    
}

.proyectoImagen {
    width: 100%;
    height: auto;
    display: block;
    border-radius: 5px;
}

.proyectoInfo {
    padding: 15px;
    text-align: center;
}

.proyectoInfo h3 {
    font-weight: bold;
    margin: 10px 0;
    font-size: 1.3em;
    color: #5e4c41;
}

.proyectoInfo p {
    margin: 10px 0;
    font-size: 1em;
    color: #755948;
}

.proyectoLinks {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-top: 10px;
}

.proyectoLinks .githubLink {
    color: #8f6246;
    text-decoration: none;
    font-size: 0.9em;
}

.proyectoLinks .githubLink:hover {
    text-decoration: underline;
}

.imagenes {
    display: flex;
    flex-direction: column; /* Cambia la dirección de las imágenes */
    align-items: center; /* Alinea las imágenes al centro */
    gap: 10px; /* Espacio entre imágenes */
    justify-content: center;
}

.mensaje{
    font-weight: 600;
    display: flex;
    justify-content: space-around;
}

.mensaje:hover{
    text-decoration: underline;
}
</style>
