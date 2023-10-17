// CHAMAR O INPUT COM CLICK NAS IMAGENS
let perfilContainer = document.querySelector("#perfilContainer");
let backgroundContainer = document.querySelector("#backgroundContainer");

perfilContainer.addEventListener('click', function() {
  document.getElementById('InputPerfil').click();
});

backgroundContainer.addEventListener('click', function() {
  document.getElementById('inputBanner').click();
});

// PREVIEW DA IMAGEM BANNER

document.getElementById('inputBanner').addEventListener('change', function() {
  var file = this.files[0];
  var reader = new FileReader();

  reader.onload = function(e) {
      backgroundContainer.style.backgroundImage = "url('" + e.target.result + "')";
  }

  reader.readAsDataURL(file);
});

// PREVIEW DA IMAGEM PERFIL

document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('InputPerfil').addEventListener('change', function() {
    var file = this.files[0];
    var reader = new FileReader();
  
    reader.onload = function(e) {
        perfilContainer.setAttribute('src', e.target.result);
    }
  
    reader.readAsDataURL(file);
  });
});




// SETAR O BANNER DO PERFIL

let banner = document.querySelectorAll(".banner");
let caminhoBanner = document.querySelector("#caminhoBanner");
document.addEventListener('DOMContentLoaded', function() {
  banner.forEach(element => {
    element.style.backgroundImage = "url('" + caminhoBanner.value + "')";
  });
});

// SEGUIR E DESEGUIR

function seguir(id) {
  fetch('/seguir/' + id);
}

function deseguir(id) {
  fetch('/deseguir/' + id);
}

// RETORNO VISUAL DE SEGUIR UM USUÁRIO

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

