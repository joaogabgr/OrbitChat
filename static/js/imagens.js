let imagem = document.querySelectorAll("#imagem")
imagem.forEach(element => {
    element.onerror = function () {
        element.src = "../static/img/perfil.svg";
    };
});