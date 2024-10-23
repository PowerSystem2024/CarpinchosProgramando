<script setup>
    
</script>

<template>
    <section class="datosPersonales">
        <div class="card">
            <h1>Ana Paula Ríos Garín</h1>
            <h2>Técnica Universitaria en Programación - UTN</h2>
            <p>Hola, bienvenido a mi portafolio, soy una desarrolladora web con experienxia en el desarrollo de aplicaciones web y móviles</p>
            <ul class="containerLista">
                <li><a class="datosPersonales-img" href=""><img class="iconRedSocial" src="./icons/LinkedIn.ico" width="35rem" alt="">LinkedIn</a></li>
                <li><a class="datosPersonales-img" href=""><img class="iconRedSocial" src="./icons/GitHub.ico" width="35rem" alt="">GitHub</a></li>
                <li><a class="datosPersonales-img" href=""><img class="iconRedSocial" src="./icons/Curriculum Vitae.ico" width="35rem" alt="">Curriculum Vitae</a></li>
            </ul>
            <h3>Mi teléfono personal: +54 9 11 5617-6194</h3>
            <h3>Mi correo electrónico: anapaulariosgarin@gmail.com</h3>
            <h4>Tres de Febrero, Buenos Aires, Argentina</h4>
        </div>
    </section>
</template>

<style scoped>
h1 {
    font-size: 2.5rem;
    color: #E7E8C4;
}

h2 {
    color: #B9CA88;
}

p {
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: 1rem;
    color: #DDE5B6;
}

a {
    color: #674633;
}

.card {
    background-color: #9B8965;
    border-radius: 10px;
    padding: 10px;
    margin: 10px;
    text-align: center;
}

.containerLista{
    display: flex;
    justify-content: center;
    list-style: none;
    padding: 0;
    margin: 0;
    text-align: center;
}

.iconRedSocial {
    align-items: center;
    background-color: #6C584C;;
    border-radius: 50%;
    padding: 2px;
    margin: 5px;
    box-shadow: 0 0 5px #ADC178;
}

.iconRedSocial:hover {
    background-color: #DDE5B6;
    box-shadow: 0 0 5px #E7E8C4;
}

h1 {
    font-size: 1.2rem;
    font-weight: 600;
}

.datosPersonales-img {
    display: grid;
    margin: 10px;
    justify-items: center;
}
</style>