let $departemento = document.getElementById('departamento')
let $provincia = document.getElementById('provincia')
let $distrito = document.getElementById('distrito')

let departamentos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
let provincias = ['Nota']
let distritos = ['Ponderación']


 
function mostrarLugares(arreglo, lugar) {
    let elementos = '<option selected disables>--Seleccione--</option>'

    for(let i = 0; i < arreglo.length; i++) {
        elementos += '<option value="' + arreglo[i] +'">' + arreglo[i] +'</option>'
    }

    lugar.innerHTML = elementos
}

mostrarLugares(departamentos, $departemento)

function recortar(array, inicio, fin, lugar) {
    let recortar = array.slice(inicio, fin)
    mostrarLugares(recortar, lugar)
}

$departemento.addEventListener('change', function() {
    let valor = $departemento.value

    switch(valor) {
        case 1:
            recortar(provincias, 0, 1, $provincia)
        break
        case 2:
            recortar(provincias, 2, 3, $provincia)
        break
        case 3:
            recortar(provincias, 0, 2, $provincia)
        break
        case 4:
            recortar(provincias, 0, 2, $provincia)
        break
        case 5:
            recortar(provincias, 0, 2, $provincia)
        break
        case 6:
            recortar(provincias, 0, 2, $provincia)
        break
        case 7:
            recortar(provincias, 0, 2, $provincia)
        break
        case 8:
            recortar(provincias, 0, 2, $provincia)
        break
        case 9:
            recortar(provincias, 0, 2, $provincia)
        break
        case 10:
            recortar(provincias, 0, 2, $provincia)
        break
        case 11:
            recortar(provincias, 0, 2, $provincia)
        break
        case 12:
            recortar(provincias, 0, 2, $provincia)
        break
        case 13:
            recortar(provincias, 0, 2, $provincia)
        break
    }

    $distrito.innerHTML = ''
})

$provincia.addEventListener('change', function() {
    let valor = $provincia.value

    if(valor == 'Cañete') {
        recortar(distritos, 0, 4, $distrito)
    } else if(valor == 'Huaral') {
        recortar(distritos, 4, 7, $distrito)
    } else {
        recortar(distritos, 7, 9, $distrito)
    }
})