import json

# Función para cargar las razas existentes desde el archivo JSON
def cargar_razas():
    try:
        with open("razas.json", "r") as archivo:
            razas = json.load(archivo)
            return razas["razas"]
    except FileNotFoundError:
        print("No se encontró el archivo razas.json, se creará uno nuevo.")
        return []

# Función para guardar las razas actualizadas en el archivo JSON
def guardar_razas(razas):
    with open("razas.json", "w") as archivo:
        json.dump({"razas": razas}, archivo, indent=4)

# Función para agregar una raza al archivo JSON si no existe
def agregar_raza(razas, nombre, descripcion):
    # Verificar si la raza ya está en la lista
    if not any(raza['nombre'].lower() == nombre.lower() for raza in razas):
        razas.append({"nombre": nombre, "descripcion": descripcion})
        print(f"Raza '{nombre}' agregada.")
    else:
        print(f"La raza '{nombre}' ya existe, no se agregó.")

# Función para procesar el archivo cargar.txt y agregar las razas
def procesar_archivo():
    razas = cargar_razas()

    # Leer el archivo cargar.txt
    with open("cargar.txt", "r") as archivo_txt:
        lineas = archivo_txt.readlines()

    # Procesar cada línea del archivo
    for linea in lineas:
        # Limpiar la línea y separar el nombre y la descripción
        linea = linea.strip()
        if ":" in linea:
            nombre, descripcion = linea.split(":", 1)
            agregar_raza(razas, nombre.strip(), descripcion.strip())

    # Guardar las razas actualizadas en el archivo JSON
    guardar_razas(razas)

if __name__ == "__main__":
    procesar_archivo()
