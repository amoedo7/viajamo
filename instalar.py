def crear_index_html():
    html_content = '''
    <html>
    <head><title>Gestión de Billetera Cripto</title></head>
    <body>
        <h1>Introduce tu Frase Semilla o Clave Privada</h1>
        <form id="walletForm">
            <label for="clave">Frase Semilla o Clave Privada:</label><br>
            <input type="text" id="clave" name="clave" required><br><br>
            <button type="submit">Procesar</button>
        </form>
        <p id="resultado"></p>
        <script src="script.js"></script>
    </body>
    </html>
    '''
    with open('index.html', 'w') as file:
        file.write(html_content)
    print("Archivo 'index.html' creado.")

def crear_script_js():
    js_content = '''
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
    '''
    with open('script.js', 'w') as file:
        file.write(js_content)
    print("Archivo 'script.js' creado.")

def crear_config_txt():
    config_content = '''
    [configuración]
    clave_secreta = "Tu_clave_secreta_aquí"
    '''
    with open('config.txt', 'w') as file:
        file.write(config_content)
    print("Archivo 'config.txt' creado.")

def crear_todo_txt():
    todo_content = '''
    1. Implementar validación segura para la clave privada.
    2. Añadir funcionalidad para realizar transacciones o solucionar problemas de billeteras.
    3. Asegurarse de que las claves no se almacenen en texto plano.
    '''
    with open('todo.txt', 'w') as file:
        file.write(todo_content)
    print("Archivo 'todo.txt' creado.")

def instalar():
    # Crear los archivos necesarios
    crear_index_html()
    crear_script_js()
    crear_config_txt()
    crear_todo_txt()
    print("Instalación completada con éxito.")

if __name__ == "__main__":
    instalar()
