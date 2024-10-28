<script setup>
import NavBar from './components/NavBar.vue';
import DatosPersonales from './components/DatosPersonales.vue';
import Educacion from './components/EducacionComponente.vue';
import ExperienciaComponente from './components/ExperienciaComponente.vue';
import ProyectosComponente from './components/ProyectosComponente.vue';
import HabilidadesComponente from './components/HabilidadesComponente.vue';
import InteresesComponente from './components/InteresesComponente.vue';
import educacionImg from './assets/Educacion.svg';
import experienciaImg from './assets/Experiencia.svg';
import proyectosImg from './assets/Proyectos.svg';
import habilidadesImg from './assets/Habilidades.svg';
import interesesImg from './assets/Intereses.svg';

</script>

<template>
    <header id="top">
        <!-- Barra de Navegación -->
        <NavBar />
        <!-- Componente Datos Personales -->
        <DatosPersonales />
    </header>
    <main>
        <section id="educacion">
            <h2>
                <img :src="educacionImg" alt="Educación" class="section-icon">
                Educación - Cursos
            </h2>
            <!-- Componente Educación -->
            <Educacion />
        </section>
        <section id="experiencia">
            <h2>
                <img :src="experienciaImg" alt="Experiencia" class="section-icon">
                Experiencia
            </h2>
            <!-- Componente Experiencia -->
            <ExperienciaComponente />
        </section>
        <section id="proyectos">
            <h2>
                <img :src="proyectosImg" alt="Proyectos" class="section-icon">
                Proyectos
            </h2>
            <!-- Componente Proyectos -->
            <ProyectosComponente />
        </section>
        <section id="habilidades">
            <h2>
                <img :src="habilidadesImg" alt="Habilidades" class="section-icon">
                Habilidades
            </h2>
            <!-- Componente Habilidades -->
            <HabilidadesComponente />
        </section>
        <section id="intereses">
            <h2>
                <img :src="interesesImg" alt="Intereses" class="section-icon">
                Intereses
            </h2>
            <!-- Componente Intereses -->
            <InteresesComponente />
        </section>
    </main>
    <footer>
        <a class="link" href="#top">Inicio</a>
        <p>© 2024 Nelson Rios - Portafolio web</p>
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

.link {
    color: #4A90E2;
    font-weight: bold;
    text-decoration: underline;
}

.link:hover {
    background-color: rgb(160, 230, 160);
    border-radius: 10px;
    padding: 0.5rem;
}

h2 {
    color: #4A90E2;
    display: flex; /* Usar flexbox para alinear imagen y texto */
    align-items: center; /* Centrar verticalmente */
    justify-content: center;
    font-weight: bolder;
}

.section-icon {
    width: 60px; /* Ajusta el tamaño según sea necesario */
    height: auto; /* Mantiene la proporción */
    margin-right: 10px; /* Espacio entre la imagen y el texto */
}
</style>
