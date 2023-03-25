function validar() {
  var nombre = document.getElementById("nombre").value;
  var email = document.getElementById("email").value;
  var mensaje = document.getElementById("mensaje").value;

  if (nombre == "" || email == "" || mensaje == "") {
    alert("Por favor complete todos los campos");
    return false;
  }

  if (!email.includes("@")) {
    alert("Por favor ingrese un correo electrónico válido");
    return false;
  }

  return true;
}

function calcularPrecio() {
  var origen = document.getElementById("origen").value;
  var destino = document.getElementById("destino").value;
  var precio = 0;

  if (origen == "dinamarca" && destino == "peru") {
    precio = 2000;
  } else if (origen == "alemania" && destino == "colombia") {
    precio = 1800;
  } else if (origen == "espana" && destino == "argentina") {
    precio = 2200;
  } else {
    precio = 2500;
  }

  document.getElementById("precio").innerHTML = "$" + precio;
}
