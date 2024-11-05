<template>
  <div class="ring">
      <div v-for="i in particles" :key="i" class="particle"></div>
  </div>
  <div class="ring2">
      <div v-for="i in particles" :key="i" class="particle2"></div>
  </div>
</template>

<script>
export default {
  name: 'ParticleRing',
  data() {
      return {
          particles: 200,
      };
  },
};
</script>

<style scoped lang="scss">
@keyframes ringRotate {
  0% {
      transform: rotateZ(0deg) rotateY(0deg) rotateX(0deg);
  }
  100% {
      transform: rotateZ(-360deg) rotateY(-360deg) rotateX(-360deg);
  }
}

.ring {
  position: relative;
  width: 0px;
  height: 0px;
  transition: all 1s linear;
  transform-style: preserve-3d;
  animation: ringRotate 15s linear infinite;

  .particle {
      position: absolute;
      width: 3px; /* Ajustado para hacer las partículas más grandes */
      height: 3px; /* Ajustado para hacer las partículas más grandes */
      border-radius: 100%;
      opacity: 0;
      background: #3498db;
  }
}

@for $i from 1 through 200 {
  $z: (random(90) * 4deg);
  $y: (random(90) * 4deg);

  .particle:nth-child(#{$i}) {
      border-radius: 100%;
      animation: birth#{$i} 10s infinite;
      animation-delay: ($i * 0.005s);
  }

  @keyframes birth#{$i} {
      10% {
          opacity: 1;
      }
      12% {
          transform: rotateZ($z) rotateY($y) translateX(300px); /* Ajustado para expandir más */
      }
      80% {
          transform: rotateZ($z) rotateY($y) translateX(150px); /* Ajustado para expandir más */
          opacity: 1;
      }
      90% {
          transform: rotateZ($z) rotateY($y) translateX(450px); /* Ajustado para expandir más */
          box-shadow: 0 0 1px 1px #bdd6d2;;
      }
  }
}

.ring2 {
  position: relative;
  width: 0px;
  height: 0px;
  transition: all 1s linear;
  transform-style: preserve-3d;
  animation: ringRotate 15s linear infinite;

  .particle2 {
      position: absolute;
      width: 4px; /* Ajustado para hacer las partículas más grandes */
      height: 4px; /* Ajustado para hacer las partículas más grandes */
      border-radius: 100%;
      opacity: 0;
      background: #6cc6e3;
  }
}

@for $i2 from 1 through 200 {
  $z2: (random(90) * 4deg);
  $y2: (random(90) * 4deg);

  .particle2:nth-child(#{$i2}) {
      border-radius: 100%;
      animation: birth2#{$i2} 10s infinite;
      animation-delay: ($i2 * 0.005s);
  }

  @keyframes birth2#{$i2} {
      10% {
          opacity: 1;
      }
      12% {
          transform: rotateZ($z2) rotateY($y2) translateX(150px); /* Ajustado para expandir más */
      }
      70% {
          transform: rotateZ($z2) rotateY($y2) translateX(150px); /* Ajustado para expandir más */
          opacity: 1;
      }
      90% {
          transform: rotateZ($z2) rotateY($y2) translateX(300px); /* Ajustado para expandir más */
      }
  }
}
</style>
