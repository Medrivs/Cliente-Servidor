import socket
import threading

def recibir_mensajes(conexion):
    while True:
        try:
            mensaje = conexion.recv(1024).decode('utf-8')
            if not mensaje or mensaje.lower() == 'salir':
                print("\n[El cliente se ha desconectado]")
                break
            print(f"\nCliente dice: {mensaje}")
        except:
            break

HOST = '0.0.0.0'
PUERTO = 12345

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PUERTO))
servidor.listen(1)

print(f"Servidor iniciado. Escuchando en el puerto {PUERTO}...")
conexion, direccion = servidor.accept()
print(f"¡Conexión establecida con la IP: {direccion}!")

hilo_escucha = threading.Thread(target=recibir_mensajes, args=(conexion,))
hilo_escucha.daemon = True
hilo_escucha.start()

while True:
    try:
        respuesta = input("")
        conexion.send(respuesta.encode('utf-8'))
        if respuesta.lower() == 'salir':
            break
    except:
        break

print("Cerrando servidor...")
conexion.close()
servidor.close()
