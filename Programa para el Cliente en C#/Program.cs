using System;
using System.Net.Sockets;
using System.Text;
using System.Threading;

class Cliente
{
    static void Main()
    {
        string ip = "192.168.218.150";
        int puerto = 81;

        try
        {
            // Crear conexión con el servidor
            TcpClient cliente = new TcpClient();
            cliente.Connect(ip, puerto);

            Console.WriteLine("Conectado al servidor.");

            NetworkStream stream = cliente.GetStream();

            // Hilo para recibir mensajes
            Thread recibir = new Thread(() =>
            {
                byte[] buffer = new byte[1024];

                try
                {
                    while (true)
                    {
                        int bytesRecibidos = stream.Read(buffer, 0, buffer.Length);

                        if (bytesRecibidos == 0)
                            break;

                        string mensaje = Encoding.UTF8.GetString(
                            buffer, 0, bytesRecibidos
                        );

                        Console.WriteLine(mensaje);
                    }
                }
                catch
                {
                    Console.WriteLine("\nConexión cerrada.");
                }
            });

            recibir.Start();

            // Enviar mensajes
            while (true)
            {
                string mensaje = Console.ReadLine();

                byte[] datos = Encoding.UTF8.GetBytes("Johan: " + mensaje + "\n");

                stream.Write(datos, 0, datos.Length);

                if (mensaje.Equals("salir",
                    StringComparison.OrdinalIgnoreCase))
                {
                    break;
                }
            }

            // Cerrar conexión
            cliente.Close();
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error: " + ex.Message);
        }
    }
}
