<script setup>
import NavBar from './components/NavBar.vue';
import DatosPersonales from './components/DatosPersonales.vue';
import Educacion from './components/EducacionComponente.vue';
import ExperienciaComponente from './components/ExperienciaComponente.vue';
import ProyectoComponente from './components/ProyectoComponente.vue';
import HabilidadesComponente from './components/HabilidadesComponente.vue';
import InteresesComponente from './components/InteresesComponente.vue';
</script>

<template>
   <header id="top">
   <!--barra de navegación-->
    <NavBar/>
    <!--Componente datos personales-->
    <DatosPersonales/>
   </header> 
   <main>
        <!--el estilo css de section se encuentra en base.css-->
        <section id="educacion">
          <h2>Educación - Cursos</h2>
          <!--Componente educación-->
          <Educacion/>
        </section>
        <section id="experiencia">
          <h2>Experiencia</h2>
          <!--Experiencia componente-->
          <ExperienciaComponente/>
        </section>
        <section id="proyectos">
          <h2>Proyectos</h2>
          <!--Componente proyectos-->
          <ProyectoComponente/>
        </section>
        <section id="habilidades">
          <h2>Habilidades</h2>
          <HabilidadesComponente/>
        </section>
        <section id="intereses">
          <h2>Intereses</h2>
          <InteresesComponente/>
        </section>
   </main>
   <footer>
      <a href="#top">Inicio</a>
      <p>@2024 Mariana Aguilera - Portafolio Web - tutorial UTN FRSR</p>
   </footer>
</template>

<style scoped>
footer {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
  font-size: 1.3rem;
}


</style>
