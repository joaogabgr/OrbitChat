function seguir(id) {
  fetch('/seguir/' + id);
}

function deseguir(id) {
  fetch('/deseguir/' + id);
}

let btnseguir = document.querySelector(".seguir");
let qtd_seguidores = document.querySelector(".qtd_seguidores");
let userUsuario = document.querySelector(".userUsuario").innerHTML;
userUsuario = userUsuario.slice(1)
btnseguir.addEventListener("click", function() {
  btnseguir.classList.toggle("seguindo");
  if (btnseguir.classList.contains("seguindo")) {
    btnseguir.innerHTML = "Seguindo";
    qtd_seguidores.innerHTML = parseInt(qtd_seguidores.innerHTML) + 1;
    seguir(userUsuario)
  } else {
    btnseguir.innerHTML = "Seguir";
    qtd_seguidores.innerHTML = parseInt(qtd_seguidores.innerHTML) - 1;
    deseguir(userUsuario)
  }
})