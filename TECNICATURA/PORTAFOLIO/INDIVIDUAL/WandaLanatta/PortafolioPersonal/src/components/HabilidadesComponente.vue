<script setup>
import { ref } from 'vue';

const habilidades = ref([
    {
        id: 1,
        nombre: 'Lenguajes de Programación',
        habilidades: [
        // Se crea un objeto con id, nombre, nivel e ícono
        { id: 1, nombre: 'JavaScript', nivel: 'Intermedio', icono: 'src/components/icons/icons/javascript.svg' },
        { id: 2, nombre: 'Python', nivel: 'Intermedio', icono: 'src/components/icons/icons/python.svg' },
        { id: 3, nombre: 'HTML/CSS', nivel: 'Avanzado', icono: 'src/components/icons/icons/html-css.svg' },
        { id: 4, nombre: 'Java', nivel: 'Intermedio', icono: 'src/components/icons/icons/java.svg' },
        { id: 5, nombre: 'SQL', nivel: 'Intermedio', icono: 'src/components/icons/icons/sql.svg' }
        ]
    },
    {
        id: 2,
        nombre: 'Frameworks y Librerías',
        habilidades: [
        { id: 1, nombre: 'React.js', nivel: 'Avanzado', icono: 'src/components/icons/icons/react.svg' },
        { id: 2, nombre: 'Vue.js', nivel: 'Intermedio', icono: 'src/components/icons/icons/vue.svg' },
        { id: 3, nombre: 'Node.js', nivel: 'Avanzado', icono: 'src/components/icons/icons/node.svg' },
        { id: 4, nombre: 'Django', nivel: 'Intermedio', icono: 'src/components/icons/icons/django.svg' },
        { id: 5, nombre: 'Bootstrap', nivel: 'Avanzado', icono: 'src/components/icons/icons/bootstrap.svg' }
        ]
    } ,
    {
        id: 3,
        nombre: 'Herramientas y Software',
        habilidades: [
        // Se crea un objeto con id, nombre, nivel e ícono
        { id: 1, nombre: 'Git', nivel: 'Avanzado', icono: 'src/components/icons/icons/git.svg' },
        { id: 2, nombre: 'Docker', nivel: 'Intermedio', icono: 'src/components/icons/icons/docker.svg' },
        { id: 3, nombre: 'Cypress', nivel: 'Avanzado', icono: 'src/components/icons/icons/cypress.svg' },
        { id: 4, nombre: 'Figma', nivel: 'Intermedio', icono: 'src/components/icons/icons/figma.svg' },
        { id: 5, nombre: 'Visual Studio Code', nivel: 'Intermedio', icono: 'src/components/icons/icons/visual.svg' }
        ]
    },
    {
        id: 4,
        nombre: 'Base de Datos',
        habilidades: [
        { id: 1, nombre: 'MongoDB', nivel: 'Avanzado', icono: '/src/components/icons/icons/mongo.svg' },
        { id: 2, nombre: 'MySQL', nivel: 'Intermedio', icono: '/src/components/icons/icons/mysql.svg' },
        { id: 3, nombre: 'PostgreSQL', nivel: 'Avanzado', icono: '/src/components/icons/icons/postgres.svg' }        
        ]
    },
    {
        id: 5,
        nombre: 'Idiomas',
        habilidades: [
        // Se crea un objeto con id, nombre, nivel e ícono
        { id: 1, nombre: 'Español', nivel: 'Nativo', icono: '/src/components/icons/icons/arg.svg' },
        { id: 2, nombre: 'Ingles', nivel: 'Intermedio', icono: '/src/components/icons/icons/eeuu.svg' }
        ]
    }
]);
</script>

<template>
    <!-- Este componente vue funciona de esta forma: -->
    <div class="skills-contenedor">
    <!-- Se recorre el array habilidades con v-for y se asigna la key habilidad.id -->
        <div v-for="habilidad in habilidades" :key="habilidad.id" class="skills-categoria">
            <!-- Se muestra el nombre de la habilidad -->
            <h3>{{ habilidad.nombre }}</h3>
            <ul class="skills">
            <!-- Se recorre el array habilidades con v-for y se asigna la key habilidad.id -->
            <li v-for="habilidad in habilidad.habilidades" :key="habilidad.id" class="skill">
                <!-- Se muestra el ícono de la habilidad y el nombre de la habilidad con su nivel -->
                <img :src="habilidad.icono" :alt="habilidad.nombre">
                <!-- Se muestra el ícono de la habilidad y el nombre de la habilidad con su nivel -->
                <span>{{ habilidad.nombre }}: {{ habilidad.nivel }}</span>
            </li>
            </ul>
        </div>
    </div>

    <!-- <div class="stacks-container">
 
        <section>
            <h2>{{ subtitulo1 }}</h2>
            <ul>
                <li v-for="front in frontLista" :key="front.id">
                    <img :src="front.src" alt="Icono de {{ front.nombre }}" class="front-img">
                    <div>
                        {{ front.nombre }}
                    </div>
                </li>
            </ul>
        </section>

     
        <section>
            <h2>{{ subtitulo2 }}</h2>
            <ul>
                <li v-for="back in backLista" :key="back.id">
                    <img :src="back.src" alt="Icono de {{ back.nombre }}" class="back-img">
                    <div>
                        {{ back.nombre }}
                    </div>
                </li>
            </ul>
        </section>

         Sección Bases de Datos y Control de Versiones (en una columna) 
        <div class="combined-section">
             Sección Base de Datos 
            <section>
                <h2>{{ subtitulo3 }}</h2>
                <ul>
                    <li v-for="datos in datosLista" :key="datos.id">
                        <img :src="datos.src" alt="Icono de {{ datos.nombre }}" class="datos-img">
                        <div>
                            {{ datos.nombre }}
                        </div>
                    </li>
                </ul>
            </section>

             Sección Control de Versiones 
            <section>
                <h2>{{ subtitulo4 }}</h2>
                <ul>
                    <li v-for="versiones in versionesLista" :key="versiones.id">
                        <img :src="versiones.src" alt="Icono de {{ versiones.nombre }}" class="versiones-img">
                        <div>
                            {{ versiones.nombre }}
                        </div>
                    </li>
                </ul>
            </section>
        </div>
    </div> -->
    
</template>

<style scoped>

.skills-contenedor {
    padding: 2rem;
}

.skills-categoria {
    margin-bottom: 20px;
}

.skills-categoria h3 {
    display: flex;
    justify-content: left;
    margin-bottom: 10px;
    font-size: 1.5rem;
   color:  rgba(60, 60, 60, 0.66);
    font-size: 1.4rem;
    font-weight: bold;
}

.skills {
    display: flex;
    justify-content: space-evenly;
    flex-wrap: wrap;
    gap: 20px;
}

.skill {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 8px;
    background-color: white;
    padding: 0.3em;
    border-radius: 8px;
    box-shadow: #a5c8ca;
    flex: 1 1 159px;
    max-width: 240px;
}

.skill:hover {
    background-color: #c3ecee;
}

.skill img {
    width: 35px;
    height: 35px;
}

.skill span {
    font-size: 1em;
    color: grey;
}

.skill:hover {
    font-size: 1.3em;
    transition: 1s ease;
}

@media (max-width: 768px) {
    .skills-categoria h3 {
        justify-content: center;
    }
    .skill {
        justify-content: center;
    }
}
</style>