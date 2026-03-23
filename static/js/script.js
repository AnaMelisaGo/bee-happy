// INICIALIZACIÓN DE TOOLTIP DE BS
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));

// TIMEOUT PARA LOS MENSAJES INFORMATIVOS PARA LOS USUARIOS
document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        let messages = document.getElementById('msg');

        if (messages) {
            let alert = new bootstrap.Alert(messages);
            alert.close();
        }
    }, 4000);
    // validar el campo de suscripción en post_detail.html
    const validateSubscription = (e) => {
        e.preventDefault();
        const emailInput = document.getElementById('subscribe-email');
        const errMsg = document.getElementById('error-msg');

        const inputValue = emailInput.value;

        if (!inputValue || inputValue.indexOf('.') === -1 || inputValue.indexOf('@') === -1) {
            errMsg.innerText = 'Por favor introduzca su correo electrónico correctamente!';
            errMsg.style.color = 'red';
        } else {
            errMsg.innerText = '¡Gracias por suscribirse!';
            errMsg.style.color = '#34e334';
        }
        errMsg.style.display = 'block';
        errMsg.style.fontWeight = '600';
        errMsg.style.textShadow = '2px 0px 3px black';

        emailInput.value = '';
    }
    document.querySelector('.post-sub-form').addEventListener('submit', validateSubscription);
});

