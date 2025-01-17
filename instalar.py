import os

# Función para crear index.html
def crear_index_html():
    html_content = '''
    <html>
    <head><title>Criptomonedas</title></head>
    <body>
        <h1>Precios de Criptomonedas</h1>
        <p id="precio_bitcoin">Cargando...</p>
        <script src="razas.js"></script>
    </body>
    </html>
    '''
    with open('index.html', 'w') as file:
        file.write(html_content)
    print("Archivo 'index.html' creado.")

# Función para crear razas.js
def crear_razas_js():
    js_content = '''
    // Script para obtener el precio de Bitcoin
    async function obtenerPrecioBitcoin() {
        const respuesta = await fetch('https://api.coindesk.com/v1/bpi/currentprice/BTC.json');
        const data = await respuesta.json();
        document.getElementById('precio_bitcoin').textContent = 'Precio de Bitcoin: ' + data.bpi.USD.rate;
    }

    obtenerPrecioBitcoin();
    '''
    with open('razas.js', 'w') as file:
        file.write(js_content)
    print("Archivo 'razas.js' creado.")

# Función para crear todo.txt
def crear_todo_txt():
    todo_content = '''
    # Todo para criptomonedas
    1. Implementar API para mostrar otros precios de criptomonedas
    2. Crear sistema de alertas cuando el precio de Bitcoin suba/baje
    '''
    with open('todo.txt', 'w') as file:
        file.write(todo_content)
    print("Archivo 'todo.txt' creado.")

# Función para crear el archivo de configuración
def crear_config():
    config_content = '''
    [configuración]
    api_key = "tu_clave_api_aquí"
    base_url = "https://api.coindesk.com/v1/"
    '''
    with open('config.txt', 'w') as file:
        file.write(config_content)
    print("Archivo 'config.txt' creado.")

# Función principal para ejecutar la instalación
def instalar():
    # Crear los archivos necesarios
    crear_index_html()
    crear_razas_js()
    crear_todo_txt()
    crear_config()

    print("Instalación completada con éxito.")

if __name__ == "__main__":
    instalar()
