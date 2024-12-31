#!/bin/bash

echo "Eliminando archivos antiguos..."

# Eliminar archivos existentes
rm index.html app.js style.css

echo "Creando index.html..."
cat <<EOL > index.html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Creación de Avatar IA</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body { margin: 0; overflow: hidden; font-family: Arial, sans-serif; background-color: #111; color: white; }
        #avatarCanvas { display: block; width: 100%; height: 100vh; }
        .container { position: absolute; top: 20px; left: 20px; z-index: 1; }
        .button { padding: 10px; background-color: #007BFF; color: white; border: none; cursor: pointer; }
        .button:hover { background-color: #0056b3; }
        input[type="file"] { margin: 10px 0; }
    </style>
</head>
<body>
    <div class="container">
        <h1>¡Crea tu Avatar IA!</h1>
        <input type="file" id="fileInput" accept="image/*" onchange="loadImage(event)">
        <br>
        <button class="button" onclick="createAvatar()">Crear Avatar</button>
    </div>

    <canvas id="avatarCanvas"></canvas>

    <script src="app.js"></script>
</body>
</html>
EOL

echo "Creando app.js..."
cat <<EOL > app.js
let scene, camera, renderer, avatar;
let textureLoader = new THREE.TextureLoader();

function init() {
    // Crear la escena
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    renderer = new THREE.WebGLRenderer({ canvas: document.getElementById("avatarCanvas") });
    renderer.setSize(window.innerWidth, window.innerHeight);

    // Crear un cubo simple como avatar
    let geometry = new THREE.BoxGeometry(1, 2, 1);
    let material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
    avatar = new THREE.Mesh(geometry, material);
    scene.add(avatar);

    // Posición de la cámara
    camera.position.z = 5;

    animate();
}

function animate() {
    requestAnimationFrame(animate);
    avatar.rotation.x += 0.01;
    avatar.rotation.y += 0.01;
    renderer.render(scene, camera);
}

// Función para cargar la imagen en el avatar
function loadImage(event) {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = function(e) {
        const texture = textureLoader.load(e.target.result);
        avatar.material.map = texture;
        avatar.material.needsUpdate = true;
    };
    reader.readAsDataURL(file);
}

// Función para crear y personalizar el avatar
function createAvatar() {
    // Aquí puedes agregar más personalizaciones, como cambiar ropa, peinado, etc.
    console.log("Avatar creado");
}

init();
EOL

echo "Creando style.css..."
cat <<EOL > style.css
body { margin: 0; overflow: hidden; font-family: Arial, sans-serif; background-color: #111; color: white; }
#avatarCanvas { display: block; width: 100%; height: 100vh; }
.container { position: absolute; top: 20px; left: 20px; z-index: 1; }
.button { padding: 10px; background-color: #007BFF; color: white; border: none; cursor: pointer; }
.button:hover { background-color: #0056b3; }
input[type="file"] { margin: 10px 0; }
EOL

echo "Archivos actualizados exitosamente."

# Leer el token desde el archivo
TOKEN=$(cat ~/token.txt)

# Configurar el URL remoto de Git usando el token
git remote set-url origin https://$TOKEN@github.com/amoedo7/viajamo.git

# Cambiar a la rama `latest_brunch`
git checkout latest_brunch

# Ejecución de git
git status
git add .
git commit -m "Página de creación de Avatar IA con 3D funcional"
git push origin latest_brunch

echo "¡Cambios empujados exitosamente a la rama latest_brunch!"
