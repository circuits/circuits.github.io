from circuits.net.sockets import TCPServer


class EchoServer(TCPServer):

    def read(self, sock, data):
        return data

EchoServer(("0.0.0.0", 8000)).run()
