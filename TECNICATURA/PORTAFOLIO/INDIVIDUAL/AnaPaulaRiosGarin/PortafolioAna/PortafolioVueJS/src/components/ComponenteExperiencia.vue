<script setup>
import { ref } from 'vue';

// Importación de componentes (img)
// experiencias
import Programacion from '/src/assets/Experiencia/programacion.svg';
import Web from '/src/assets/Experiencia/web.svg';
import Tick from '/src/assets/Experiencia/tick.svg';
// experiencias2
import Ilustracion from '/src/assets/Experiencia/ilustracion.svg';
import Dibujo from '/src/assets/Experiencia/dibujo.svg';
import Color from '/src/assets/Experiencia/color.svg';

const titulo = 'Enfocada en adquirir experiencia práctica';
const descripcion = 'Me encuentro en búsqueda de nuevos desafíos, siempre dispuesta a aprender nuevas tecnologías y trabajar en equipo para lograr un producto de buena calidad';
const subtitulo = 'Proyectos Personales en Programación';

const experiencias = ref([
    { id: 1, src: Programacion, parrafo: 'Durante mi trayecto como programadora he participado de varios proyectos y pasantías los cuales me permitieron aumentar y profesionalizar mis conocimientos.' },
    { id: 2, src: Web, parrafo: 'En todos los proyectos que participé, implementé varias de las tecnologías que se utilizan actualmente como HTML, CSS, JavaScript, Bootstrap, NodeJS y VueJS, desarrollando habilidades en desarrollo web.' },
    { id:3, src: Tick, parrafo: 'Esto me ha permitido adquirir experiencia práctica, y mejorar mis habilidades en resolución de problemas, depuración y lógica de programación.' }
]);

const subtitulo2 = 'Proyectos Personales en Ilustración';
const experiencias2 = ref([
    { id: 1, src: Ilustracion, parrafo: 'Durante mi trayecto dentro del área de ilustración, he desarrollado proyectos personales para fortalecer mis habilidades y conocimientos en esta área. ' },
    { id: 2, src: Dibujo, parrafo: 'He trabajado en ilustraciones tanto tradicionales como digitales, diseño de personajes y diseño de escenarios, utilizando herramientas como Clip Paint Studio y Adobe Photoshop' },
    { id:3, src: Color, parrafo: 'Estos proyectos me han permitido mejorar en técnicas de composición, manejo de color y estilo personal, así como en mi habilidad para comunicar ideas visualmente de manera creativa y profesional.' }
]);

</script> 

<template>
    <div class="card">
        <h3 class="titulo">{{ titulo.toLocaleUpperCase() }}</h3>
        <p class="descripcion">{{ descripcion }}</p>
        <p class="subtitulo">{{ subtitulo }}</p>
        <ul class="listado">
            <li class="item" v-for="experencia in experiencias" :key="experencia.id">
                <img class="imagenSvg" :src="experencia.src" width="45rem" :alt="experencia.parrafo">
                <p>{{ experencia.parrafo }}</p>
            </li>
        </ul>
        <p class="subtitulo">{{ subtitulo2 }}</p>
        <ul class="listado">
            <li class="item" v-for="experencia in experiencias2" :key="experencia.id">
                <img class="imagenSvg" :src="experencia.src" width="45rem" :alt="experencia.parrafo">
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
    background-color: #8B6E5A;
    border-radius: 15px;
}

.titulo {
    font-size: 1.5rem;
    color: #b6cf6f;
    font-weight: 600;
}

.descripcion {
    font-size: 1.1rem;
    color: #B9CA88;
}

.subtitulo {
    font-size: 1rem;
    color: #a8b385;
    margin-bottom: 1rem;
    font-weight: 500;
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
}

.imagenSvg {
    height: 30px;
    width: 30px;
}

p {
    color: #E7E8C4;
}
</style>
