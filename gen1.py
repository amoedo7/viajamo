import json

# Cargar las razas desde el archivo JSON
def cargar_razas():
    try:
        with open("razas.json", "r") as archivo:
            razas = json.load(archivo)
            return razas["razas"]
    except FileNotFoundError:
        print("No se encontró el archivo de razas.")
        return []

# Generar el archivo HTML con la lista de razas
def generar_html():
    razas = cargar_razas()
    if not razas:
        print("No hay razas para mostrar.")
        return
    
    # Abrir archivo HTML en modo escritura
    with open("razas.html", "w") as archivo_html:
        archivo_html.write("<!DOCTYPE html>\n")
        archivo_html.write("<html lang='es'>\n")
        archivo_html.write("<head>\n")
        archivo_html.write("<meta charset='UTF-8'>\n")
        archivo_html.write("<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
        archivo_html.write("<title>Razas Alienígenas</title>\n")
        archivo_html.write("</head>\n")
        archivo_html.write("<body>\n")
        archivo_html.write("<h1>Lista de Razas Alienígenas</h1>\n")
        archivo_html.write("<ul>\n")
        
        # Escribir los nombres de las razas en una lista de enlaces
        for raza in razas:
            archivo_html.write(f"<li><a href='descripcion.html?raza={raza['nombre']}'>{raza['nombre']}</a></li>\n")
        
        archivo_html.write("</ul>\n")
        archivo_html.write("</body>\n")
        archivo_html.write("</html>\n")

    print("Archivo HTML generado correctamente.")

# Llamar a la función para generar el HTML
if __name__ == "__main__":
    generar_html()
