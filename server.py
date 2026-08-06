from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from core.builder import ProfileBuilder
from utils.logger import TrapLogger

class TrapHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        logger = TrapLogger()
        logger.info(f"Incoming connection from attacker: {self.client_address[0]}")
        
        # Generate fresh fake data for every request
        builder = ProfileBuilder()
        fake_data = builder.build_profile()
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(fake_data).encode('utf-8'))

def run_trap_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, TrapHandler)
    print(f"[*] DI-MixerX Live Trap running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_trap_server()
