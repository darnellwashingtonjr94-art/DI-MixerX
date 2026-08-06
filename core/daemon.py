import threading
from http.server import HTTPServer

class MultiPortDaemon:
    def __init__(self, handler_class, ports=[80, 8080, 8888]):
        self.handler_class = handler_class
        self.ports = ports
        self.threads = []

    def _start_server(self, port):
        server_address = ('', port)
        httpd = HTTPServer(server_address, self.handler_class)
        print(f"[*] Trap binding active on port {port}")
        httpd.serve_forever()

    def ignite(self):
        print("[*] Igniting Multi-Port Daemon...")
        for port in self.ports:
            t = threading.Thread(target=self._start_server, args=(port,))
            t.daemon = True
            t.start()
            self.threads.append(t)
            
        for t in self.threads:
            t.join()
