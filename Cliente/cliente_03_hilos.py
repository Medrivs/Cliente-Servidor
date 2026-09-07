import socket
import threading

def recibir_mensajes(cliente):
    while True:
        try:
            mensaje = cliente.recv(1024).decode('utf-8')
            if not mensaje or mensaje.lower() == 'salir':
                print("\n[El servidor ha cerrado el chat]")
                break
            print(f"\nServidor dice: {mensaje}")
        except:
            break

IP_DEL_SERVIDOR = '192.168.1.25'
PUERTO = 12345

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    cliente.connect((IP_DEL_SERVIDOR, PUERTO))
    print("¡Conectado al chat de hilos libres! Escribe 'salir' para terminar.\n")
    
    hilo_escucha = threading.Thread(target=recibir_mensajes, args=(cliente,))
    hilo_escucha.daemon = True
    hilo_escucha.start()

    while True:
        mensaje = input("")
        cliente.send(mensaje.encode('utf-8'))
        if mensaje.lower() == 'salir':
            break
            
except Exception as e:
    print(f"Error al conectar: {e}")

print("Desconectado.")
cliente.close()
