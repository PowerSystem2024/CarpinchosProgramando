<script setup>
import { ref } from 'vue';
const titulo = 'Desarrollador Full Stack';
const fecha = 'Desde Marzo 2024';
const experiencias = ref([
    {id: 1, src:'/src/assets/ventas.svg', parrafo: 'Lidere un equipo de 5 desarrolladores'}
])
</script>

<template>
    <div class="card">
        <h3 class="titulo">{{titulo}}</h3>
        <p class="fecha">{{fecha}}</p>
        <ul class="listado">
            <li class="item" v-for="experiencia in experiencias" :key="experiencia.id">
                <img class="image-svg" :src="experiencia.src" width="45rem" :alt="experiencia.parrafo">
                <p>{{ experiencia.parrafo }}</p>
            </li>
        </ul>
    </div>
</template>

<style scoped>
.card{
    display: flex;
    flex-direction: column;
    padding: 2rem;
    background-color:#bdd6d2;
    border-radius: 15px;
}

.titulo{
    font-size: 1.5rem;
    color: #586875;
}

.fecha{
    font-size: 1rem;
    color:#586875;;
    margin-bottom: 1rem;
}

.listado{
    display: flex;
    flex-direction: column;
}

.item{
    align-items: center;
    display: flex;
    padding: 1rem;
    gap: 1.5rem;
}
</style>