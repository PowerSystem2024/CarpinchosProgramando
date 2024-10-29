<template>
  <div>
    <h1 class="title">Portafolios Carpinchos Programando</h1>
    <div class="introduction">
      <p class="group-description">
        Somos alumnos de la Tecnicatura Universitaria en Programación de la UTN
        (Universidad Tecnológica Nacional FRSR). Actualmente estamos cursando el
        segundo semestre y pertenecemos a la cohorte 2024. Durante este trayecto
        formativo, estamos aprendiendo en la Cátedra Programación II, lenguajes de programación como Java, JavaScript, Python y herramientas como Vue.js y Git.
      </p>
    </div>

    <div class="circle">
      <div
        v-for="(student, index) in students"
        :key="index"
        :style="getNodeStyle(index)"
        class="node"
      >
        <img :src="student.image" :class="['student-image', student.size]" />
        <a :href="student.portfolio"
          class="node-link"
          :style="getLinkStyle(index, index)">{{ student.name }}</a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

// Importar imágenes
import MelinaImage from '@/assets/Melina.png';
import MarianaImage from '@/assets/Mariana.png';
import MercedesImage from '@/assets/Mercedes.png';
import WandaImage from '@/assets/Wanda.png';
import NicolasImage from '@/assets/Nicolas.png';
import NelsonImage from '@/assets/Nelson.png';
import AnaImage from '@/assets/Ana.png'; // Cambiado a Ana.png

const students = ref([
  { name: "Aguilar, Melina Elizabeth", portfolio: "/portafolio1", image: MelinaImage, size: 'peque-image' },
  { name: "Aguilera, Mariana Florencia", portfolio: "https://marianafaguilera.netlify.app/", image: MarianaImage, size: 'small-image' },
  { name: "Atim, Maria Mercedes", portfolio: "https://mariamercedesatim.netlify.app/", image: MercedesImage, size: 'medium-image' },
  { name: "Lanatta, Wanda Oriana", portfolio: "/portafolio4", image: WandaImage, size: 'medium-image' },
  { name: "Mercado, Nicolas Exequiel", portfolio: "/portafolio5", image: NicolasImage, size: 'larger-image' }, // Más grande
  { name: "Rios, Nelson Omar", portfolio: "https://nelsonrios.netlify.app/", image: NelsonImage, size: 'large-image' }, // Más grande
  { name: "Rios Garin, Ana Paula", portfolio: "/portafolio7", image: AnaImage, size: 'medium-image' },
]);

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
    'GreenYellow',
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
  border: 10px solid rgb(255, 255, 0);
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
</style>
