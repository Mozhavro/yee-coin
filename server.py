import socket


class Server:
    def __init__(self, ip="127.0.0.1", port=5000):
        self._ip = ip
        self._port = port
        self.reserver_ports = [self._port]
        self.peers_list

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def add_peer(self, name):
        last_reserved_port = self.get_reserver_ports()[-1]
        try:


    def get_reserver_ports(self):
        pass

    def reserve_ports_for_peer(self):
        pass


def main():
    server = Server()
    server.run()


if __name__ == '__main__':
    main()