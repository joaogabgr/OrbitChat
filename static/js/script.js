function ajustarTamanho(element) {
    element.style.height = "1px";
    element.style.height = (25+element.scrollHeight)+"px";
  }

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

// DAR SUBMIT NO FORM DE PESQUISA 

let formExplorar = document.querySelector("#formExplorar");
let pesquisa = document.querySelector("#pesquisa");
let btnExplorar = document.querySelector(".btnExplorar");
let btnTeste = document.querySelector(".btnTeste");

btnTeste.addEventListener("click", function() {
  formExplorar.classList.toggle("ativar");
  pesquisa.focus();
  btnTeste.classList.toggle("ocultar");
})

btnExplorar.addEventListener("click", function() {
  formExplorar.submit();
})

// ATIVAR O FOCUS QUANDO O FORM ABRIR

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