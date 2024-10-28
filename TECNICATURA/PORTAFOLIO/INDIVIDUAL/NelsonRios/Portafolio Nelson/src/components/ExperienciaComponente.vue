<script setup>
import icono1 from '../assets/grupo.png';
import icono2 from '../assets/web.png';

import { ref } from 'vue';
const titulo = 'Desarrollador Full Stack';
const fecha = 'Desde Enero 2022 / Octubre 2024';
const experiencias = ref([
    { id: 1, src: icono1, parrafo: 'Forme parte de proyectos grupales en los cursos de formación de programación, incursionando en diferentes bibliotecas, frameworks y tecnologías de desarrollo web.' },
    { id: 2, src: icono2, parrafo: 'Desarrollé aplicaciones web utilizando Node.js, Vue.js, HTML, CSS. Formando parte del diseño, la ejecución y el testeo.' },
]);
</script>

<template>
    <div class="card">
        <h3 class="titulo">{{ titulo.toLocaleUpperCase() }}</h3>
        <p class="fecha">{{ fecha }}</p>
        <ul class="listado">
            <li class="item" v-for="experencia in experiencias" :key="experencia.id">
                <img class="imagen-svg" :src="experencia.src" :alt="experencia.parrafo">
                <p>{{ experencia.parrafo }}</p>
            </li>
        </ul>
    </div>
</template>

<style scoped>
.card {
    display: flex;
    flex-direction: column;
    padding: 2rem;
    background-color: rgb(28, 41, 52);
    border-radius: 15px;
}

.imagen-svg{
    width: 80px;
    height: auto;
    margin-right: 1rem;
}

.titulo {
    font-size: 1.5rem;
    color: coral;
}

.fecha {
    font-size: 1rem;
    color: burlywood;
    margin-bottom: 1rem;
}

.listado {
    display: flex;
    flex-direction: column;
}

.item {
    align-items: center;
    display: flex;
    padding: 1rem;
    gap: 1.5rem;
    font-size: 20px;
    color: aliceblue;
}
</style>