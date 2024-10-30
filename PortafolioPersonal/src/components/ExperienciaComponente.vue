<script setup>
import { ref } from 'vue';
const titulo = 'Desarrollador Full Stack';
const fecha = 'Desde Marzo 2024';
const experiencias = ref([
        { id: 1, src: 'src/assets/ventas.svg', parrafo: 'Líder en un equipo de 5 desarrolladores en la creación de una plataforma de comercio electrónico que incrementó las ventas en un 35% durante el primer año.' },
        { id: 2, src: '/src/assets/ecommerce.svg', parrafo: 'Diseñé y desarrollé aplicaciones web utilizando Node.js, React y MongoDB, logrando reducir el tiempo de carga de las páginas en un 50%.' },
        { id: 4, src: '/src/assets/uiux.svg', parrafo: 'Colaboré con diseñadores de UX/UI para crear interfaces de usuario atractivas y fáciles de usar, aumentando la satisfacción del cliente en un 15%.' },
        { id: 5, src: '/src/assets/watch.svg', parrafo: 'Automatizé procesos de despliegue continuo utilizando Jenkins y Docker, reduciendo los tiempos de despliegue en un 40%.' }
    ]);
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