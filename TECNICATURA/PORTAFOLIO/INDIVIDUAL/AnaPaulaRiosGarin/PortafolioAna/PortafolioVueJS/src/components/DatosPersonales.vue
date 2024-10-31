<script setup>
// Importación de componentes (img)
import LinkedIn from "./icons/LinkedIn.ico";
import GitHub from "./icons/GitHub.ico";
import CurriculumVitae from "./icons/Curriculum Vitae.ico";

const titulo = "Ana Paula Ríos Garín";
    const descripcion = "Tecnica Universitaria en Programación - UTN";
    const residencia = "Tres de Febrero, Buenos Aires, Argentina";
    const presentacion = "Hola, bienvenido a mi portafolio, soy una desarrolladora web con experiencia en el desarrollo de aplicaciones web y móviles.";
    const telefono = "+54 9 11 5617-6194";
    const mail = "anapaulariosgarin@gmail.com"
    const redesSociales = [
        {id: 1, name: "LinkedIn", src: LinkedIn, url: "www.linkedin.com/in/anapaularíosgarín"},
        {id: 2, name: "GitHub", src: GitHub, url: "https://github.com/anaprg05"},
        {id: 3, name: "Curriculum Vitae", src: CurriculumVitae, url: "https://www.canva.com/design/DAGPt5_Bvv0/tHZ-6Si8BzCF7xjJRDghXQ/edit?utm_content=DAGPt5_Bvv0&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton"}
    ];

</script>

<template>
    <section class="datosPersonales">
        <div class="card">
            <h1>{{ titulo }}</h1>
            <h2>{{ descripcion }}</h2>
            <p>{{ presentacion }}</p>
            <ul class="containerLista">
                <li v-for="red in redesSociales" :key="red.id">
                    <a :href="red.url" target="_blank">
                        <img class="iconRedSocial" :src="red.src" width="35rem" :alt="red.name">
                    </a>
                </li>
            </ul>
            <h3>Mi teléfono personal: {{ telefono }}</h3>
            <h3>Mi correo electrónico: {{ mail }}</h3>
            <h4>{{ residencia }}</h4>
        </div>
    </section>
</template>

<style scoped>
h1 {
    font-size: 2.5rem;
    color: #E7E8C4;
}

h2 {
    color: #B9CA88;
}

p {
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: 1rem;
    color: #DDE5B6;
}

a {
    color: #674633;
}

.card {
    background-color: #9B8965;
    border-radius: 10px;
    padding: 10px;
    margin: 10px;
    text-align: center;
}

.containerLista{
    display: flex;
    justify-content: center;
    list-style: none;
    padding: 0;
    margin: 0;
    text-align: center;
}

.iconRedSocial {
    align-items: center;
    background-color: #6C584C;;
    border-radius: 50%;
    padding: 2px;
    margin: 5px;
    box-shadow: 0 0 5px #ADC178;
}

.iconRedSocial:hover {
    background-color: #DDE5B6;
    box-shadow: 0 0 5px #E7E8C4;
}

h1 {
    font-size: 1.2rem;
    font-weight: 600;
}
</style>