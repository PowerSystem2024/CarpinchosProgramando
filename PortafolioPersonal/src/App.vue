<script setup> // setup: indica que se va a ejecutar solamente el codigo que se encuentra dentro de este script
  import NavBar from './components/icons/NavBar.vue';
  import DatosPersonales from './components/DatosPersonales.vue';
  import Educacion from './components/EducacionComponente.vue';
  import ExperienciaComponente from './components/ExperienciaComponente.vue';
  import ProyectosComponente from './components/ProyectosComponente.vue';
 import Habilidades from "./components/HabilidadesComponente.vue"
 import Intereses from './components/InteresesComponente.vue';
</script>

<template>

  <header>
    <!-- Barra de Navegacion -->
     <NavBar />

    <!-- Componente Datos Persoanles-->
      <DatosPersonales />
  </header>

  <main>
    <!-- El estilo css de section se encuentra en base.css-->
      <section id="educacion"><h2>Educacion - Cursos</h2>
      <!--Componente Educacion-->
      <Educacion/>
      </section>

      <section id="experiencia"><h2>Experiencia</h2>
      <!--Componente Experiencia-->
      <ExperienciaComponente/>
      </section>

      <section id="proyectos"><h2>Proyectos</h2>
      <!--Componente Proyectos-->
      <ProyectosComponente />
      </section>

      <section id="habilidades"><h2>Habilidades
      <!-- Componente habilidades -->
       <Habilidades/>
    </h2></section>
    
    <section id="intereses"><h2>Intereses</h2>
      <!-- Componente intereses -->
       <Intereses/>
    </section>

      
  </main>
  <footer>
    <a href="#top">Inicio</a>
    <p>@ 2024 Wanda Lanatta - Portafolio web</p>
  </footer>


</template>

<style scoped>
footer { 
  display:flex;
  flex-direction: column;
  align-items: center;
  padding:2rem;
  font-size: 1.3rem;
 }

 h2 {
  color:  gray;
 }
</style>
