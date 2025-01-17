
    document.getElementById('claveForm').addEventListener('submit', function(e) {
        e.preventDefault();  // Evitar que el formulario se envíe

        const clavePrivada = document.getElementById('clavePrivada').value;
        
        if (clavePrivada) {
            // Almacenamos la clave de forma temporal en el localStorage
            localStorage.setItem('clavePrivada', clavePrivada);
            alert("Clave privada almacenada temporalmente.");
        } else {
            alert("Por favor ingrese una clave.");
        }
    });
    