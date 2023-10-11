function ajustarTamanho(element) {
    element.style.height = "1px";
    element.style.height = (25+element.scrollHeight)+"px";
  }

let barraPesquisa = document.querySelector(".barraPesquisa");
let barraExplorar = document.querySelector(".barraExplorar");

barraPesquisa.addEventListener("click", function() {
  barraExplorar.classList.toggle("ativar");
})

let btnPost = document.querySelector(".btnPost");
let secPublicar = document.querySelector(".secPublicar");

btnPost.addEventListener("click", function() {
  secPublicar.classList.toggle("ativar");
})

let btnEditarPerfil = document.querySelector(".btnEditarPerfil");
let secEditarPerfil = document.querySelector(".secEditarPerfil");
let closeEditarPerfil = document.querySelector(".closeEditarPerfil");

btnEditarPerfil.addEventListener("click", function() {
  secEditarPerfil.classList.toggle("ativar");
})

closeEditarPerfil.addEventListener("click", function() {
  secEditarPerfil.classList.toggle("ativar");
})