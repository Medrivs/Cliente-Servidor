import socket

IP_DEL_SERVIDOR = '192.168.1.25' 
PUERTO = 12345

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print(f"Conectando al servidor en {IP_DEL_SERVIDOR}...")
    cliente.connect((IP_DEL_SERVIDOR, PUERTO))
    print("¡Conectado al chat! Escribe 'salir' para terminar la conversación.\n")
    
    while True:
        mensaje = input("Tú (Cliente): ")
        cliente.send(mensaje.encode('utf-8'))
        
        if mensaje.lower() == 'salir':
            break
            
        respuesta_servidor = cliente.recv(1024).decode('utf-8')
        
        if respuesta_servidor.lower() == 'salir':
            print("El servidor ha cerrado el chat.")
            break
            
        print(f"Servidor dice: {respuesta_servidor}")
        
except Exception as e:
    print(f"Error al conectar: {e}")

print("Desconectado.")
cliente.close()
