import java.io.*;
import java.net.*;
import java.util.*;

public class Servidor {

    // Lista de clientes conectados
    private static List<PrintWriter> clientesConectados =
            Collections.synchronizedList(new ArrayList<>());

    // Lista de sockets para poder cerrarlos
    private static List<Socket> socketsClientes =
            Collections.synchronizedList(new ArrayList<>());

    private static ServerSocket servidor;

    public static void main(String[] args) throws Exception {

        System.out.println("Servidor Sala de Chat iniciado...");

        servidor = new ServerSocket(81);

        System.out.println("Esperando integrantes en el puerto 81...");

        // Hilo para que Yahani pueda escribir mensajes
        Thread enviarMensajes = new Thread(() -> {

            Scanner teclado = new Scanner(System.in);

            while (true) {

                String mensaje = teclado.nextLine();

                // Si Yahani escribe salir
                if (mensaje.equalsIgnoreCase("salir")) {

                    System.out.println("Yahani salió del chat.");

                    // Avisar a todos los clientes
                    synchronized (clientesConectados) {
                        for (PrintWriter cliente : clientesConectados) {
                            cliente.println("Yahani salió del chat.");
                        }
                    }

                    // Cerrar conexiones de los clientes
                    synchronized (socketsClientes) {
                        for (Socket socket : socketsClientes) {
                            try {
                                socket.close();
                            } catch (IOException e) {
                                // Ignorar
                            }
                        }
                    }

                    // Cerrar servidor
                    try {
                        servidor.close();
                    } catch (IOException e) {
                        // Ignorar
                    }

                    break;
                }

                // Enviar mensaje de Yahani a todos
                synchronized (clientesConectados) {
                    for (PrintWriter cliente : clientesConectados) {
                        cliente.println("Yahani: " + mensaje);
                    }
                }
            }
        });

        enviarMensajes.start();

        // Esperar clientes
        try {

            while (!servidor.isClosed()) {

                Socket socket = servidor.accept();

                socketsClientes.add(socket);

                System.out.println("¡Un nuevo cliente se ha conectado!");

                new ManejadorCliente(socket).start();
            }

        } catch (SocketException e) {

            if (servidor.isClosed()) {
                System.out.println("Servidor cerrado.");
            }

        } finally {

            if (!servidor.isClosed()) {
                servidor.close();
            }
        }
    }


    // Atiende a cada cliente de manera independiente
    private static class ManejadorCliente extends Thread {

        private Socket socket;
        private PrintWriter salida;

        public ManejadorCliente(Socket socket) {
            this.socket = socket;
        }

        public void run() {

            try {

                BufferedReader entrada = new BufferedReader(
                        new InputStreamReader(socket.getInputStream())
                );

                salida = new PrintWriter(
                        socket.getOutputStream(),
                        true
                );

                clientesConectados.add(salida);

                salida.println("¡Bienvenido a la sala de chat!");

                String mensaje;

                while ((mensaje = entrada.readLine()) != null) {

                    // Si el cliente escribe salir
                    if (mensaje.equalsIgnoreCase("salir")) {

                        System.out.println("Un cliente salió del chat.");

                        salida.println("Conexión cerrada.");

                        break;
                    }

                    // Mostrar mensaje en la consola de Yahani
                    System.out.println("Cliente: " + mensaje);

                    // Reenviar mensaje a los demás clientes
                    synchronized (clientesConectados) {

                        for (PrintWriter cliente : clientesConectados) {

                            // No regresar el mensaje al mismo cliente
                            if (cliente != salida) {
                                cliente.println(mensaje);
                            }
                        }
                    }
                }

            } catch (IOException e) {

                if (!socket.isClosed()) {
                    System.out.println("Un cliente se desconectó.");
                }

            } finally {

                if (salida != null) {
                    clientesConectados.remove(salida);
                }

                socketsClientes.remove(socket);

                try {
                    socket.close();
                } catch (IOException e) {
                    // Ignorar
                }

                System.out.println(
                        "Conexión cerrada. Clientes restantes: "
                                + clientesConectados.size()
                );
            }
        }
    }
}