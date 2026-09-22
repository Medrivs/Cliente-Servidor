import java.io.*;
import java.net.*;
import java.util.Scanner;

public class ClienteJava {
    public static void main(String[] args) throws Exception {
        Socket socket = new Socket("192.168.218.150", 81);
        BufferedReader entrada = new BufferedReader(
                new InputStreamReader(socket.getInputStream()));
        PrintWriter salida = new PrintWriter(
            
                socket.getOutputStream(), true);

        Thread recibir = new Thread(() -> {
            try {
                String mensaje;
                while ((mensaje = entrada.readLine()) != null) {
                    System.out.println(mensaje);
                }
            } catch (Exception e) {
                System.out.println("Conexión cerrada.");
            }
        });
        recibir.start();
        Scanner teclado = new Scanner(System.in);

        while (true) {
            String mensaje = teclado.nextLine();
            salida.println("Daniel: "+mensaje);

            if (mensaje.equalsIgnoreCase("salir"))
                break;
        }

        socket.close();
    }
}