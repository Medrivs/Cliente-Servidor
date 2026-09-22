const net = require('net');
const readline = require('readline');

// Configuración de la conexión
const PORT = 81; 
const HOST = '192.168.218.150'; 
const MI_NOMBRE = 'Rivassss'; // <-- ¡PON TU NOMBRE AQUÍ!

const cliente = new net.Socket();

// Interfaz para leer lo que escribes en la consola
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// 1. Intentar conectar al servidor
cliente.connect(PORT, HOST, () => {
    console.log(`¡Conectado exitosamente al servidor Java en ${HOST}:${PORT}!`);
    console.log("Escribe tu mensaje y presiona Enter (Escribe 'salir' para terminar).\n");
    rl.prompt(); // Muestra el cursor para escribir
});

// 2. Escuchar los mensajes que manda el Servidor (Java)
cliente.on('data', (data) => {
    // Solo imprimimos los datos tal cual llegan, sin ponerle "Servidor Java dice:"
    console.log(`\n${data.toString().trim()}`);
    rl.prompt();
});
// 3. Leer lo que tú escribes y enviarlo
rl.on('line', (linea) => {
    if (linea.toLowerCase() === 'salir') {
        cliente.write(`${MI_NOMBRE} se ha desconectado.\n`); // Avisamos a los demás
        console.log("Cerrando la conexión...");
        cliente.destroy();
        process.exit(0);
    } else {
        // ¡LA NUEVA MAGIA AQUÍ! 
        // Juntamos tu nombre, dos puntos, tu mensaje y el salto de línea
        cliente.write(`${MI_NOMBRE}:${linea}\n`);
        rl.prompt();
    }
});

// 4. Manejo de errores o desconexiones
cliente.on('close', () => {
    console.log('\n[Conexión cerrada por el servidor]');
    process.exit(0);
});

cliente.on('error', (err) => {
    console.log(`\nError de conexión: Verifica que el servidor Java esté encendido y la IP sea correcta.\nDetalle: ${err.message}`);
    process.exit(1);
});