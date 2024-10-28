<script setup>
import { ref } from 'vue';

const habilidades = ref ([
{
    id: 1, nombre: 'LENGUAJES DE PROGRAMACIÓN', habilidades: [
        { id: 1, nombre: 'Python', nivel: 'Principiante', icono: '/src/assets/Habilidades/python.svg' },
        { id: 2, nombre: 'Java', nivel: 'Principiante', icono: '/src/assets/Habilidades/java.svg' },
        { id: 3, nombre: 'JavaScript', nivel: 'Principiante', icono: '/src/assets/Habilidades/javascript.svg' },
        { id: 4, nombre: 'SQL', nivel: 'Principiante', icono: '/src/assets/Habilidades/sql.svg' },
        { id: 5, nombre: 'Lenguaje C', nivel: 'Principiante', icono: '/src/assets/Habilidades/lenguajec.svg' }
    ]
},
{
    id: 2, nombre: 'DESARROLLO WEB', habilidades: [
        { id: 1, nombre: 'HTML', nivel: 'Avanzado', icono: '/src/assets/Habilidades/html.svg' },
        { id: 1, nombre: 'CSS', nivel: 'Intermedio', icono: '/src/assets/Habilidades/css.svg' }
    ]
},
{
    id: 3, nombre: 'HERRAMIENTAS Y SOFTWARE', habilidades: [
        { id: 1, nombre: 'Visual Studio Code', nivel: 'Avanzado', icono: '/src/assets/Habilidades/visualstudiocode.svg' },
        { id: 2, nombre: 'PyCharm', nivel: 'Principiante', icono: '/src/assets/Habilidades/pycharm.svg' },
        { id: 3, nombre: 'NetBeans', nivel: 'Principiante', icono: '/src/assets/Habilidades/netbeans.svg' },
        { id: 4, nombre: 'Arduino', nivel: 'Principiante', icono: '/src/assets/Habilidades/arduino.svg' },
        { id: 5, nombre: 'Git', nivel: 'Principiante', icono: '/src/assets/Habilidades/git.svg' },
        { id: 6, nombre: 'Photoshop', nivel: 'Intermedio', icono: '/src/assets/Habilidades/photoshop.svg' },
        { id: 7, nombre: 'Clip Studio Paint', nivel: 'Intermedio', icono: '/src/assets/Habilidades/clipstudiopaint.svg' }

    ]
},
{
    id: 4, nombre: 'FRAMEWORKS Y LIBRERÍAS', habilidades: [
        { id: 1, nombre: 'VueJS', nivel: 'Principiante', icono: '/src/assets/Habilidades/vuejs.svg' },
        { id: 2, nombre: 'NodeJS', nivel: 'Principiante', icono: '/src/assets/Habilidades/nodejs.svg' },
        { id: 3, nombre: 'Bootstrap', nivel: 'Principiante', icono: '/src/assets/Habilidades/bootstrap.svg' }
    ]
},
{
    id: 5, nombre: 'BASE DE DATOS', habilidades: [
        { id: 1, nombre: 'MySQL', nivel: 'Principiante', icono: '/src/assets/Habilidades/mysql.svg' }
    ]
},
{
    id: 6, nombre: 'PAQUETE OFFICE', habilidades: [
        { id: 1, nombre: 'Word', nivel: 'Avanzado', icono: '/src/assets/Habilidades/word.svg' },
        { id: 2, nombre: 'Excel', nivel: 'Principiante', icono: '/src/assets/Habilidades/excel.svg' },
        { id: 3, nombre: 'PowerPoint', nivel: 'Avanzado', icono: '/src/assets/Habilidades/powerpoint.svg' }
    ]
},
{
    id: 7, nombre: 'IDIOMAS', habilidades: [    
        { id: 1, nombre: 'Español', nivel: 'Nativo', icono: '/src/assets/Habilidades/español.svg' },
        { id: 2, nombre: 'Inglés', nivel: 'Intermedio (A2)', icono: '/src/assets/Habilidades/ingles.svg ' }
    ]
}
]);
const habilidadesBlandas = ref ([
{
    id: 1, nombre: 'HABILIDADES BLANDAS', habilidades: [    
        { id: 1, nombre: 'Comunicación asertiva', icono: '/src/assets/Habilidades/comunicacionasertiva.svg' },
        { id: 2, nombre: 'Trabajo en equipo', icono: '/src/assets/Habilidades/trabajoenequipo.svg' },
        { id: 3, nombre: 'Aprendizaje rápido', icono: '/src/assets/Habilidades/aprendizajerapido.svg' },
        { id: 4, nombre: 'Empatía', icono: '/src/assets/Habilidades/empatia.svg' },
        { id: 5, nombre: 'Capacidad para aceptar críticas constructivas', icono: '/src/assets/Habilidades/criticasconstructivas.svg' },
        { id: 6, nombre: 'Creatividad', icono: '/src/assets/Habilidades/creatividad.svg' }
    ]
}
]);
</script>

<template>
    <div class="habilidadesContainer">
      <div v-for="categoria in habilidades" :key="categoria.id" class="habilidadesCategoria">
        <h3>{{ categoria.nombre }}</h3>
        <ul class="habilidades">
          <li v-for="habilidad in categoria.habilidades" :key="habilidad.id" class="habilidad">
            <img :src="habilidad.icono" :alt="habilidad.nombre">
            <span>{{ habilidad.nombre }}: {{ habilidad.nivel }}</span>
          </li>
        </ul>
      </div>

      <div v-for="categoria in habilidadesBlandas" :key="categoria.id" class="habilidadesCategoria">
        <h3>{{ categoria.nombre }}</h3>
        <ul class="habilidades">
          <li v-for="habilidad in categoria.habilidades" :key="habilidad.id" class="habilidad">
            <img :src="habilidad.icono" :alt="habilidad.nombre">
            <span>{{ habilidad.nombre }}</span>
          </li>
        </ul>
      </div>
    </div>
  </template>

<style scoped>
.habilidadesContainer {
    padding: 2rem;
    background-color: #ABA370;
    border-radius: 10px;
}

.habilidadesCategoria {
    margin-bottom: 20px;
}

.habilidadesCategoria h3 {
    display: flex;
    justify-content: left;
    margin-bottom: 10px;
    font-size: 1.5rem;
    color: #6C584C;
    font-weight: bold;
}

.habilidades {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    gap: 20px;
}

.habilidad {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    background-color: #C5D397;
    padding: 0.3rem;
    border-radius: 8px;
    box-shadow: 0px 4px 12px #8B6E5A;
    flex: 1 1 200px;
    min-width: 250px;
}

.habilidad:hover {
    background-color: #ADC178;
}

.habilidad img {
    width: 35px;
    height: 35px;
}

.habilidad span {
    font-size: 1em;
    color: #333;
}

.habilidad:hover {
    font-size: 1.2em;
    transition: 1s ease;
}

@media (max-width: 768px) {
    .habilidadesCategoria h3 {
        justify-content: center;
    }
    .habilidad {
        justify-content: center;
    }
}
</style>

