<script setup>
import { ref } from 'vue';

// Importación de componentes (img)
// LENGUAJES DE PROGRAMACIÓN
import Python from '/src/assets/Habilidades/python.svg';
import Java from '/src/assets/Habilidades/java.svg';
import JavaScript from '/src/assets/Habilidades/javascript.svg';
import SQL from '/src/assets/Habilidades/sql.svg';
import LenguajeC from '/src/assets/Habilidades/lenguajec.svg';
// DESARROLLO WEB
import HTML from '/src/assets/Habilidades/html.svg';
import CSS from '/src/assets/Habilidades/css.svg';
// HERRAMIENTAS Y SOFTWARE
import VisualStudioCode from '/src/assets/Habilidades/visualstudiocode.svg';
import PyCharm from '/src/assets/Habilidades/pycharm.svg';
import NetBeans from '/src/assets/Habilidades/netbeans.svg';
import Arduino from '/src/assets/Habilidades/arduino.svg';
import Git from '/src/assets/Habilidades/git.svg';
import GitHub from '/src/assets/Habilidades/github.svg';
import Photoshop from '/src/assets/Habilidades/photoshop.svg';
import ClipStudioPaint from '/src/assets/Habilidades/clipstudiopaint.svg';
// FRAMEWORKS Y LIBRERÍAS
import VueJS from '/src/assets/Habilidades/vuejs.svg';
import NodeJS from '/src/assets/Habilidades/nodejs.svg';
import Bootstrap from '/src/assets/Habilidades/bootstrap.svg';
// BASE DE DATOS
import MySQL from '/src/assets/Habilidades/mysql.svg';
// PAQUETE OFFICE
import Word from '/src/assets/Habilidades/word.svg';
import Excel from '/src/assets/Habilidades/excel.svg';
import PowerPoint from '/src/assets/Habilidades/powerpoint.svg';
// IDIOMAS
import Español from '/src/assets/Habilidades/español.svg';
import Ingles from '/src/assets/Habilidades/ingles.svg';
// HABILIDADES BLANDAS
import ComunicacionAsertiva from '/src/assets/Habilidades/comunicacionasertiva.svg';
import TrabajoEnEquipo from '/src/assets/Habilidades/trabajoenequipo.svg';
import AprendizajeRapido from '/src/assets/Habilidades/aprendizajerapido.svg';
import Empatia from '/src/assets/Habilidades/empatia.svg';
import CriticasConstructivas from '/src/assets/Habilidades/criticasconstructivas.svg';
import Creatividad from '/src/assets/Habilidades/creatividad.svg';

const habilidades = ref ([
{
    id: 1, nombre: 'LENGUAJES DE PROGRAMACIÓN', habilidades: [
        { id: 1, nombre: 'Python', nivel: 'Principiante', icono: Python },
        { id: 2, nombre: 'Java', nivel: 'Principiante', icono: Java },
        { id: 3, nombre: 'JavaScript', nivel: 'Principiante', icono: JavaScript },
        { id: 4, nombre: 'SQL', nivel: 'Principiante', icono: SQL },
        { id: 5, nombre: 'Lenguaje C', nivel: 'Principiante', icono: LenguajeC }
    ]
},
{
    id: 2, nombre: 'DESARROLLO WEB', habilidades: [
        { id: 1, nombre: 'HTML', nivel: 'Avanzado', icono: HTML },
        { id: 1, nombre: 'CSS', nivel: 'Intermedio', icono: CSS }
    ]
},
{
    id: 3, nombre: 'HERRAMIENTAS Y SOFTWARE', habilidades: [
        { id: 1, nombre: 'Visual Studio Code', nivel: 'Avanzado', icono: VisualStudioCode },
        { id: 2, nombre: 'PyCharm', nivel: 'Principiante', icono: PyCharm },
        { id: 3, nombre: 'NetBeans', nivel: 'Principiante', icono: NetBeans },
        { id: 4, nombre: 'Arduino', nivel: 'Principiante', icono: Arduino },
        { id: 5, nombre: 'Git', nivel: 'Principiante', icono: Git },
        { id: 6, nombre: 'GitHub', nivel: 'Principiante', icono: GitHub },
        { id: 7, nombre: 'Photoshop', nivel: 'Intermedio', icono: Photoshop },
        { id: 8, nombre: 'Clip Studio Paint', nivel: 'Intermedio', icono: ClipStudioPaint }

    ]
},
{
    id: 4, nombre: 'FRAMEWORKS Y LIBRERÍAS', habilidades: [
        { id: 1, nombre: 'VueJS', nivel: 'Principiante', icono: VueJS },
        { id: 2, nombre: 'NodeJS', nivel: 'Principiante', icono: NodeJS },
        { id: 3, nombre: 'Bootstrap', nivel: 'Principiante', icono: Bootstrap }
    ]
},
{
    id: 5, nombre: 'BASE DE DATOS', habilidades: [
        { id: 1, nombre: 'MySQL', nivel: 'Principiante', icono: MySQL }
    ]
},
{
    id: 6, nombre: 'PAQUETE OFFICE', habilidades: [
        { id: 1, nombre: 'Word', nivel: 'Avanzado', icono: Word },
        { id: 2, nombre: 'Excel', nivel: 'Principiante', icono: Excel },
        { id: 3, nombre: 'PowerPoint', nivel: 'Avanzado', icono: PowerPoint }
    ]
},
{
    id: 7, nombre: 'IDIOMAS', habilidades: [    
        { id: 1, nombre: 'Español', nivel: 'Nativo', icono: Español },
        { id: 2, nombre: 'Inglés', nivel: 'Intermedio (A2)', icono: Ingles }
    ]
}
]);
const habilidadesBlandas = ref ([
{
    id: 1, nombre: 'HABILIDADES BLANDAS', habilidades: [    
        { id: 1, nombre: 'Comunicación asertiva', icono: ComunicacionAsertiva },
        { id: 2, nombre: 'Trabajo en equipo', icono: TrabajoEnEquipo },
        { id: 3, nombre: 'Aprendizaje rápido', icono: AprendizajeRapido },
        { id: 4, nombre: 'Empatía', icono: Empatia },
        { id: 5, nombre: 'Capacidad para aceptar críticas constructivas', icono: CriticasConstructivas },
        { id: 6, nombre: 'Creatividad', icono: Creatividad }
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

