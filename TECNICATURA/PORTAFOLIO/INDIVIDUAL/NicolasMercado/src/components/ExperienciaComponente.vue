<script setup>
import { ref } from 'vue';
import BocaDeUrna from "../assets/BocaDeUrna.png";
import Encuesta from '../assets/calendar-check-svgrepo-com.svg';
import Comunicador from "../assets/Comunicador.png";
const titulo = 'Experiencia';
const fecha = 'Desde 2021';
const experiencias = ref([
    { id: 1, src:Encuesta, parrafo: 'Trabaje haciendo encuestas para las elecciones a gobernador, sobre las problematicas que creian los ciudadanos que se tenian que resolver en la provincia, en el año 2021.'},
    { id: 2, src:BocaDeUrna, parrafo: 'Trabaje Haciendo boca de urna para una encuestadora, que queria analizar de antemano el resultado de las elecciones municipales, tambien trabaje como fiscal de mesa voluntario para el partido de La Libertad Avanza todo en el año 2023.' },
    { id: 3, src: Comunicador, parrafo: 'Debido a mi historial, tanto de encuestador como de Boca de Urna, conozco cual es mi lugar, sé cómo tratar a una persona, a un público, sé cómo manejar ciertas situaciones y cómo tratar a personas "conflictivas".' },
   

]);
</script>

<template>
    <div class="card">
        <h3 class="titulo">{{ titulo }}</h3>
        <p class="fecha">{{ fecha }}</p>
        <ul class="listado">
            <li class="item" v-for="experiencia in experiencias" :key="experiencia.id">
                <img class="image-svg" :src="experiencia.src" width="45rem" :alt="experiencia.parrafo">
                <p>{{ experiencia.parrafo }}</p>
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
    display: flex;
    align-items: center;
    padding: 1rem;
    gap: 1.5rem;
}

.image-svg {
    width: 45px; /* Ajusta el tamaño de la imagen */
}

p{
    color:aliceblue;
}
</style>
