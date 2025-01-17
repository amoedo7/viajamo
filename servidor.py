from flask import Flask, request
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
