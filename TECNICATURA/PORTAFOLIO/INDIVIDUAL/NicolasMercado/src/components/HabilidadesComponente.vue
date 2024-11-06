<script setup>
import espanol from '../components/icons/arg.svg';
import ingles from '../components/icons/eeuu.svg';
import git from '../components/icons/git.svg';
import html from '../components/icons/html-css.svg';
import java from '../components/icons/java.svg';
import js from '../components/icons/js.svg';
import mysql from '../components/icons/mysql.svg';
import node from '../components/icons/node.svg';
import python from '../components/icons/python.svg';
import vsc from '../components/icons/visual.svg';
import vue from '../components/icons/vue.svg';

// Se importa ref de vue para poder usarlo
import { ref } from 'vue';

// Se crea un array de objetos con las habilidades
const habilidades = ref([
    {
        id: 1, nombre: 'Lenguajes de Programación', habilidades: [
            { id: 1, nombre: 'JavaScript', nivel: 'Intermedio', icono: js },
            { id: 2, nombre: 'Python', nivel: 'Intermedio', icono: python },
            { id: 3, nombre: 'HTML', nivel: 'Intermedio', icono: html },
            { id: 4, nombre: 'Java', nivel: 'Intermedio', icono: java },
            { id: 5, nombre: 'SQL', nivel: 'Intermedio', icono: mysql }  // Aquí el icono estaba incorrecto (se usaba sql que no estaba importado)
        ]
    },
    {
        id: 2, nombre: 'Frameworks y Librerías', habilidades: [
            { id: 1, nombre: 'Vue.js', nivel: 'Intermedio', icono: vue },
            { id: 2, nombre: 'Node.js', nivel: 'Intermedio', icono: node }
        ]
    },
    {
        id: 3, nombre: 'Herramientas y Software', habilidades: [
            { id: 1, nombre: 'Git', nivel: 'Intermedio', icono: git },
            { id: 2, nombre: 'Visual Studio Code', nivel: 'Avanzado', icono: vsc }
        ]
    },
    {
        id: 4, nombre: 'Bases de Datos', habilidades: [
            { id: 1, nombre: 'MySQL', nivel: 'Intermedio', icono: mysql },
        ]
    },
    {
        id: 5, nombre: 'Idiomas', habilidades: [
            { id: 1, nombre: 'Español', nivel: 'Nativo', icono: espanol },
            { id: 2, nombre: 'Inglés', nivel: 'Intermedio', icono: ingles }
        ]
    }
]);
</script>

<template>
    <!-- Este componente Vue funciona de esta forma: -->
    <div class="skills-contenedor">
        <!-- Se recorre el array habilidades con v-for y se asigna la key habilidad.id -->
        <div v-for="categoria in habilidades" :key="categoria.id" class="skills-categoria">
            <!-- Se muestra el nombre de la habilidad -->
            <h3>{{ categoria.nombre }}</h3>
            <ul class="skills">
                <!-- Se recorre el array habilidades dentro de cada categoria -->
                <li v-for="habilidad in categoria.habilidades" :key="habilidad.id" class="skill">
                    <!-- Se muestra el icono de la habilidad y el nombre de la habilidad con su nivel -->
                    <img :src="habilidad.icono" :alt="habilidad.nombre">
                    <span>{{ habilidad.nombre }}: {{ habilidad.nivel }}</span>
                </li>
            </ul>
        </div>
    </div>
</template>

<style scoped>
.skills-contenedor {
    padding: 2rem;
    background: linear-gradient(-45deg, #021526, #03346E, #6EACDA, #a9bedf);
}

.skills-categoria {
    margin-bottom: 20px;
}

.skills-categoria h3 {
    display: flex;
    justify-content: left;
    margin-bottom: 10px;
    font-size: 1.5em;
    color: aliceblue;
    font-weight: bold;
}

.skills {
    display: flex;
    justify-content: space-evenly;
    flex-wrap: wrap;
    gap: 20px;
}

.skill {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    background-color: rgba(241, 245, 243, 0.856);
    padding: 0.3em;
    border-radius: 8px;
    box-shadow: 0px 4px 12px rgba(2, 151, 151, 0.963);
    flex: 1 1 200px;
    max-width: 250px;
}

.skill:hover {
    background-color: rgba(2, 151, 151, 0.963);
}

.skill img {
    width: 35px;
    height: 35px;
}

.skill span {
    font-size: 1em;
    color: #333;
}

.skill:hover {
    font-size: 1.3em;
    transition: 2s ease;
}

@media (max-width: 768px) {
    .skills-categoria h3 {
        justify-content: center;
    }

    .skill {
        justify-content: center;
    }
}
</style>
