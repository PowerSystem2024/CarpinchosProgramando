<script setup>
import { ref } from 'vue';
import FondoLava from './FondoLava.vue';
//Este es un arreglo con ref para que se pueda reactivar el cambio de los intereses
const intereses = ref([
    'Exploración en Programación: Estoy comenzando en el mundo de la programación y aprendiendo varios lenguajes. Aunque soy nuevo en esta área, disfruto mucho cada paso del aprendizaje y me motiva la idea de mejorar continuamente.',
    'Creatividad e Innovación: Soy una persona curiosa y meticulosa, con experiencia como matricero industrial, lo que me ha enseñado a prestar atención al detalle. Me apasiona investigar sobre nuevas tecnologías y disfruto aplicando mi creatividad a cada proyecto en el que trabajo.'
]);
</script>

<template>
    <div class="intereses-contenedor">
        <FondoLava />
        <ul class="contenedor-lista">
            <li class="item" v-for="interes in intereses" :key="interes">
                {{ interes }}
            </li>
        </ul>
    </div>
</template>

<style scoped>
.intereses-contenedor {
    display: flex;
    position: relative;
    margin: 0 auto;
    max-width: 100%;
    padding: 1rem;
}

.contenedor-lista {
    list-style-type: none;
    padding: 1rem;
    margin: 0;
    width: 100%;
    height: 100%;
}

.item {
    margin-bottom: 1rem;
    padding: 1rem; /* Añade espacio alrededor del texto */
    background-color: rgba(9, 9, 9, 0.5); /* Fondo negro semitransparente */
    border-radius: 8px; /* Bordes redondeados */
    color: white; /* Color del texto */
    font-size: 25px; /* Tamaño de fuente */
    text-shadow: 3px 3px 6px rgb(88, 201, 232); /* Sombra del texto */
}
</style>