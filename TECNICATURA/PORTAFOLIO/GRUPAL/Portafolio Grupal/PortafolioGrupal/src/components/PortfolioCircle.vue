<template>
  <div class="contenedor">
    <h1 class="title">Portafolios Carpinchos Programando</h1>
    <div class="introduction">
      <p class="group-description">
        Somos alumnos de la Tecnicatura Universitaria en Programación de la UTN
        (Universidad Tecnológica Nacional FRSR). Actualmente estamos cursando el
        segundo semestre y pertenecemos a la cohorte 2024. Durante este trayecto
        formativo, estamos aprendiendo en la Cátedra Programación II, lenguajes de programación como Java, JavaScript, Python y herramientas como Vue.js y Git.
        <br><br>Por favor, para ver los portafolios tocar el nombre del alumno.
      </p>
    </div>

    <div class="circle" v-if="windowWidth > 600">
      <div
        v-for="(student, index) in students"
        :key="index"
        :style="getNodeStyle(index)"
        class="node"
      >
        <img :src="student.image" :class="['student-image', student.size]" />
        <a :href="student.portfolio"
          class="node-link"
          :style="getLinkStyle(index)">{{ student.name }}</a>
      </div>
    </div>

    <div v-else class="list-container">
      <div v-for="student in students" :key="student.name" class="student-list-item">
        <img :src="student.image" class="student-image" />
        <a :href="student.portfolio" class="node-link">{{ student.name }}</a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, onUnmounted, ref } from 'vue';

// Importar imágenes
import AnaImage from '@/assets/Ana.png'; // Cambiado a Ana.png
import MarianaImage from '@/assets/Mariana.png';
import MelinaImage from '@/assets/Melina.png';
import MercedesImage from '@/assets/Mercedes.png';
import NelsonImage from '@/assets/Nelson.png';
import NicolasImage from '@/assets/Nicolas.png';
import WandaImage from '@/assets/Wanda.png';

const students = ref([
  { name: "Aguilar, Melina Elizabeth", portfolio: "https://portafolio-vuejs-melina.netlify.app/", image: MelinaImage, size: 'peque-image' },
  { name: "Aguilera, Mariana Florencia", portfolio: "https://marianafaguilera.netlify.app/", image: MarianaImage, size: 'small-image' },
  { name: "Atim, Maria Mercedes", portfolio: "https://mariamercedesatim.netlify.app/", image: MercedesImage, size: 'medium-image' },
  { name: "Lanatta, Wanda Oriana", portfolio: "https://wandalanatta.netlify.app/", image: WandaImage, size: 'medium-image' },
  { name: "Mercado, Nicolas Exequiel", portfolio: "https://nicolasexemercado.netlify.app/", image: NicolasImage, size: 'larger-image' }, // Más grande
  { name: "Rios, Nelson Omar", portfolio: "https://nelsonrios.netlify.app/", image: NelsonImage, size: 'large-image' }, // Más grande
  { name: "Rios Garin, Ana Paula", portfolio: "https://anapaulariosgarin.netlify.app/", image: AnaImage, size: 'medium-image' },
]);

const windowWidth = ref(window.innerWidth);

function updateWindowWidth() {
  windowWidth.value = window.innerWidth;
}

onMounted(() => {
  window.addEventListener('resize', updateWindowWidth);
});

onUnmounted(() => {
  window.removeEventListener('resize', updateWindowWidth);
});

function getNodeStyle(index) {
  const angle = (index / students.value.length) * 2 * Math.PI;
  const radius = 150;
  const x = Math.cos(angle) * radius;
  const y = Math.sin(angle) * radius;

  return {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: `translate(${x}px, ${y}px) translate(-50%, -50%)`,
    textAlign: 'center',
  };
}

function getLinkStyle(index) {
  const angle = (index / students.value.length) * 2 * Math.PI;
  const radius = 110;
  const x = Math.cos(angle) * radius;
  const y = Math.sin(angle) * radius;

  const colors = [
    'OrangeRed',
    'magenta',
    '#FFFF00',
    'deeppink',
    'Green',
    'aqua',
    'Chartreuse',
  ];
  const nodeColor = colors[index % colors.length];

  return {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: `translate(${x}px, ${y}px) translate(-50%, -50%)`,
    backgroundColor: nodeColor,
    color: 'black',
    padding: '5px',
    width: '120px',
    height: '90px',
    lineHeight: '25px',
    textAlign: 'center',
    borderRadius: '5px',
    textShadow: '1px 1px 2px lightgrey',
  };
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@100;400;700&family=Spectral+SC:wght@400&display=swap');

.title {
  font-family: 'Spectral SC', serif;
  text-align: center;
  font-weight: bold;
  font-size: 35px;
  margin-bottom: 20px;
  z-index: 1;
  position: relative;
}

.introduction {
  text-align: center;
  margin-bottom: 50px;
}

.group-description {
  font-family: 'Montserrat', sans-serif;
  font-weight: bold;
  font-size: 20px;
  line-height: 1.5;
  color: #333;
  padding: 0 20px;
  margin-bottom: 200px;
}

.circle {
  position: relative;
  width: 300px;
  height: 300px;
  margin: 20px auto 0;
  border: 10px solid #FF6F61;
  border-radius: 50%;
  background-color: transparent;
}

.node {
  position: absolute;
  width: 80px;
  text-align: center;
}

.student-image {
  margin-bottom: 5px;
  position: relative;
  z-index: 2;
}

.small-image {
  width: 120px;
  height: 100px;
}

.medium-image {
  width: 90px;
  height: 90px;
}

.large-image {
  width: 90px;
  height: 110px;
}

.peque-image {
  width: 110px;
  height: 90px;
}

.larger-image {
  width: 80px;
  height: 100px;
}

.node-link {
  display: block;
  color: black;
  padding: 2px;
  font-family: 'Montserrat', sans-serif;
  font-weight: bolder;
  font-size: 20px;
  text-decoration: none;
}

.list-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.student-list-item {
  display: flex;
  align-items: center;
  margin: 10px 0;
}

.student-list-item img {
  margin-right: 10px;
}

/* Media Queries */
@media (max-width: 600px) {
  .contenedor{
  min-width: 250px;
  }

  h1{
    text-align: center;
    font-weight: bold;
    font-size: 22px;
    color:rgb(33, 93, 214);
  }
  .circle {
    width: 200px;
    height: 200px;
  }

  .node {
    width: 60px;
  }

  .student-image {
    width: 85px; /* Ajusta según sea necesario */
    height: 75px; /* Mantiene la proporción */
  }

  .node-link {
    font-size: 20px; /* Tamaño de fuente más pequeño */
    margin-left: 20px;
    text-align: end;
    text-decoration: underline;
    color: blue;
    }

  .group-description {
    font-size: 22px; /* Tamaño de fuente más pequeño */
    margin-bottom: 100px; /* Ajusta el margen inferior */
  }
}
</style>
