<script setup>
import { ref } from 'vue';
const titulo='Mi Trayectoria en la Programación';
const fecha='Desde Enero 2022 / ...';
const experiencias = ref([
    {id:1, src:'/src/assets/ventas.svg', parrafo: 'Me atrae la programación y he dedicado numerosas horas a aprender y practicar diferentes lenguajes.'},
    {id:2, src:'src/assets/ecomerce.svg', parrafo: 'He completado varios proyectos personales que me han permitido aplicar mis conocimientos y mejorar mis habilidades técnicas.'},
    {id:3, src: 'src/assets/configuracion.svg', parrafo: 'Mi dedicación al aprendizaje continuo me ha llevado a dominar conceptos clave en desarrollo web y software.'},
    {id:4, src: 'src/assets/uiux.svg', parrafo: 'A través de cursos en línea y recursos autodidactas, he adquirido una sólida comprensión de las mejores prácticas en programación.'},
    {id:5, src: 'src/assets/watch.svg', parrafo: 'Estoy comprometida a seguir creciendo profesionalmente y estoy entusiasmado por las oportunidades de aplicar mis habilidades en un entorno profesional.'}
])
</script>

<template>
    <div class="card">
        <h3 class="titulo">{{  titulo }}</h3>
        <p class="fecha">{{ fecha }}</p>
        <ul class="listado">
            <li class="item" v-for="experiencia in experiencias" :key="experiencia.id">
                <img class="imagen123.svg" :src="experiencia.src" width="45rem" :alt="experiencia.parrafo">
                <p>{{  experiencia.parrafo }}</p>
            </li>

           <!-- <li class="item"><img class="imagen-svg" src="/src/assets/ventas.svg" width="45rem " alt="">
                <p>Lideré un grupo de desarrolladores en la crecaión de una plataforma para un negocio</p>
            </li>
            <li class="item"><img class="imagen-svg" src="/src/assets/ecomerce.svg" width="45rem" alt="">
                <p>Diseñé y desarrollé aplicaciones web utilizando Node.js, React y MongoDB</p>
            </li>
            <li class="item"><img class="imagen-svg" src="/src/assets/configuracion.svg" width="45rem" alt="">
                <p>Implementé soluciones de autenticación y autorización, mejorando la seguridad del sitio web</p>
            </li>
            <li class="item"><img class="imagen-svg" src="/src/assets/uiux.svg" width="45rem" alt="">
                <p>Colaboré con diseñadores de UX/UI para crear interfaces de usuario atractivas y fáciles de usar</p>
            </li>
            <li class="item"><img class="imagen-svg" src="/src/assets/watch.svg" width="45rem" alt="">
                <p>Automaticé procesos de despliegue continuo utilizando Jenkins y Docker</p>
            </li> -->
        </ul>
    </div>
</template>

<style scoped>

.card{
    display: flex;
    flex-direction: column;
    padding: 2rem;
    background-color: rgb(28, 41, 52);
    border-radius: 15px;
}

.titulo{
    font-size: 1.5rem;
    color: coral;
}
.fecha{
    font-size: 1rem;
    color: burlywood;
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