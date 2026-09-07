import socket

HOST = '0.0.0.0'
PUERTO = 12345

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PUERTO))
servidor.listen(1)

print(f"Servidor iniciado y escuchando en el puerto {PUERTO}...")

conexion, direccion = servidor.accept()
print(f"¡Conexión establecida con la IP: {direccion}!")

while True:
    mensaje_cliente = conexion.recv(1024).decode('utf-8')
    
    if mensaje_cliente.lower() == 'salir':
        print("El cliente ha cerrado el chat.")
        break
        
    print(f"Cliente dice: {mensaje_cliente}")

    respuesta = input("Tú (Servidor): ")
    conexion.send(respuesta.encode('utf-8'))
    
    if respuesta.lower() == 'salir':
        break

print("Cerrando servidor...")
conexion.close()
servidor.close()
