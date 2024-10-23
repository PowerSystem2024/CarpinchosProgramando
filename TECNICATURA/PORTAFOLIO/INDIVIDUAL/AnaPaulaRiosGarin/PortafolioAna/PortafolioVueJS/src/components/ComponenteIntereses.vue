<script setup>
import { ref } from 'vue';
import FondoLava from './FondoLava.vue';

const intereses = ref([
    'Algoritmos y Estructuras de Datos: Optimización y resolución eficiente de problemas utilizando estructuras como listas, árboles, grafos, etc.',
    'Lenguajes de Programación: Aprender y dominar distintos lenguajes como Python, Java, C++, JavaScript, entre otros.',
    'Desarrollo de Software: Crear aplicaciones, sistemas, videojuegos, o plataformas tecnológicas.',
    'Inteligencia Artificial y Machine Learning: Interés en el aprendizaje automático, redes neuronales y el procesamiento de grandes volúmenes de datos.',
    'Diseño UX/UI: Diseñar interfaces de usuario y experiencias interactivas que sean estéticamente atractivas y fáciles de usar.',
    'Ilustración y Arte digital: Desarrollar habilidades en la creación de gráficos vectoriales, ilustraciones digitales y otras formas de arte visual.',
    'Teoría del color: Experimentar con colores y paletas para transmitir emociones, crear armonía o destacar elementos clave en los diseños.'
]);
</script>

<template>
    <div class="interesesContenedor">
        <FondoLava />
        <ul class="contenedorLista">
            <li class="item" v-for="interes in intereses" :key="interes">
                {{ interes }}
            </li>
        </ul>
    </div>

<!--
    <div class="interesesContenedor">
        
        <ul class="contenedorLista">
            <li class="item">
                Algoritmos y Estructuras de Datos: Optimización y resolución eficiente de problemas utilizando estructuras como listas, árboles, grafos, etc.
            </li>
            <li class="item">
                Lenguajes de Programación: Aprender y dominar distintos lenguajes como Python, Java, C++, JavaScript, entre otros.
            </li>
            <li class="item">
                Desarrollo de Software: Crear aplicaciones, sistemas, videojuegos, o plataformas tecnológicas.
            </li>
            <li class="item">
                Inteligencia Artificial y Machine Learning: Interés en el aprendizaje automático, redes neuronales y el procesamiento de grandes volúmenes de datos.
            </li>
            <li class="item">
                Diseño UX/UI: Diseñar interfaces de usuario y experiencias interactivas que sean estéticamente atractivas y fáciles de usar.
            </li>
            <li class="item">
                Ilustración y Arte digital: Desarrollar habilidades en la creación de gráficos vectoriales, ilustraciones digitales y otras formas de arte visual.
            </li>
            <li class="item">
                Teoría del color: Experimentar con colores y paletas para transmitir emociones, crear armonía o destacar elementos clave en los diseños.
            </li>
        </ul>
  </div>
-->
</template>

<style scoped>
.interesesContenedor {
    display: flex;
    position: relative;
    margin: 0 auto;
    min-width: 85%;
    padding: 1rem;
}

.contenedorLista {
    list-style-type: none;
    padding: 1rem;
    margin-bottom: .5rem;
    color: #ECE9CB;
    font-size: 1.4rem;
    text-shadow: 3px 3px 6px rgba(0, 0, 0, 1);
}

.item {
    margin-bottom: 1rem;
}
</style>
