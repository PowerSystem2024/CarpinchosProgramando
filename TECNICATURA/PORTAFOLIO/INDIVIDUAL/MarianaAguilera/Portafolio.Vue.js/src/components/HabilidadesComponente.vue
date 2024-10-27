<script setup>
//Se importa ref de vue para poder usarlo
import { ref } from 'vue';
//se crea un array de objetos con las habilidades
//este es un array de objetos con habilidades ue se pueden modificar o agregar
const habilidades = ref([
    { //se crea un objeto con id, nombre y habilidades
        id: 1, nombre: 'Lenguajes de Programación', habilidades: [
        //Se crea un objeto con id, nombre, nivel e ícono
            { id: 1, nombre: 'JavaScript', nivel: 'Inicial', icono: '/src/components/icons/javascript.svg'},
            { id: 2, nombre: 'Python', nivel: 'Inicial', icono: '/src/components/icons/python.svg'},
            { id: 3, nombre: 'HTML/CSS', nivel: 'Inicial', icono: '/src/components/icons/HTML.svg'},
            { id: 4, nombre: 'Java', nivel: 'Inicial', icono: '/src/components/icons/Java.svg'},
            { id: 5, nombre: 'SQL', nivel: 'Inicial', icono: '/src/components/icons/SQL.svg'}
        ]
    },
    {
        id: 2, nombre: 'Frameworks y Librerías', habilidades: [
            { id: 1, nombre: 'Vue.js', nivel: 'Inicial', icono: '/src/components/icons/vue.svg'},
            { id: 2, nombre: 'Node.js', nivel: 'Inicial', icono: '/src/components/icons/Node.svg'},
        ]
    },
    {
        id: 3, nombre: 'Herramientas y Software', habilidades: [ 
            { id: 1, nombre: 'Git', nivel: 'Inicial', icono: '/src/components/icons/git.svg'},
            { id: 2, nombre: 'MySQL', nivel: 'Inicial', icono: '/src/components/icons/mySQL.svg'},
            { id: 3, nombre: 'Visual Studio Code', nivel: 'Inicial', icono: '/src/components/icons/vscode.svg'},
            { id: 4, nombre: 'PyCharm', nivel: 'Inicial', icono: '/src/components/icons/pycharm.svg'},
            { id: 5, nombre: 'Sublime Text', nivel: 'Inicial', icono: '/src/components/icons/sublimeText.svg'}
         ]
    },
    {
        id: 4, nombre: 'Idiomas', habilidades: [
        { id: 1, nombre: 'Español', nivel: 'Nativo', icono: '/src/components/icons/español.svg'},
        { id: 2, nombre: 'Inglés', nivel: 'Inicial', icono: '/src/components/icons/ingles.svg'},
         ]
    }
]);

</script>


<template> 
    <!--Este componente vue funciona de esta forma:-->
    <div class="skills-contenedor">
        <!--Se recorre el array habilidades con v-for y se asigna la key habilidad.id-->
        <div v-for="habilidad in habilidades" :key="habilidad.id" class="skills-categoria">
            <!--Se muestra el nombre de la habilidad-->
            <h3>{{ habilidad.nombre }}</h3>
            <ul class="skills">
                <!--Se recorre el array habilidades con v-for y se asigna la key habilidad.id-->
                <li v-for="habilidad in habilidad.habilidades" :key="habilidad.id" class="skill">
                    <!--Se muestar el ícono de la habilidad y el nombre de la habilidad con su nivel-->
                    <img :src="habilidad.icono" :alt="habilidad.nombre">
                    <!--Se muestra el ícono de la habilidad y el nombre de la habilidad con su nivel-->
                    <span>{{ habilidad.nombre }}: {{ habilidad.nivel }}</span>
                </li>
            </ul>
        </div>
    </div>
    <!--<div class="skills-contenedor">
        <div class="skills-categoria">
            <h3>Lenguajes de Programación</h3>
            <ul class="skills">
                <li class="skill">
                    <img src="/src/components/icons/javascript.svg" alt="JavaScript">
                    <span>JavaScript: Inicial</span>
                </li>
                <li class="skill">
                    <img src="/src/components/icons/python.svg" alt="Python">
                    <span>Python: Inicial</span>
                </li>
                <li class="skill">
                    <img src="/src/components/icons/HTML.svg" alt="HTML/CSS">
                    <span>HTML/CSS: Inicial</span>
                </li>
                <li class="skill">
                    <img src="/src/components/icons/Java.svg" alt="Java">
                    <span>Java: Inicial</span>
                </li>
                <li class="skill">
                    <img src="/src/components/icons/SQL.svg" alt="SQL">
                    <span>SQL: Inicial</span>
                </li>
            </ul>
        </div>
   
    <div class="skills-categoria">
        <h3>Frameworks y Librerías</h3>
        <ul class="skills">
            <li class="skill">
                <img src="/src/components/icons/vue.svg" alt="Vue.js">
                <span>Vue.js: Inicial</span>
            </li>
            <li class="skill">
                <img src="/src/components/icons/Node.svg" alt="Node.js">
                <span>Node: Inicial</span>
            </li>
        </ul>
    </div>
    <div class="skills-categoria">
        <h3>Herramientas y Software</h3>
        <ul class="skills">
            <li class="skill">
                <img src="/src/components/icons/git.svg" alt="Git">
                <span>Git: Inicial</span>
            </li>
            <li class="skill">
                <img src="/src/components/icons/mySQL.svg" alt="MySQL">
                <span>MySQL: Inicial</span>
            </li>
            <li class="skill">
                <img src="/src/components/icons/vscode.svg" alt="Visual Studio Code">
                <span>Visual Studio Code: Inicial</span>
            </li>
            <li class="skill">
                <img src="/src/components/icons/pycharm.svg" alt="PyCharm">
                <span>PyCharm: Inicial</span>
            </li>
            <li class="skill">
                <img src="/src/components/icons/sublimeText.svg" alt="SublimeText">
                <span>SublimeText: Inicial</span>
            </li>
        </ul>
    </div>
    <div class="skills-categoria">
        <h3>Idiomas</h3>
        <ul class="skills">
            <li class="skill">
                <img src="/src/components/icons/español.svg" alt="Español">
                <span>Español: nativo</span>
            </li>
            <li class="skill">
                <img src="/src/components/icons/ingles.svg" alt="Inglés">
                <span>Inglés: (A1)</span>
            </li>
        </ul>
    </div>
</div> -->
</template>

<style scoped>
.skills-contenedor {
    /*display: flex;*/
    padding: 2rem;
    /*Fondo cargado desde una imagen estatica en Assets*/
    background-image: url('/src/assets/fondo.jpg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    /*Fondo con gradiente*/
    /*background: linear-gradient(-45deg, #26021d, #6e0341, #87da6e, #E2E2B6); 
    /* Fondo con color sólido*/
    /* background-color: rgb(28, 41, 52); */
    }

    .skills-categoria {
        margin-bottom: 20px;
    }

    .skills-categoria h3 {
        display: flex;
        justify-content: left;
        margin-bottom: 10px;
        font-size: 1.5em;
        color: rgb(246, 240, 255);
        font-size: 1.5em;
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
        gap: 10px;
        background-color: rgba(241, 245, 243, 0.856);
        padding: 0.3em;
        border-radius: 8px;
        box-shadow: 0px 4px 12px rgba(2, 151, 151, 0.963);
        flex: 1 1 200px;
        max-width: 200px;
    }

    .skill:hover {
        background-color: rgba(2, 151, 151, 0.963);
    }

    .skill img {
        width: 35px;
        height: 35px;
    }

    .skill span {
        font-size: 1em;
        color: #333;
    }

    .skill:hover {
        font-size: 1.3em;
        transition: 2s ease;
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