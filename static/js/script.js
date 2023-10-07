function ajustarTamanho(element) {
    element.style.height = "1px";
    element.style.height = (25+element.scrollHeight)+"px";
  }

let btnEditarPerfil = document.querySelector(".btnEditarPerfil");
let secEditarPerfil = document.querySelector(".secEditarPerfil");
let closeEditarPerfil = document.querySelector(".closeEditarPerfil");

btnEditarPerfil.addEventListener("click", function() {
  secEditarPerfil.classList.toggle("ativar");
})

closeEditarPerfil.addEventListener("click", function() {
  secEditarPerfil.classList.toggle("ativar");
})