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
