import socket
import threading

class ADBHoneypot:
    def __init__(self, port=5555):
        self.port = port

    def handle_client(self, client_socket, addr):
        print(f"[*] ADB Probe detected from {addr[0]}")
        try:
            # Send fake ADB connection acceptance sequence
            client_socket.send(b"CNXN\x00\x00\x00\x01\x00\x10\x00\x00\x17\x00\x00\x00device::ro.product.name=fake_device;")
            client_socket.recv(1024) # Swallow their command
        except Exception:
            pass
        finally:
            client_socket.close()

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('0.0.0.0', self.port))
        server.listen(5)
        print(f"[*] Fake ADB Service listening on port {self.port}")
        
        while True:
            client, addr = server.accept()
            threading.Thread(target=self.handle_client, args=(client, addr)).start()
