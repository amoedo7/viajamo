import os
import subprocess

# Función para instalar Flask si no está instalado
def instalar_flask():
    try:
        subprocess.check_call([os.sys.executable, "-m", "pip", "install", "flask"])
    except subprocess.CalledProcessError:
        print("Error al instalar Flask. Por favor, intentalo manualmente.")
        exit(1)

# Función para crear el servidor Python básico
def crear_servidor():
    servidor_code = '''from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/guardar_clave', methods=['POST'])
def guardar_clave():
    clave_privada = request.form.get('clave')
    if clave_privada:
        with open('clave_privada.txt', 'w') as file:
            file.write(clave_privada)
        return "Clave privada guardada con éxito", 200
    return "No se recibió la clave", 400

if __name__ == '__main__':
    if not os.path.exists('clave_privada.txt'):
        with open('clave_privada.txt', 'w') as f:
            f.write('')

    app.run(host='0.0.0.0', port=5000)
'''

    with open('servidor.py', 'w') as f:
        f.write(servidor_code)
    
    print("Servidor Python 'servidor.py' creado con éxito.")

# Función para crear el archivo HTML
def crear_html():
    html_code = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guardar Clave</title>
</head>
<body>
    <h1>Guardar Clave Privada</h1>
    <form id="claveForm">
        <label for="clavePrivada">Ingresa tu clave privada:</label><br>
        <input type="text" id="clavePrivada" name="clavePrivada" required><br><br>
        <button type="submit">Guardar Clave</button>
    </form>

    <script>
        document.getElementById('claveForm').addEventListener('submit', function(e) {
            e.preventDefault();
            const clavePrivada = document.getElementById('clavePrivada').value;
            if (clavePrivada) {
                fetch('http://localhost:5000/guardar_clave', {
                    method: 'POST',
                    body: new URLSearchParams({ 'clave': clavePrivada }),
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
                })
                .then(response => response.text())
                .then(data => alert("Clave privada almacenada: " + data))
                .catch(error => alert("Error al almacenar la clave: " + error));
            } else {
                alert("Por favor ingrese una clave.");
            }
        });
    </script>
</body>
</html>'''

    with open('index.html', 'w') as f:
        f.write(html_code)
    
    print("Archivo HTML 'index.html' creado con éxito.")

# Función para crear el archivo de configuración (config.txt)
def crear_config():
    config_code = '''# Configuración de la aplicación

# Dirección del servidor donde se almacenan las claves privadas
SERVER_URL = "http://localhost:5000/guardar_clave"'''

    with open('config.txt', 'w') as f:
        f.write(config_code)
    
    print("Archivo de configuración 'config.txt' creado con éxito.")

# Función principal
def main():
    print("Iniciando instalación...")

    # Instalar Flask
    instalar_flask()

    # Crear los archivos necesarios
    crear_servidor()
    crear_html()
    crear_config()

    print("Instalación completada con éxito.")
    print("Puedes iniciar el servidor ejecutando 'python3 servidor.py'.")
    print("La página web 'index.html' se puede abrir en tu navegador.")

if __name__ == '__main__':
    main()
