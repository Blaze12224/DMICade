using System;

namespace dmipm_csharp
{
    class Program
    {
        static void Main(string[] args)
        {
            string path = "/tmp/dmicade_socket.s";

            PmClient client = new PmClient(path);

            client.Start();

            client.Send("HAHAH JEFF");
        }
    }
}
