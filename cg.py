def guardar_en_archivo(texto):
    # Guardar el texto en el archivo 'cargar.txt', agregando al final
    with open('cargar.txt', 'a') as archivo:  # Usar 'a' para agregar al final
        archivo.write("\n")  # Agregar una línea en blanco antes de las nuevas entradas (opcional)
        
        # Procesar el texto línea por línea
        lineas = texto.strip().split('\n')
        for linea in lineas:
            nombre, descripcion = linea.split(": ", 1)
            archivo.write(f"{nombre}: {descripcion}\n")  # Escribir cada raza y su descripción

    print("Datos guardados exitosamente en cargar.txt.")

def main():
    # Mostrar mensaje para ingresar texto
    print("¿Qué vas a agregar? Ingresa las razas con su descripción, separadas por una línea.")
    print("Ejemplo de entrada:")
    print("Greys: Extraterrestres pequeños, de piel gris, cabezas grandes y ojos negros.")
    
    # Leer la entrada del usuario
    texto_entrada = ""
    while True:
        linea = input("Introduce una raza y su descripción (o presiona Enter para finalizar): ")
        if not linea:
            break  # Termina cuando el usuario presiona Enter sin escribir nada
        texto_entrada += linea + "\n"
    
    # Llamar a la función para guardar los datos en 'cargar.txt'
    guardar_en_archivo(texto_entrada)

if __name__ == "__main__":
    main()
