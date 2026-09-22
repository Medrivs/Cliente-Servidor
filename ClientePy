import socket
import threading
import sys

def recibir_mensajes(cliente_socket):
    while True:
        try:
            data = cliente_socket.recv(1024)
            if not data:
                print("\nEl servidor cerró la conexión.")
                break
            mensaje = data.decode('utf-8')
            print(f"\nOtro: {mensaje.strip()}", end="\n> ")
        except Exception:
            break

def main():
    HOST = '192.168.218.150'  # Reemplaza por la IP del servidor si están en máquinas distintas
    PORT = 81

    # Pedir el nombre antes de conectar
    nombre_usuario = input("Ingresa tu nombre de usuario: ").strip()

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        cliente.connect((HOST, PORT))
        print("Conectado al servidor.")

        # Inicia el hilo secundario para escuchar mensajes
        hilo_recepcion = threading.Thread(target=recibir_mensajes, args=(cliente,), daemon=True)
        hilo_recepcion.start()

        # Hilo principal para enviar mensajes
        while True:
            mensaje = input("> ")
            if mensaje.strip():
                if mensaje.lower() == "salir":
                    # Avisa que te desconectas y sale
                    cliente.sendall(f"{nombre_usuario} se ha desconectado.\n".encode('utf-8'))
                    print("Cerrando conexión...")
                    break
                else:
                    # Formato EXACTO de tu compañero (Nombre:mensaje)
                    mensaje_formateado = f"{nombre_usuario}:{mensaje}\n"
                    cliente.sendall(mensaje_formateado.encode('utf-8'))

    except ConnectionRefusedError:
        print("Error: No se pudo conectar al servidor. Asegúrate de que el servidor esté activo.")
    finally:
        cliente.close()
        sys.exit()

if __name__ == "__main__":
    main()
