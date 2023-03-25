import requests
import json

# Información del repositorio
username = 'amoedo7'
repository = 'viajamo'
token = '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'

# Información del archivo
filename = input('Ingrese el nombre del archivo: ')
filepath = input('Ingrese la ruta del archivo: ')
filecontent = open(filepath, 'rb').read()

# Agregar archivo al repositorio
url = f'https://api.github.com/repos/{username}/{repository}/contents/{filename}'
headers = {'Authorization': f'token {token}'}
payload = {
    'message': 'Agregando archivo ' + filename,
    'content': filecontent.decode('utf-8')
}
response = requests.put(url=url, headers=headers, data=json.dumps(payload))
if response.status_code == 201:
    print(f'El archivo {filename} se ha agregado correctamente al repositorio')
else:
    print(f'Error al agregar el archivo {filename} al repositorio. Código de estado HTTP: {response.status_code}')

# Realizar commit en el repositorio
url = f'https://api.github.com/repos/{username}/{repository}/git/commits'
payload = {
    'message': 'Agregando archivo ' + filename,
    'content': filecontent.decode('utf-8')
}
response = requests.post(url=url, headers=headers, data=json.dumps(payload))
if response.status_code == 201:
    print('Se ha creado el commit correctamente en el repositorio')
else:
    print(f'Error al crear el commit en el repositorio. Código de estado HTTP: {response.status_code}')
