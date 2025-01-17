# Crear los archivos necesarios para la página

# Crear index.html
def crear_index_html():
    html_content = '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ingreso de clave privada</title>
    </head>
    <body>
        <h1>Ingrese su clave privada</h1>
        <form id="claveForm">
            <input type="password" id="clavePrivada" placeholder="Ingrese su clave privada" required>
            <button type="submit">Guardar</button>
        </form>

        <script src="razas.js"></script>
    </body>
    </html>
    '''
    with open('index.html', 'w') as file:
        file.write(html_content)
    print("Archivo 'index.html' creado.")

# Crear razas.js (para manejar el almacenamiento de la clave)
def crear_razas_js():
    js_content = '''
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
    '''
    with open('razas.js', 'w') as file:
        file.write(js_content)
    print("Archivo 'razas.js' creado.")

# Crear un archivo de tareas pendientes (todo.txt)
def crear_todo_txt():
    todo_content = '''
    # Todo para la página de claves
    1. Implementar función para encriptar la clave antes de almacenarla
    2. Crear un sistema de autenticación para asegurar el acceso
    '''
    with open('todo.txt', 'w') as file:
        file.write(todo_content)
    print("Archivo 'todo.txt' creado.")

# Crear el archivo de configuración
def crear_config():
    config_content = '''
    [configuración]
    api_key = "tu_clave_api_aquí"
    base_url = "https://api.coindesk.com/v1/"
    '''
    with open('config.txt', 'w') as file:
        file.write(config_content)
    print("Archivo 'config.txt' creado.")

# Función principal que ejecuta la instalación
def instalar():
    # Crear los archivos necesarios
    crear_index_html()
    crear_razas_js()
    crear_todo_txt()
    crear_config()
    
    print("Instalación completada con éxito.")

# Ejecutar la instalación si es el script principal
if __name__ == "__main__":
    instalar()
