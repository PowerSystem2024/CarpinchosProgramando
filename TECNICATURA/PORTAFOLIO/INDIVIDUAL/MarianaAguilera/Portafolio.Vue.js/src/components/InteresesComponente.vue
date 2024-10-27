<script setup>
import { ref } from 'vue';
import FondoLava from './FondoLava.vue';

//este es un arreglo con ref para que se pueda reactivar el cambio de los intereses

const intereses = ref([
    'Disfruto mantenerme activa y saludable, por lo que voy regularmente al gimnasio. Creo que un cuerpo sano es fundamental para un rendimiento óptimo en todas las áreas de la vida.',
    'Tengo una pasión por la programación y dedico tiempo a estudiar y mejorar mis habilidades en este campo. Me encanta resolver problemas y crear soluciones innovadoras a través del código.',
    'Siempre estoy en busca de nuevas oportunidades para aprender y crecer, especialmente en el ámbito de la programación. Me mantengo actualizado con las últimas tendencias y tecnologías para asegurarme de estar a la vanguardia.'
]);
</script>

<template>
    <div class="intereses-contenedor">
        <FondoLava/>
        <ul class="contenedor-lista">
            <li class="item" v-for="interes in intereses" :key="interes">
                {{ interes }}
            </li>
        </ul>
    </div>
    <!--<div class="intereses-contenedor">
        <ul class="contenedor-lista">
            <li class="ítems">
                Desarrollo de software de código abierto: contribuyo con proyectos en GitHub, colaborando con otros 
                desarrolladores para mejorar herramientas y librerías populares.
            </li>
            <li class="ítems">
                Deporte al aire libre que practico regularmente para mantener el equilibrio entre entre el trabajo
                y la vida personal.
            </li>
            <li class="ítems">
                Tecnología de innovación: me apasiona explorar nuevas tendencias tecnológicas con la inteligencia
                artificial.
            </li>
            <li class="ítems">
                Fotografía: la practico como hobbie, lo que me ayuda a mantener una prespectiva creativa tanto de mi
                vida profesional como personal.
            </li>
        </ul>
    </div>-->
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
    list-style-type: none;
    padding: 1rem;
    margin-bottom: .5rem;
    color: var(--vt-c-white-soft);
    font-size: 1.4rem;
    text-shadow: 3px 3px 6px rgba(0, 0, 0, 1);
}

.item {
    margin-bottom: 1rem;
}
</style>