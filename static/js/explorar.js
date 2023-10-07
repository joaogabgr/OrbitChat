let filtroUsuario = document.querySelector(".filtroUsuario");
let filtroComentario = document.querySelector(".filtroComentario");

let secUsuario = document.querySelector(".secUsuario");
let secComentarios = document.querySelector(".secComentarios");

let faFiltroUsuario = document.querySelector(".faFiltroUsuario");
let faFiltroComentario = document.querySelector(".faFiltroComentario");

filtroUsuario.addEventListener("click", () => {
    secUsuario.classList.toggle("oculto");
    faFiltroUsuario.classList.toggle("fa-xmark");
    faFiltroUsuario.classList.toggle("fa-check");
})

filtroComentario.addEventListener("click", function () {
    secComentarios.classList.toggle("oculto");
    faFiltroComentario.classList.toggle("fa-xmark");
    faFiltroComentario.classList.toggle("fa-check");
})