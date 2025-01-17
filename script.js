
    document.getElementById("walletForm").addEventListener("submit", function(event){
        event.preventDefault();  // Evitar el envío del formulario
        const clave = document.getElementById("clave").value;
        
        if (clave) {
            // Aquí iría el proceso para validar o usar la clave
            document.getElementById("resultado").textContent = "Frase Semilla o Clave Privada ingresada: " + clave;
        } else {
            document.getElementById("resultado").textContent = "Por favor ingresa una frase semilla o clave privada.";
        }
    });
    