import socket

HOST = '0.0.0.0'
PUERTO = 12345

print("Iniciando servidor...")
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PUERTO))
servidor.listen(1)

print(f"Servidor listo y escuchando en el puerto {PUERTO}...")

conexion, direccion = servidor.accept()
print(f"¡Conexión establecida con la IP: {direccion}!")

mensaje_recibido = conexion.recv(1024).decode('utf-8')
print(f"MENSAJE RECIBIDO: {mensaje_recibido}")

conexion.close()
servidor.close()
