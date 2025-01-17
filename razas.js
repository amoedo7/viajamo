
    // Script para obtener el precio de Bitcoin
    async function obtenerPrecioBitcoin() {
        const respuesta = await fetch('https://api.coindesk.com/v1/bpi/currentprice/BTC.json');
        const data = await respuesta.json();
        document.getElementById('precio_bitcoin').textContent = 'Precio de Bitcoin: ' + data.bpi.USD.rate;
    }

    obtenerPrecioBitcoin();
    