<script setup>
import { ref } from 'vue';
import FondoLava from './FondoLava.vue';

const intereses = ref([
    { id: 1, titulo: 'Algoritmos y Estructuras de Datos:', parrafo: 'Optimización y resolución eficiente de problemas utilizando estructuras como listas, árboles, grafos, etc.' },
    { id: 2, titulo: 'Lenguajes de Programación:', parrafo: 'Aprender y dominar distintos lenguajes como Python, Java, C++, JavaScript, entre otros.' },
    { id: 3, titulo: 'Desarrollo de Software:', parrafo: 'Crear aplicaciones, sistemas, videojuegos, o plataformas tecnológicas.' },
    { id: 4, titulo: 'Inteligencia Artificial y Machine Learning:', parrafo: 'Interés en el aprendizaje automático, redes neuronales y el procesamiento de grandes volúmenes de datos.' },
    { id: 5, titulo: 'Diseño UX/UI:', parrafo: 'Diseñar interfaces de usuario y experiencias interactivas que sean estéticamente atractivas y fáciles de usar.' },
    { id: 6, titulo: 'Ilustración y Arte Digital:', parrafo: 'Desarrollar habilidades en la creación de gráficos vectoriales, ilustraciones digitales y otras formas de arte visual.' },
    { id: 7, titulo: 'Teoría del Color:', parrafo: 'Experimentar con colores y paletas para transmitir emociones, crear armonía o destacar elementos clave en los diseños.' }
]);
</script>

<template>
    <div class="interesesContenedor">
        <FondoLava />
        <ul class="contenedorLista">
            <li class="item" v-for="interes in intereses" :key="interes.id">
                <p class="titulo">{{ interes.titulo }}</p>
                <p>{{ interes.parrafo }}</p>
            </li>
        </ul>
    </div>
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

.titulo {
  text-decoration: underline;
}

.item {
    margin-bottom: 1rem;
}
</style>
