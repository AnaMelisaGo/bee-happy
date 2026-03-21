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
});