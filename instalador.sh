#!/bin/bash
# Script de instalación para Apuestas Rápidas

# Obtener la ruta absoluta del directorio donde se ejecuta el script
INSTALL_DIR="$(pwd)"

echo "Iniciando instalación en $INSTALL_DIR..."

# Verificar si estamos dentro de una carpeta llamada "viajamo"
if [[ "$(basename "$INSTALL_DIR")" == "viajamo" ]]; then
    echo "Instalando archivos en la carpeta viajamo..."
else
    echo "Error: Debes ejecutar este script dentro de la carpeta viajamo."
    exit 1
fi

# Crear index.html si no existe en la carpeta actual
if [ ! -f "$INSTALL_DIR/index.html" ]; then
    echo "Creando index.html..."
    cat > "$INSTALL_DIR/index.html" <<EOL
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Crear Deal - Apuestas Rápidas</title>
</head>
<body>
  <h1>Crear Deal</h1>
  <form id="dealForm">
    <label for="monto">Monto de Deals:</label>
    <input type="number" id="monto" name="monto" required>
    <br><br>
    <button type="submit">Generar Deal</button>
  </form>

  <script>
    document.getElementById('dealForm').addEventListener('submit', function(e) {
      e.preventDefault();
      const monto = document.getElementById('monto').value;
      const jugador = "Faker";
      const url = \`apostar.html?jugador=\${encodeURIComponent(jugador)}&monto=\${encodeURIComponent(monto)}\`;
      window.location.href = url;
    });
  </script>
</body>
</html>
EOL
fi

# Crear apostar.html si no existe en la carpeta actual
if [ ! -f "$INSTALL_DIR/apostar.html" ]; then
    echo "Creando apostar.html..."
    cat > "$INSTALL_DIR/apostar.html" <<EOL
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Apostar - Apuestas Rápidas</title>
</head>
<body>
  <h1>Detalles del Deal</h1>
  <div id="dealInfo"></div>
  <br>
  <button id="apuestaAFavor">Apostar a Favor</button>
  <button id="apuestaEnContra">Apostar en Contra</button>

  <script>
    function getQueryParams() {
      const params = {};
      const search = window.location.search.substring(1);
      if (search) {
        search.split('&').forEach(function(part) {
          const item = part.split('=');
          params[decodeURIComponent(item[0])] = decodeURIComponent(item[1]);
        });
      }
      return params;
    }

    const params = getQueryParams();
    const jugador = params.jugador || "Desconocido";
    const monto = params.monto || "0";

    document.getElementById('dealInfo').innerHTML = \`<p>Jugador: \${jugador}</p><p>Monto: \${monto}</p>\`;

    document.getElementById('apuestaAFavor').addEventListener('click', function() {
      alert(\`Has apostado a favor del deal de \${jugador} con monto \${monto}.\`);
    });

    document.getElementById('apuestaEnContra').addEventListener('click', function() {
      alert(\`Has apostado en contra del deal de \${jugador} con monto \${monto}.\`);
    });
  </script>
</body>
</html>
EOL
fi

# Eliminar carpeta extra "viajamo" si existe
if [ -d "$INSTALL_DIR/viajamo" ]; then
    echo "Eliminando carpeta innecesaria viajamo..."
    rm -rf "$INSTALL_DIR/viajamo"
fi

echo "Instalación completada en $INSTALL_DIR. Ahora puedes abrir index.html en tu navegador."
