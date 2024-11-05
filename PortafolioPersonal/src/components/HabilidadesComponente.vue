<script setup>

import Javascript from  '/src/components/icons/icons/javascript.svg';
import Python from '/src/components/icons/icons/python.svg';
import Java from '/src/components/icons/icons/java.svg';
import CSS from "/src/components/icons/icons/css.svg";
import HTML from '/src/components/icons/icons/html-css.svg';
import SQL from  '/src/components/icons/icons/sql.svg';
import Reactjs from '/src/components/icons/icons/react.svg';
import Vuejs from '/src/components/icons/icons/vue.svg';
import Nodejs from '/src/components/icons/icons/node.svg';
import  Django from '/src/components/icons/icons/django.svg' ;
import Bootstrap from '/src/components/icons/icons/bootstrap.svg' ;
import Git from '/src/components/icons/icons/git.svg';
import Docker from '/src/components/icons/icons/docker.svg';
import Cypress from '/src/components/icons/icons/cypress.svg';
import Figma from '/src/components/icons/icons/figma.svg';
import VisualStudioCode from '/src/components/icons/icons/visual.svg';
import MongoDB from '/src/components/icons/icons/mongo.svg';
import MySQL from '/src/components/icons/icons/mysql.svg';
import PostgreSQL from '/src/components/icons/icons/postgres.svg';
import Español from '/src/components/icons/icons/arg.svg';
import Ingles from '/src/components/icons/icons/eeuu.svg';


import { ref } from 'vue';


const habilidades = ref([
    {
        id: 1,
        nombre: 'Lenguajes de Programación',
        habilidades: [
        // Se crea un objeto con id, nombre, nivel e ícono
        { id: 1, nombre: 'JavaScript', nivel: 'Intermedio', icono: Javascript },
        { id: 2, nombre: 'Python', nivel: 'Intermedio', icono: Python },
        { id: 3, nombre: 'HTML', nivel: 'Avanzado', icono: HTML },
        { id: 4, nombre: 'CSS', nivel: 'Avanzado', icono: CSS },
        { id: 5, nombre: 'Java', nivel: 'Intermedio', icono: Java },
        { id: 6, nombre: 'SQL', nivel: 'Intermedio', icono: SQL }
        ]
    },
    {
        id: 2,
        nombre: 'Frameworks y Librerías',
        habilidades: [
        { id: 1, nombre: 'Reactjs', nivel: 'Avanzado', icono: Reactjs },
        { id: 2, nombre: 'Vuejs', nivel: 'Intermedio', icono: Vuejs},
        { id: 3, nombre: 'Nodejs', nivel: 'Avanzado', icono: Nodejs },
        { id: 4, nombre: 'Django', nivel: 'Intermedio', icono: Django},
        { id: 5, nombre: 'Bootstrap', nivel: 'Avanzado', icono: Bootstrap}
        ]
    } ,
    {
        id: 3,
        nombre: 'Herramientas y Software',
        habilidades: [
        // Se crea un objeto con id, nombre, nivel e ícono
        { id: 1, nombre: 'Git', nivel: 'Avanzado', icono: Git},
        { id: 2, nombre: 'Docker', nivel: 'Basico', icono: Docker},
        { id: 3, nombre: 'Cypress', nivel: 'Basico', icono: Cypress },
        { id: 4, nombre: 'Figma', nivel: 'Intermedio', icono: Figma},
        { id: 5, nombre: 'Visual Studio Code', nivel: 'Intermedio', icono: VisualStudioCode}
        ]
    },
    {
        id: 4,
        nombre: 'Base de Datos',
        habilidades: [
        { id: 1, nombre: 'MongoDB', nivel: 'Avanzado', icono: MongoDB },
        { id: 2, nombre: 'MySQL', nivel: 'Intermedio', icono: MySQL },
        { id: 3, nombre: 'PostgreSQL', nivel: 'Avanzado', icono: PostgreSQL}        
        ]
    },
    {
        id: 5,
        nombre: 'Idiomas',
        habilidades: [
        // Se crea un objeto con id, nombre, nivel e ícono
        { id: 1, nombre: 'Español', nivel: 'Nativo', icono: Español },
        { id: 2, nombre: 'Ingles', nivel: 'Intermedio', icono: Ingles }
        ]
    }
]);
</script>

<template>
    <!-- Este componente vue funciona de esta forma: -->
    <div class="skills-contenedor">
    <!-- Se recorre el array habilidades con v-for y se asigna la key habilidad.id -->
        <div v-for="habilidad in habilidades" :key="habilidad.id" class="skills-categoria">
            <!-- Se muestra el nombre de la habilidad -->
            <h3>{{ habilidad.nombre }}</h3>
            <ul class="skills">
            <!-- Se recorre el array habilidades con v-for y se asigna la key habilidad.id -->
            <li v-for="habilidad in habilidad.habilidades" :key="habilidad.id" class="skill">
                <!-- Se muestra el ícono de la habilidad y el nombre de la habilidad con su nivel -->
                <img :src="habilidad.icono" :alt="habilidad.nombre">
                <!-- Se muestra el ícono de la habilidad y el nombre de la habilidad con su nivel -->
                <span>{{ habilidad.nombre }}: {{ habilidad.nivel }}</span>
            </li>
            </ul>
        </div>
    </div>


    
</template>

<style scoped>

h3 {
font-size: 25px; 
color: gray;

}
.skills-contenedor {
    padding: 2rem;
}

.skills-categoria {
    margin-bottom: 20px;
}

/*.skills-categoria h3 {
    display: flex;
    justify-content: left;
    margin-bottom: 10px;
    font-size: 1rem;
   color:  rgba(60, 60, 60, 0.66);
   
    font-weight: bold;
}
*/
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
    gap: 8px;
    background-color: #bdd6d2;
    padding: 0.3em;
    border-radius: 8px;
    box-shadow: #a5c8ca;
    flex: 1 1 159px;
    max-width: 240px;
    font-size: 20px;
}



.skill img {
    width: 35px;
    height: 35px;
}

.skill span {
    font-size: 1em;
    color: grey;
}

.skill:hover {
    font-size: 23px;
    transition: 1s ease;
    background-color: #e3f8f9;

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