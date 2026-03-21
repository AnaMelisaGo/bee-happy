console.log('hello');

const botones = document.querySelectorAll('.tab-btn');
const contenidos = document.querySelectorAll('.tab-content');

botones.forEach(boton => {
    boton.addEventListener('click', () => {
        botones.forEach(btn => btn.classList.remove('tab-btn-active'));
        contenidos.forEach(contenido => contenido.classList.remove('tab-active'));
        boton.classList.add('tab-btn-active');
        const target = boton.dataset.target;
        document.getElementById(target).classList.add('tab-active');
    });
});
