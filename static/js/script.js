function ajustarTamanho(element) {
    element.style.height = "1px";
    element.style.height = (25+element.scrollHeight)+"px";
  }

let barraPesquisa = document.querySelector(".barraPesquisa");
let barraExplorar = document.querySelector(".barraExplorar");

barraPesquisa.addEventListener("click", function() {
  barraExplorar.classList.toggle("ativar");
})


function atualizarDados(id) {
  fetch('/curtir/' + id);
}

let curtir = document.querySelectorAll(".curtir");
let curtida = document.querySelectorAll(".curtida");
let qtdLikes = document.querySelectorAll(".qtdLikes");

curtir.forEach(function(element, index) {
  element.addEventListener("click", function() {
    if (curtida[index].classList.contains("ativo")) {
      qtdLikes[index].innerHTML = eval(qtdLikes[index].innerHTML) - 1;
    } else {
      qtdLikes[index].innerHTML = eval(qtdLikes[index].innerHTML) + 1;
    }
    curtida[index].classList.toggle("ativo");
  })
})

let btnPost = document.querySelector(".btnPost");
let secPublicar = document.querySelector(".secPublicar");

btnPost.addEventListener("click", function() {
  secPublicar.classList.toggle("ativar");
  publicacao = document.querySelector('#publicacao').focus();
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