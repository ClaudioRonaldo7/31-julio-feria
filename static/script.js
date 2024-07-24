let mostrador = document.getElementById("mostrador")
let seleccion = document.getElementById("seleccion")
let imgSeleccionada = document.getElementById("img")
let modeloSeleccionado = document.getElementById("modelo")
let descripSeleccionada = document.getElementById("descripcion")
let precioSeleccionado = document.getElementById("precio")

//funcion que carga la info de los item seleccionado
function cargar(item) {
    quitarbordes();
    mostrador.style.width = "100%";/*mostrador hacia la derecha*/
    seleccion.style.width = "40%";
    seleccion.style.opacity = "1";
    item.style.border = "2px solid red";

    imgSeleccionada.src = item.getElementsByTagName("img")[0].src;

    modeloSeleccionado.innerHTML = item.getElementsByTagName("p")[0].innerHTML;

    descripSeleccionada.innerHTML = "Descripcion Del Modelo";

    precioSeleccionado.innerHTML = item.getElementsByTagName("span")[0].innerHTML
}
function quitarbordes() {
    var items = document.getElementsByClassName("item");
    for (i = 0; i < items.length; i++) {
        items[i].style.border = "none";
    }
}

function cerrar() {
    mostrador.style.width = "100%";
    seleccion.style.width = "0";
    seleccion.style.opacity = "0";
    quitarbordes();
}
//Carrito de compras
//var
let allContainerCart = document.querySelector('.item');

let buyThings = [];
//funcion
loadEventListenrs();
function loadEventListenrs(){
    allContainerCart.addEventListener('click', AgregarAlCarrito);
}
function AgregarAlCarrito(e){
    e.preventDefault();
    if (e.target.classList.contains('AgregarAlCarrito')){
        console.log (e.target.parentElements);
        const selectProduct = e.target 
        readTheContent('selectProduct');
        //console.log(e.target.parentElements);
    }
}
function readTheContent(product){
    const infoProduct = {
        image: product.querySelector('.contenedor-foto img').src,
        title: product.querySelector('descripcion').textContent,
        price: product.querySelector('.contenedor-foto span'),
        id: product.querySelector('a').getAttribute('AgregarAlCarrito'),
        amount: 1
    }

    buyThings = [...buyThings, infoProduct]
    loadHtml();
    console.log(infoProduct);
}

function loadHtml(){
    buyThings.forEach(product =>{
        const {image, title, price, amount, id} = product;
        const row = document.createElement('div');
        row.classList.add('contenedor-foto')
        row.innerHTML = `
        img src="${image}" alt=""><!--aca cambias las imagenes-->
                            <h3 class="description">${title}</h3>
                            <p>Zapatillas para Mujer</p>
                            <span class="precio-lanz">${price}</span>
        `;
    });
}