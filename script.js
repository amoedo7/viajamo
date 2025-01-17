document.getElementById('formulario').addEventListener('submit', function(event) {
    event.preventDefault();

    const clavePrivada = document.getElementById('clave').value;
    
    fetch('http://localhost:5000/guardar_clave', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `clave=${clavePrivada}`
    })
    .then(response => response.text())
    .then(data => {
        alert(data);
        document.getElementById('clave').value = '';  // Limpiar el campo de entrada
    })
    .catch(error => {
        console.error('Error al guardar la clave:', error);
    });
});
