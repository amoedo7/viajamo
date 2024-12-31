#!/bin/bash

# Crear una nueva carpeta para el proyecto
mkdir audio-player
cd audio-player

# Crear el archivo index.html
cat > index.html <<EOL
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reproductor de Audio</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="audio-container">
        <h1>Reproductor de Audio</h1>
        <audio id="audioPlayer" controls>
            <source src="your-audio-file.mp3" type="audio/mp3">
            Tu navegador no soporta el elemento de audio.
        </audio>
        <br>
        <button id="playPauseBtn">Reproducir/Pausar</button>
    </div>
    <script src="app.js"></script>
</body>
</html>
EOL

# Crear el archivo style.css
cat > style.css <<EOL
body {
    font-family: Arial, sans-serif;
    text-align: center;
    background-color: #f4f4f4;
    padding: 20px;
}

.audio-container {
    background-color: #222;
    padding: 30px;
    border-radius: 10px;
    display: inline-block;
    color: white;
}

audio {
    width: 100%;
    margin-top: 10px;
}

button {
    background-color: #007BFF;
    color: white;
    border: none;
    padding: 10px 20px;
    margin-top: 15px;
    cursor: pointer;
    border-radius: 5px;
}

button:hover {
    background-color: #0056b3;
}
EOL

# Crear el archivo app.js
cat > app.js <<EOL
const audioPlayer = document.getElementById('audioPlayer');
const playPauseBtn = document.getElementById('playPauseBtn');

playPauseBtn.addEventListener('click', () => {
    if (audioPlayer.paused) {
        audioPlayer.play();
        playPauseBtn.textContent = "Pausar";
    } else {
        audioPlayer.pause();
        playPauseBtn.textContent = "Reproducir";
    }
});
EOL

# Confirmar la creación de los archivos
echo "Archivos creados con éxito: index.html, style.css, app.js"
