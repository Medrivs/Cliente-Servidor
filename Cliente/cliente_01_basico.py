import socket

IP_DEL_SERVIDOR = '192.168.1.25' 
PUERTO = 12345

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print(f"Conectando al servidor en {IP_DEL_SERVIDOR}...")
    cliente.connect((IP_DEL_SERVIDOR, PUERTO))
    
    mensaje = "¡Hola Servidor! Misión cumplida, logramos comunicarnos."
    cliente.send(mensaje.encode('utf-8'))
    print("¡Mensaje enviado con éxito!")
    
except Exception as e:
    print(f"Error al conectar: {e}")

cliente.close()
