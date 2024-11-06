<script setup>
import { ref } from 'vue';
//Este es un arreglo con ref para que se pueda reactivar el cambio de los intereses
const intereses = ref([
    'Creador de Contenido: Soy un creador de contenido en ascenso, compartiendo mi pasión por los videojuegos y la interacción con la comunidad a través de plataformas como Twitch, YouTube y Tik tok.',
    'Edición de Video: Me encanta todo el proceso de creación de contenido, desde la grabación hasta la edición, lo que me permite darle un toque profesional y creativo a mis transmisiones.',
    'Seguridad Informática: Me interesa profundamente la ciberseguridad y siempre busco aprender sobre nuevas amenazas, vulnerabilidades y cómo proteger sistemas y redes.',
    'Programación: Disfruto programando y explorando diferentes lenguajes de programación, ya que cada uno ofrece nuevas formas de resolver problemas y crear soluciones innovadoras.',
    'Aprendizaje de Nuevas Tecnologías: Me apasiona estar al tanto de las últimas tendencias en tecnología y siempre busco nuevos retos para mejorar mis habilidades y conocimientos.'
]);
</script>

<template>
    <div class="intereses-contenedor">
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
    max-width: 85%;
    padding: 1rem;
}

.contenedor-lista {
    list-style:symbols(•);
    padding: 1rem;
    margin-bottom: .5rem;
    color: var(--vt-c-white-soft);
    font-size: 1.4rem;
    text-shadow: 3px 3px 6px rgba(0, 0, 0, 1);
}

.item {
    margin-bottom: 1rem;
    text-align: center;
    background-color: rgba(0, 0, 0, 0.9);
    font-size: 22px;
}
</style>