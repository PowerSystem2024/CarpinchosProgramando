<script setup>
import NavBar from './components/NavBar.vue';
import DatosPersonales from './components/DatosPersonales.vue';
import Educacion from './components/EducacionComponente.vue';
import ExperienciaComponente from './components/ExperienciaComponente.vue';
</script>

<template>
   <header> <!--barra de navegación-->
    <NavBar/>
    <DatosPersonales/>
   </header> 
   <main>
        <section id="educacion"><h2>Educación - Cursos</h2>
          <Educacion/>
        </section>
        <section id="experiencia"><h2>Experiencia</h2></section>
          <ExperienciaComponente/>
        <section id="proyectos"><h2>Proyectos</h2></section>
        <section id="habilidades"><h2>Habilidades</h2></section>
        <section id="intereses"><h2>Intereses</h2></section>
   </main>
</template>

<style scoped>


</style>
